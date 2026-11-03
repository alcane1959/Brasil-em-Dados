# Brasil em Dados

Dashboard responsivo em HTML, CSS e JavaScript para acompanhar indicadores econômicos e sociais do Brasil, comparar aplicações financeiras, simular previdência privada e calcular a valorização real de imóveis.

## Versão atual

Esta versão utiliza o GitHub como fonte única de atualização do painel.

O navegador não consulta diretamente Banco Central, IBGE, B3 ou Tesouro Direto. Ao abrir a página, o arquivo `index.html` carrega somente:

```text
./dados/painel.json
```

O arquivo `dados/painel.json` deve ser produzido e publicado pela automação do repositório.

## Funcionamento da atualização

1. A automação do GitHub coleta os dados das fontes configuradas.
2. Os resultados são normalizados e gravados em `dados/painel.json`.
3. O GitHub Pages publica o site e o arquivo de dados.
4. Ao abrir o painel, o navegador carrega automaticamente `dados/painel.json`.
5. O botão **Buscar dados publicados** força uma nova leitura desse mesmo arquivo, sem consultar fontes externas.
6. Se o arquivo publicado não estiver disponível, o painel tenta restaurar o último pacote válido salvo no navegador.

## Indicadores do painel

O painel está preparado para receber pelo JSON publicado:

- dólar, incluindo PTAX e histórico;
- meta Selic;
- CDI;
- TR;
- IPCA mensal;
- IPCA acumulado em 12 meses;
- taxa de desocupação;
- população ocupada;
- população estimada;
- Tesouro Prefixado;
- Tesouro IPCA+;
- histórico do Ibovespa.

Cada indicador pode apresentar sua data de referência e o horário de coleta registrados no arquivo publicado.

## Recursos

- cartões com indicadores econômicos e sociais;
- gráficos de dólar, Selic, inflação e desocupação;
- leitura rápida das tendências recentes;
- comparação de aplicações financeiras;
- estimativa de IR e IOF;
- cálculo de retorno líquido e retorno real;
- simulação de PGBL e VGBL;
- aportes mensais em previdência;
- comparação entre tributação regressiva e progressiva;
- cálculo estimado de imposto no saque;
- distribuição dos aportes segundo o limite fiscal informado para PGBL;
- cálculo da valorização real de imóveis;
- impressão do painel em formato de relatório;
- armazenamento local do último pacote válido como contingência.

## Estrutura esperada do repositório

```text
Brasil-em-Dados/
├── index.html
├── README.md
├── icon.ico
├── dados/
│   └── painel.json
├── scripts/
│   └── atualizar_dados.py
└── .github/
    └── workflows/
        └── atualizar-dados.yml
```

## Arquivo de dados

O `index.html` espera um pacote JSON com esta estrutura geral:

```json
{
  "app": "Brasil em Dados",
  "version": 5,
  "exportedAt": "2026-11-03T09:30:00-03:00",
  "meta": {
    "selic": {
      "reference": "03/11/2026",
      "consultedAt": "2026-11-03T09:30:00-03:00"
    }
  },
  "state": {
    "usd": [],
    "usdPtax": [],
    "selic": [],
    "cdi": [],
    "tr": [],
    "ibov": [],
    "ipca": [],
    "ipca12": [],
    "unemp": [],
    "employed": [],
    "population": [],
    "treasury": null
  }
}
```

As séries temporais devem usar registros no formato:

```json
{
  "label": "30/10/2026",
  "value": 13.75
}
```

## Botões disponíveis

### Buscar dados publicados

Relê `dados/painel.json` com cache desativado e atualiza cartões, gráficos, campos automáticos e simuladores.

### Imprimir relatório

Prepara os cálculos atuais e abre a janela de impressão do navegador. O HTML inclui estilos específicos para impressão em papel A4.

## Simulador de aplicações

O simulador compara cenários de:

- poupança;
- CDBs vinculados ao CDI;
- LCI e LCA;
- Tesouro Selic;
- Tesouro Prefixado;
- Tesouro IPCA+;
- debênture incentivada;
- fundo de renda fixa;
- fundo de ações;
- ETF de ações;
- ganho na venda de FII;
- previdência VGBL;
- previdência PGBL.

Os cálculos incluem estimativas de rendimento bruto, tributação, valor líquido, retorno líquido e retorno real acima da inflação.

## Previdência privada

A simulação contempla:

- aporte inicial;
- aportes mensais;
- separação entre PGBL e VGBL;
- limite anual informado para dedução do PGBL;
- tributação regressiva por idade de cada lote;
- estimativa progressiva;
- comparação de imposto no saque;
- resgate dos lotes mais antigos primeiro.

## Valorização real de imóvel

O cálculo usa:

```text
((1 + valorização nominal) ÷ (1 + inflação)) - 1
```

O resultado compara o valor nominal projetado com o valor corrigido pela inflação do mesmo período.

## Publicação no GitHub Pages

No repositório:

1. Abra **Settings**.
2. Entre em **Pages**.
3. Em **Build and deployment**, selecione **GitHub Actions** como fonte.
4. Confirme que o workflow está em `.github/workflows/atualizar-dados.yml`.
5. Execute o workflow uma vez para criar `dados/painel.json` e publicar a página.

## Atualização automática

O workflow pode ser configurado para:

- executar em horários agendados;
- executar manualmente pela aba Actions;
- executar quando houver alterações na branch principal.

O HTML não controla a agenda. Ele apenas lê o arquivo mais recente já publicado no GitHub.

## Contingência local

Depois de receber um pacote válido, o painel mantém uma cópia no armazenamento local do navegador. Essa cópia é usada somente quando `dados/painel.json` não pode ser carregado.

## Tecnologias utilizadas

- HTML5;
- CSS3;
- JavaScript sem frameworks;
- Canvas API;
- GitHub Actions;
- GitHub Pages;
- Python para coleta e preparação dos dados.

## Privacidade

Os cálculos são realizados no navegador. O projeto não inclui cadastro de usuários nem envio dos valores digitados nos simuladores para serviços externos.

## Observações importantes

- Os resultados financeiros são estimativas educacionais.
- Rentabilidade passada não garante rentabilidade futura.
- Tributação, taxas, inflação e regras dos produtos podem mudar.
- Os cálculos não substituem orientação financeira, contábil ou tributária profissional.
- A validade dos indicadores depende da atualização correta de `dados/painel.json` pela automação do repositório.

## Arquivo principal

Use o `index.html` testado que contém apenas uma fonte de dados:

```text
./dados/painel.json
```
