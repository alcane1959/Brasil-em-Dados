#!/usr/bin/env python3
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from datetime import datetime, timedelta, timezone
from pathlib import Path
from html.parser import HTMLParser
import csv, io, json, re, time

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dados'/'painel.json'
OUT.parent.mkdir(parents=True,exist_ok=True)
TZ=timezone(timedelta(hours=-3))

def now_iso(): return datetime.now(TZ).isoformat(timespec='seconds')
def get(url, text=False, timeout=90):
 req=Request(url,headers={'User-Agent':'Mozilla/5.0 BrasilEmDadosGitHub/1.0','Accept-Language':'pt-BR,pt;q=0.9'})
 with urlopen(req,timeout=timeout) as r: raw=r.read(); charset=r.headers.get_content_charset() or 'utf-8'
 decoded=raw.decode(charset,errors='replace')
 return decoded if text else json.loads(decoded)
def br_date(d): return d.strftime('%d/%m/%Y')
def us_date(d): return d.strftime('%m-%d-%Y')
def parse_num(v):
 v=re.sub(r'[^0-9,.-]','',str(v)).replace('.','').replace(',','.')
 try:return float(v)
 except:return None

def sidra_label(row):
 for k in sorted((x for x in row if re.fullmatch(r'D\d+C',x)), key=lambda x:int(x[1:-1])):
  code=str(row.get(k,'')).strip()
  if re.fullmatch(r'(19|20|21)\d{2}([01]\d)?',code): return row.get(k[:-1]+'N') or code
 return row.get('D3N') or row.get('D2N') or row.get('D1N') or ''

def normalize_bcb(payload):
 result=[]
 for row in payload if isinstance(payload,list) else []:
  try:value=float(str(row.get('valor','')).replace(',','.'))
  except:continue
  result.append({'label':row.get('data',''),'value':value})
 return result

def normalize_sidra(payload):
 result=[]
 for row in payload[1:] if isinstance(payload,list) and len(payload)>1 else []:
  try:value=float(str(row.get('V','')).replace(',','.'))
  except:continue
  result.append({'label':sidra_label(row),'value':value})
 return result

def normalize_ptax(payload):
 result=[]
 for row in payload.get('value',[]) if isinstance(payload,dict) else []:
  try:value=float(row.get('cotacaoCompra'))
  except:continue
  raw=str(row.get('dataHoraCotacao',''));m=re.match(r'^(\d{4})-(\d{2})-(\d{2})',raw);label=f'{m.group(3)}/{m.group(2)}/{m.group(1)}' if m else raw
  result.append({'label':label,'dateTime':raw,'value':value})
 result.sort(key=lambda x:x['dateTime'])
 return result

def meta_from_bcb(payload): return payload[-1].get('data','não informada') if payload else 'não informada'
def meta_from_sidra(payload): return sidra_label(payload[-1]) if isinstance(payload,list) and len(payload)>1 else 'não informada'

class TableParser(HTMLParser):
 def __init__(self): super().__init__();self.tables=[];self.table=None;self.row=None;self.cell=None
 def handle_starttag(self,tag,attrs):
  if tag=='table':self.table=[]
  elif tag=='tr' and self.table is not None:self.row=[]
  elif tag in ('th','td') and self.row is not None:self.cell=[]
 def handle_data(self,data):
  if self.cell is not None:self.cell.append(data)
 def handle_endtag(self,tag):
  if tag in ('th','td') and self.cell is not None:self.row.append(' '.join(self.cell).strip());self.cell=None
  elif tag=='tr' and self.row is not None:
   if self.row:self.table.append(self.row)
   self.row=None
  elif tag=='table' and self.table is not None:self.tables.append(self.table);self.table=None

def parse_ibov(html):
 p=TableParser();p.feed(html);table=next((t for t in p.tables if t and any('Dia' in c for c in t[0]) and any('Jan' in c for c in t[0])),None)
 if not table: raise ValueError('tabela diária do Ibovespa não encontrada')
 ym=re.search(r'IBovespa\s*-\s*(20\d{2})',html,re.I);year=int(ym.group(1)) if ym else datetime.now().year
 months={'jan':1,'fev':2,'mar':3,'abr':4,'mai':5,'jun':6,'jul':7,'ago':8,'set':9,'out':10,'nov':11,'dez':12}
 header=[re.sub(r'\s+',' ',c).strip().lower()[:3] for c in table[0]];points=[]
 for row in table[1:]:
  try: day=int(row[0])
  except: continue
  if not 1<=day<=31:continue
  for i,val in enumerate(row[1:],1):
   if i>=len(header) or header[i] not in months or not val.strip():continue
   num=parse_num(val)
   if num is None or num<1000:continue
   try:d=datetime(year,months[header[i]],day)
   except:continue
   points.append({'label':d.strftime('%d/%m/%Y'),'value':num})
 points.sort(key=lambda x:datetime.strptime(x['label'],'%d/%m/%Y'))
 if len(points)<2:raise ValueError('histórico insuficiente do Ibovespa')
 return points

def parse_treasury(raw):
 rows=list(csv.reader(io.StringIO(raw.lstrip('\ufeff')),delimiter=';'))[1:]
 items=[]
 for r in rows:
  if len(r)>=2:items.append({'title':r[0].strip(),'yield':r[1].strip(),'maturity':r[4].strip() if len(r)>4 else ''})
 prefix=sorted((x for x in items if re.match(r'^Tesouro Prefixado \d',x['title'])),key=lambda x:x['maturity'])
 ipca=sorted((x for x in items if re.match(r'^Tesouro IPCA\+ \d',x['title'])),key=lambda x:x['maturity'])
 if not prefix or not ipca:raise ValueError('títulos Prefixado/IPCA+ não encontrados')
 return {'prefix':parse_num(prefix[0]['yield']),'ipca':parse_num(ipca[0]['yield']),'prefixTitle':prefix[0]['title'],'ipcaTitle':ipca[0]['title']}

def main():
 old={}
 if OUT.exists():
  try:old=json.loads(OUT.read_text(encoding='utf-8'))
  except:pass
 state=dict(old.get('state') or {});meta=dict(old.get('meta') or {});errors=[];now=datetime.now(TZ);start=now-timedelta(days=14);period=20
 specs={
 'usd':(f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/{period}?formato=json','bcb'),
 'selic':(f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/{period}?formato=json','bcb'),
 'cdi':('https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados/ultimos/1?formato=json','bcb'),
 'tr':('https://api.bcb.gov.br/dados/serie/bcdata.sgs.7812/dados/ultimos/1?formato=json','bcb'),
 'ipca':(f'https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/63/p/last%20{period}/d/v63%202','sidra'),
 'ipca12':('https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/2265/p/last%201/d/v2265%202','sidra'),
 'unemp':(f'https://apisidra.ibge.gov.br/values/t/6381/n1/all/v/4099/p/last%20{period}/d/v4099%201','sidra'),
 'employed':(f'https://apisidra.ibge.gov.br/values/t/6318/n1/all/v/1641/p/last%20{period}/c629/32387/d/v1641%201','sidra'),
 'population':('https://apisidra.ibge.gov.br/values/t/6579/n1/all/v/9324/p/last%201/d/v9324%201','sidra')}
 for key,(url,kind) in specs.items():
  try:
   payload=get(url);normalized=normalize_bcb(payload) if kind=='bcb' else normalize_sidra(payload);
   if not normalized:raise ValueError('resposta sem valores válidos')
   state[key]=normalized;ref=normalized[-1]['label'];meta[key]={'reference':ref,'consultedAt':now_iso()}
  except Exception as e:errors.append(f'{key}: {e}')
 try:
  url=f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='{us_date(start)}'&@dataFinalCotacao='{us_date(now)}'&$top=100&$format=json&$select=cotacaoCompra,dataHoraCotacao"
  payload=get(url);normalized=normalize_ptax(payload);
  if not normalized:raise ValueError('PTAX sem valores válidos')
  state['usdPtax']=normalized;meta['usdPtax']={'reference':normalized[-1]['label'],'consultedAt':now_iso()}
 except Exception as e:errors.append(f'usdPtax: {e}')
 try:
  raw=get('https://www.tesourodireto.com.br/documents/d/guest/rendimento-investir-csv?download=true',text=True);t=parse_treasury(raw);state['treasury']=t;meta['treasury']={'reference':t['prefixTitle']+' / '+t['ipcaTitle'],'consultedAt':now_iso()}
 except Exception as e:errors.append(f'treasury: {e}')
 try:
  html=get('https://sistemaswebb3-listados.b3.com.br/indexStatisticsPage/daily-evolution/IBOVESPA?language=pt-br',text=True);pts=parse_ibov(html);state['ibov']=pts;meta['ibov']={'reference':pts[-1]['label'],'consultedAt':now_iso()}
 except Exception as e:errors.append(f'ibov: {e}')
 package={'app':'Brasil em Dados','version':5,'exportedAt':now_iso(),'meta':meta,'state':state,'errors':errors}
 OUT.write_text(json.dumps(package,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'saved':str(OUT),'errors':errors},ensure_ascii=False))
 if not state:raise SystemExit(1)
if __name__=='__main__':main()
