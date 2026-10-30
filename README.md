# Brasil em Dados

Dashboard responsivo desenvolvido em HTML, CSS e JavaScript para acompanhar indicadores econômicos do Brasil, comparar aplicações financeiras, simular previdência privada e calcular a valorização real de imóveis.

## Visão geral

O projeto reúne, em uma única página, indicadores públicos, gráficos, comparações financeiras e ferramentas de simulação. A interface foi construída para funcionar em computadores, celulares e tablets, com suporte a impressão em formato de relatório.

## Principais recursos

- Consulta de indicadores econômicos e sociais.
- Exibição de IPCA mensal e acumulado em 12 meses.
- Consulta da cotação de compra do dólar.
- Exibição da meta Selic.
- Indicadores de desocupação, população ocupada e população estimada.
- Gráficos de dólar, Selic, inflação e desocupação.
- Comparação de aplicações financeiras.
- Estimativa de rendimento bruto, imposto, valor líquido e retorno real.
- Simulação de PGBL e VGBL.
- Cálculo de aportes mensais em previdência.
- Distribuição anual entre PGBL e VGBL conforme o limite fiscal informado.
- Comparação entre tributação regressiva e progressiva.
- Estimativa de imposto sobre saques da previdência.
- Simulação da valorização real de imóveis.
- Layout responsivo e versão otimizada para impressão.

## Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript
- Canvas API para os gráficos
- APIs públicas do Banco Central do Brasil e do IBGE/SIDRA

## Estrutura básica

```text
projeto/
├── index.html
├── README.md
├── manifest.webmanifest     # necessário para instalação como PWA
├── service-worker.js        # necessário para funcionamento offline
└── icons/                   # ícones utilizados pelo aplicativo
```

> No arquivo atual, a aplicação principal está concentrada em `index.html`. Os demais arquivos da estrutura acima são necessários somente se o projeto for configurado como PWA.

## Como executar localmente

### Opção simples

Abra o arquivo `index.html` em um navegador moderno.

Algumas consultas externas podem ser bloqueadas quando o arquivo é aberto diretamente pelo protocolo `file://`. Nesse caso, execute o projeto por um servidor local.

### Servidor local com Python

No terminal, dentro da pasta do projeto, execute:

```bash
python -m http.server 8000
```

Depois, abra no navegador:

```text
http://localhost:8000
```

### Servidor local com Visual Studio Code

Também é possível utilizar uma extensão de servidor local, como o Live Server, e abrir o arquivo `index.html` por ela.

## Uso do simulador financeiro

1. Informe o valor inicial da aplicação.
2. Se desejar, informe o valor do aporte mensal.
3. Defina o prazo em meses.
4. Revise as taxas usadas na comparação.
5. Para previdência privada, informe a renda bruta tributável anual.
6. Informe o valor que pretende sacar.
7. Compare os resultados dos regimes regressivo e progressivo.

### Premissas da previdência

- O limite do PGBL é calculado por ano-calendário.
- Os aportes destinados ao PGBL respeitam o limite de 12% da renda tributável anual informada.
- Depois de atingir esse limite, o excedente é direcionado ao VGBL na simulação.
- Os aportes mensais são considerados no fim de cada mês.
- No regime regressivo, cada aporte possui sua própria idade tributária.
- A simulação de resgate utiliza primeiro os lotes mais antigos.
- No PGBL, o imposto é estimado sobre o valor retirado.
- No VGBL, o imposto é estimado somente sobre a parcela de rendimentos.
- A estimativa progressiva utiliza a tabela anual de 2026 como referência constante para comparação.
- Regras tributárias futuras, deduções pessoais e condições específicas do plano podem alterar o resultado real.

## Impressão do relatório

Use o botão **Imprimir relatório** disponível na página. O projeto possui estilos específicos para impressão em papel A4.

## Fontes de dados

O painel consulta séries e tabelas públicas, incluindo:

- Banco Central do Brasil, por meio do SGS.
- IBGE/SIDRA.
- Tabela 1737 para dados do IPCA.
- Tabela 6381 para desocupação.
- Tabela 6318 para população ocupada.
- Tabela 6579 para população estimada.
- Série 432 do Banco Central para a meta Selic.
- Série 10813 do Banco Central para a cotação de compra do dólar.

A disponibilidade dos indicadores depende da resposta das fontes externas e das permissões do navegador.

## Instalação no computador

### No Google Chrome ou Microsoft Edge:

1. Abra o endereço publicado do projeto.
2. Aguarde o carregamento completo da página.
3. Clique no ícone de instalação exibido na barra de endereço ou abra o menu do navegador.
4. Selecione **Instalar aplicativo** ou **Instalar este site como aplicativo**.
5. Confirme a instalação.

Depois disso, o aplicativo poderá ser aberto pelo menu Iniciar, pela área de trabalho ou pelo gerenciador de aplicativos do sistema.

## Instalação no celular ou tablet

### Em navegadores compatíveis:

1. Abra o endereço do projeto.
2. Acesse o menu do navegador.
3. Selecione **Instalar aplicativo** ou **Adicionar à tela inicial**.
4. Confirme o nome e a instalação.

O ícone será adicionado à tela inicial do dispositivo.

## Observações

- A disponibilidade e o nome da opção de instalação podem variar conforme o navegador e o sistema operacional.
- Abrir somente o arquivo `index.html` pelo computador não garante a instalação como PWA.
- O projeto deve ser publicado em HTTPS para utilizar os recursos completos de instalação e service worker.
- O funcionamento offline depende da configuração do `service-worker.js` e dos arquivos adicionados ao cache.
- Atualizações no projeto podem exigir a atualização da versão do cache do service worker.
- Para que o navegador ofereça a instalação completa, o projeto precisa incluir e registrar os arquivos de PWA, como o manifesto, o service worker e os ícones.

---

## Limitações

- Os resultados financeiros são estimativas educacionais.
- Taxas, inflação, tributação e preços dos ativos podem mudar.
- O simulador não substitui orientação contábil, tributária ou financeira profissional.
- A tabela progressiva de 2026 é mantida constante em projeções futuras apenas para comparação.
- O cálculo não reproduz todas as regras e particularidades de cada instituição ou produto financeiro.
- A disponibilidade dos dados econômicos depende das APIs externas.

## Privacidade

Os cálculos são realizados no navegador. O projeto não possui, por padrão, mecanismo próprio de cadastro ou armazenamento de dados pessoais.

## Aviso

> Este projeto é uma demonstração educacional desenvolvida para estudos de HTML, CSS e JavaScript. A empresa mencionada é fictícia e qualquer semelhança com empresas reais é mera coincidência.

Your site is live at https://alcane1959.github.io/Brasil-em-Dados/

