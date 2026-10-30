# Brasil em Dados

Dashboard web responsivo para acompanhar indicadores econômicos e sociais do Brasil usando dados públicos do IBGE e do Banco Central do Brasil.

## Visão geral

O projeto reúne, em uma única página, indicadores de inflação, juros, câmbio, população e mercado de trabalho. Também oferece uma calculadora de valorização real de imóveis e um relatório otimizado para impressão ou salvamento em PDF.

O sistema foi desenvolvido em HTML, CSS e JavaScript puro. Não exige instalação de bibliotecas ou frameworks.

## Funcionalidades

- IPCA mensal
- IPCA acumulado em 12 meses
- Cotação do dólar americano para compra
- Meta da taxa Selic
- Taxa de desocupação
- População ocupada
- População estimada do Brasil
- Gráficos de evolução dos indicadores
- Seleção do período exibido
- Atualização dos dados sob demanda
- Leitura automática das tendências recentes
- Calculadora de valorização real de imóveis
- Impressão do relatório em formato A4
- Opção de salvar o relatório como PDF pelo navegador
- Layout responsivo para computadores, tablets e celulares
- Tratamento de indisponibilidade das fontes de dados
- Campos monetários inicialmente vazios, com orientação dentro das caixas
- Validação antes de executar as simulações

## Fontes de dados

| Indicador | Fonte | Série ou tabela |
|---|---|---|
| IPCA | IBGE / SIDRA | Tabela 1737 |
| Taxa de desocupação | IBGE / SIDRA | Tabela 6381 |
| População ocupada | IBGE / SIDRA | Tabela 6318 |
| População estimada | IBGE / SIDRA | Tabela 6579 |
| Meta Selic | Banco Central / SGS | Série 432 |
| Dólar americano, compra | Banco Central / SGS | Série 10813 |

Os períodos de referência podem variar porque cada indicador segue seu próprio calendário de divulgação.

## Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript
- Canvas API para os gráficos
- Fetch API para consulta das fontes públicas
- CSS de impressão para geração do relatório

## Como executar

### Opção 1: abrir diretamente

1. Baixe o arquivo `brasil_em_dados_v7.html`.
2. Abra o arquivo em um navegador moderno.
3. Aguarde o carregamento das fontes oficiais.

Alguns navegadores podem restringir consultas de um arquivo aberto localmente. Caso algum indicador apareça como indisponível, utilize um servidor local ou publique o arquivo em um serviço de hospedagem estática.

### Opção 2: executar em um servidor local

Com Python instalado, abra o terminal na pasta do projeto e execute:

```bash
python -m http.server 8000
```

Depois, acesse:

```text
http://localhost:8000/brasil_em_dados_v7.html
```

## Como publicar

O projeto é estático e pode ser publicado em serviços como:

- GitHub Pages
- Netlify
- Cloudflare Pages
- Azure Static Web Apps
- Qualquer hospedagem que aceite arquivos HTML

Antes da publicação, você pode renomear `brasil_em_dados_v7.html` para `index.html`. Assim, o dashboard será carregado na página inicial do site.

## Calculadora de valorização real

A calculadora compara a valorização nominal de um imóvel com a inflação acumulada no mesmo período.

O campo **Valor inicial do imóvel (R$)** começa vazio. Dentro da caixa, a mensagem *Digite o valor inicial do imóvel* orienta o preenchimento. O cálculo só é realizado depois que o usuário informa um valor válido.

Fórmula utilizada:

```text
Valorização real = ((1 + valorização nominal) / (1 + inflação)) - 1
```

Exemplo:

- Valorização nominal: 6%
- Inflação: 4,58%
- Valorização real aproximada: 1,36%

O cálculo não inclui aluguéis, manutenção, reformas, impostos, vacância, corretagem ou outros custos de aquisição e venda.


## Simulador de aplicações financeiras

O simulador compara cenários de poupança, CDB, LCI, LCA, Tesouro Direto, debêntures incentivadas, fundos, ETFs e FIIs. Os resultados incluem rendimento bruto, imposto estimado, valor líquido, retorno líquido e retorno real acima da inflação.

O campo **Valor aplicado (R$)** começa vazio. Dentro da caixa, a mensagem *Digite o valor que deseja aplicar* orienta o usuário. Enquanto esse campo não for preenchido, a tabela informa que o valor aplicado é obrigatório e não executa a simulação.

Os demais parâmetros permanecem editáveis, incluindo prazo, CDI, Selic, IPCA, TR, taxa prefixada, adicional do IPCA+, cenário de renda variável e taxa do fundo.

As taxas exibidas são cenários para comparação e não representam promessa de rentabilidade ou oferta de uma instituição financeira.

## Impressão do relatório

1. Aguarde a atualização dos dados.
2. Ajuste os valores da calculadora, se necessário.
3. Clique em **Imprimir relatório**.
4. Escolha uma impressora ou selecione **Salvar como PDF**.

Na impressão, os controles de navegação são ocultados e o conteúdo é reorganizado para papel A4.

## Estrutura sugerida do repositório

```text
brasil-em-dados/
├── index.html  # versão publicada do brasil_em_dados_v7.html
├── README.md
└── LICENSE
```

## Observações

- Os dados são obtidos de fontes públicas e podem sofrer revisões.
- O dashboard depende da disponibilidade das APIs consultadas.
- Os indicadores podem ter periodicidades diferentes.
- Este projeto tem finalidade informativa e educacional.
- As informações exibidas não constituem recomendação financeira ou de investimento.

## Melhorias futuras

- Comparação por estado e região
- Mapa interativo do Brasil
- Histórico ampliado dos indicadores
- Exportação dos dados em CSV
- Alternância entre tema claro e escuro
- Inclusão de PIB, rendimento médio e informalidade
- Configuração personalizada dos indicadores do relatório

### Instalação no computador

### No Google Chrome ou Microsoft Edge:

  1. Abra o endereço publicado do projeto.
  2. Aguarde o carregamento completo da página.
  3. Clique no ícone de instalação exibido na barra de endereço ou abra o menu do navegador.
  4. Selecione Instalar aplicativo ou Instalar este site como aplicativo.
  5. Confirme a instalação.

Depois disso, o aplicativo poderá ser aberto pelo menu Iniciar, pela área de trabalho ou pelo gerenciador de aplicativos do sistema.

### Instalação no celular ou tablet

### Em navegadores compatíveis:

1. Abra o endereço do projeto.
2. Acesse o menu do navegador.
3. Selecione Instalar aplicativo ou Adicionar à tela inicial.
4. Confirme o nome e a instalação.

O ícone será adicionado à tela inicial do dispositivo.

**Observações**

A disponibilidade e o nome da opção de instalação podem variar conforme o navegador e o sistema operacional.
Abrir somente o arquivo index.html pelo computador não garante a instalação como PWA.
O projeto deve ser publicado em HTTPS para utilizar os recursos completos de instalação e service worker.
O funcionamento offline depende da configuração do service-worker.js e dos arquivos adicionados ao cache.
Atualizações no projeto podem exigir a atualização da versão do cache do service worker.

## Licença

Defina uma licença antes da publicação pública. Para projetos abertos, uma opção comum é a licença MIT. Se optar por ela, adicione um arquivo `LICENSE` ao repositório.

## Autor

Projeto desenvolvido como dashboard independente para visualização de indicadores públicos do Brasil.

---

## Aviso

> Este projeto é uma demonstração educacional desenvolvida para estudos de HTML, CSS e JavaScript. A empresa mencionada é fictícia e qualquer semelhança com empresas reais é mera coincidência.
