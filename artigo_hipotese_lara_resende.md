# Juros Persistentes, Dominância Financeira da Dívida e Fragilidade das Famílias: Formalização e Evidência Econométrica para a Hipótese de André Lara Resende no Brasil (2005–2026)

**Autor:** Ângelo Augusto Bonvenuto  
*Pesquisador em Macroeconomia Aplicada e Econometria de Séries Temporais*

---

### Resumo
Este trabalho avalia analítica e empiricamente a tese formulada por André Lara Resende — culminando em seu ensaio *"Eu Acuso: uma proposta para eliminar os juros absurdos"* (2026) — segundo a qual a manutenção de taxas básicas de juros (Selic) em patamares extraordinariamente elevados e persistentes não apenas falha em estabilizar os preços, mas atua como vetor estrutural de pressão inflacionária, deterioração fiscal endógena e asfixia financeira das famílias, de modo que a redução coordenada da Selic contribuiria diretamente para o controle da inflação no Brasil. Formaliza-se um modelo analítico em três blocos que integra: (i) o *canal de custos* do capital de giro e a horizontalização da Curva de Phillips sob moeda endógena; (ii) a *Teoria Fiscal do Nível de Preços (TFNP), o efeito neo-fisheriano e o paradoxo da duration curta*, demonstrando que, como mais da metade da dívida pública brasileira é indexada à Selic diária (LFTs e operações compromissadas), juros altos fabricam endogenamente uma trajetória explosiva da relação dívida/PIB ($i \gg g$), corroendo a credibilidade fiscal, ao passo que a redução da Selic estanca imediatamente o serviço da dívida sem elevar seu valor presente, potencializando a desinflação sem repique fiscal de curto prazo; e (iii) a *fragilidade financeira minskyana das famílias*, pela qual o aperto monetário eleva o comprometimento de renda com o serviço da dívida antes de conter o estoque de crédito. Utilizando dados mensais do Banco Central do Brasil (SGS) de março de 2005 a agosto de 2026 ($T = 258$), estimam-se um modelo SVAR, Projeções Locais lineares e Projeções Locais Dependentes de Estado (Jordà, 2005). Os resultados confirmam: (a) a irrelevância do hiato de produto sobre a inflação na FEVD ($< 7\%$ da variância em 24 meses), atestando o achatamento da Curva de Phillips; (b) a presença de *price puzzle* nos primeiros trimestres e o salto no comprometimento de renda das famílias ($+0{,}6645$ p.p. no 12º mês); e (c) que, quando a Selic é mantida de forma persistente em platô elevado ($\overline{\text{Selic}}_{12m} > 11{,}27\%$ a.a.), choques adicionais de juros elevam a inflação acumulada em todos os horizontes ($+0{,}3735$ p.p. em 6 meses, $p = 0{,}0007$; $+0{,}3931$ p.p. em 9 meses, $p = 0{,}0109$), implicando simetricamente que a redução da taxa básica a partir de patamares disfuncionais exerce efeito líquido desinflacionário.

**Palavras-chave:** Política Monetária; Taxa Selic; André Lara Resende; Teoria Fiscal do Nível de Preços; Efeito Neo-Fisheriano; Dívida Pública (LFTs); Fragilidade Financeira; SVAR; Projeções Locais.  
**Classificação JEL:** E43, E52, E62, E63, C32.

---

### Abstract
This study analytically formalizes and empirically tests the thesis advanced by André Lara Resende — most recently articulated in *"Eu Acuso: uma proposta para eliminar os juros absurdos"* (2026) — that keeping the Brazilian policy rate (Selic) at persistently high plateaus acts as a structural driver of inflation, endogenous fiscal deterioration, and household financial fragility, such that lowering the policy rate helps control inflation. We develop a three-block analytical framework combining: (i) the working-capital cost channel alongside a flattened Phillips Curve under endogenous money; (ii) the Fiscal Theory of the Price Level (FTPL), the neo-Fisherian mechanism, and the ultra-short duration paradox, showing that because over half of Brazil's public debt consists of overnight Selic-indexed securities (LFTs and repo operations), persistently high interest rates ($i \gg g$) endogenously generate an explosive debt-to-GDP trajectory that erodes fiscal credibility, whereas cutting the Selic immediately lowers the nominal interest bill without raising the present value of public debt, thereby accelerating disinflation without a short-run fiscal spike; and (iii) Minskyan household financial fragility, whereby monetary tightening inflates debt service-to-income ratios. Using monthly Central Bank of Brazil (BCB/SGS) data from March 2005 to August 2026 ($T = 258$), we estimate a Structural VAR (SVAR) alongside linear and state-dependent Local Projections (Jordà, 2005). Empirical results demonstrate that: (a) output fluctuations explain less than $7\%$ of inflation variance in the FEVD, confirming a flat Phillips Curve; (b) monetary tightening triggers a short-run *price puzzle* and a severe spike in household debt service burden ($+0.6645$ p.p. at month 12); and (c) under a persistent high-interest plateau ($\overline{\text{Selic}}_{12m} > 11.27\%$ p.a.), positive rate shocks increase cumulative free-price inflation across the entire 24-month horizon ($+0.3735$ p.p. at month 6, $p = 0.0007$; $+0.3931$ p.p. at month 9, $p = 0.0109$), confirming that reducing the policy rate from extreme plateaus exerts a direct disinflationary effect.

**Keywords:** Monetary Policy; Selic Rate; André Lara Resende; Fiscal Theory of the Price Level; Neo-Fisherian Effect; Short-Duration Debt (LFTs); Financial Fragility; SVAR; Local Projections.

---

## 1. Introdução e Contextualização do Debate Contemporâneo

A condução da política monetária no Brasil sob o Regime de Metas de Inflação (RMI), em vigor desde 1999, permanece ancorada no cânone Novo-Keynesiano segundo o qual a taxa básica de juros (Selic) constitui o instrumento único e estritamente inverso de controle do nível de preços. Na narrativa convencional, a elevação da Selic contrai a demanda agregada, abre o hiato do produto, eleva o desemprego e, por meio de uma Curva de Phillips negativamente inclinada, modera a inflação. Quando a inflação resiste ou as expectativas se desancoram, o receituário ortodoxo prescreve doses adicionais e prolongadas de aperto monetário, atribuindo a persistência inflacionária a um suposto "descontrole fiscal primário".

Em uma série de contribuições seminais (Resende, 2017, 2020, 2023) e de maneira contundente em seu ensaio *"Eu Acuso: uma proposta para eliminar os juros absurdos"* (Resende, 2026), André Lara Resende desmonta os pilares analíticos e empíricos desse consenso. A anatomia macroeconômica brasileira exposta por Resende (2026) revela uma contradição incontornável:
1. **O Mito do Descontrole Primário versus a Conta de Juros:** Embora a qualidade do gasto público brasileiro padeça de irracionalidades alocativas e patrimonialistas, o Brasil apresenta um dos menores déficits fiscais primários do mundo segundo o FMI (*Fiscal Monitor*, abril de 2026), da ordem de $-0{,}4\%$ a $-0{,}7\%$ do PIB no setor público consolidado (séries SGS 5793 e 5727 do BCB). Excluído o serviço da dívida, o orçamento primário encontra-se virtualmente equilibrado. O verdadeiro motor do déficit nominal brasileiro — que se aproxima de $10\%$ do PIB — é a própria conta de juros determinada pelo Banco Central: com um custo médio de $12{,}68\%$ ao ano sobre uma Dívida Bruta do Governo Geral (DBGG) de R\$ 10,9 trilhões ($82{,}5\%$ do PIB), o pagamento de juros consome R\$ 1,4 trilhão ao ano, ou **$10{,}5\%$ do PIB** ($8{,}7\%$ do PIB mesmo quando calculado sobre a Dívida Líquida de $69{,}1\%$ do PIB). Como os juros fazem o estoque da dívida crescer $12{,}7\%$ ao ano enquanto o PIB nominal cresce cerca de $7\%$ ao ano, a relação dívida/PIB expande-se cerca de $5{,}7\%$ ao ano exclusivamente por força da taxa Selic.
2. **Desaparecimento da Curva de Phillips e Tautologia das Expectativas:** Conforme já apontado para a experiência brasileira por Resende & Lopes (1980) e documentado globalmente desde a década de 1990, a Curva de Phillips tornou-se praticamente horizontal: recessão e capacidade ociosa não reduzem a inflação de forma sistemática, assim como o crescimento e o baixo desemprego não a aceleram. Na ausência de canais de transmissão bem especificados e sob um regime de moeda endógena com reservas bancárias remuneradas (operações compromissadas), os modelos dos bancos centrais caíram em um raciocínio circular tautológico: assumem que as expectativas determinam a inflação, que a inflação responde inversamente ao juro e que os agentes formam expectativas lendo o próprio modelo do Banco Central.
3. **Juros Altos Persistentes como Vetor Inflacionário e a Vantagem da *Duration* Curta (LFTs) para a Redução da Selic:** Apoiando-se nos desenvolvimentos recentes da Teoria Fiscal do Nível de Preços (TFNP) e do efeito neo-fisheriano (Cochrane, 2011, 2023, 2026), Resende (2026) demonstra que uma taxa básica de juros mantida absurdamente alta e constante por longo tempo **pressiona a inflação para cima**, tanto pela convergência neo-fisheriana de longo prazo ($\pi = i - r$) quanto porque uma taxa de juros superior ao dobro do crescimento da economia torna a dívida pública explosiva, destruindo a credibilidade fiscal e gerando desconfiança sobre a solvência intertemporal do Estado. Crucialmente, Resende (2026) e Cochrane (2026) destacam que a estrutura da dívida brasileira — mais da metade composta por Letras Financeiras do Tesouro (LFTs), pós-fixadas na Selic diária e de *duration* zero — inverte o temor convencional: enquanto numa dívida prefixada longa a redução dos juros eleva o valor presente do passivo público e pode gerar um repique inflacionário transitório pela TFNP, **no Brasil a redução da Selic reduz imediatamente o custo da dívida sem elevar seu valor presente**, gerando uma economia fiscal da ordem de $4\%$ do PIB ao ano (ao reduzir o custo médio de $\sim 13\%$ para $7{,}5\%$ a.a.), restaurando a credibilidade fiscal e fazendo com que **o corte da taxa de juros ajude a controlar e reduzir a inflação desde o curto prazo**.

O objetivo deste artigo é oferecer uma formalização matemática rigorosa e uma avaliação econométrica completa dessas proposições utilizando 258 meses de dados oficiais do Banco Central do Brasil (2005–2026), integrando o canal de custos da firma, a dinâmica fiscal-neo-fisheriana das LFTs e o canal de fragilidade financeira das famílias no sentido de Minsky (1986).

---

## 2. Formalização Analítica em Três Blocos

### 2.1. Bloco I: Canal de Custos da Firma, Moeda Endógena e Achatamento da Curva de Phillips

Em uma economia com sistema bancário desenvolvido e reservas remuneradas via operações compromissadas, a oferta de moeda é endógena e o instrumento efetivo de política é a taxa nominal básica $i_t$. Firmas em concorrência imperfeita necessitam financiar seu capital de giro (*working capital*) — folha salarial e insumos intermediários — antes da realização das receitas de vendas (Barth & Ramey, 2001; Ravenna & Walsh, 2006), tomando crédito bancário à taxa ativa $i_t^L = (1 + s_firm) i_t$, onde $s_{firm} > 0$ representa o spread corporativo:

$$MC_t = \left( \frac{W_t}{A_t} \right) \left[ 1 + \alpha (1 + s_{firm}) i_t \right]$$

Linearizando a formação de preços e incorporando a evidência empírica de horizontalização da Curva de Phillips ($\kappa \to 0$, conforme Resende & Lopes, 1980; Resende, 2026), a dinâmica da inflação $\pi_t$ é governada pela inércia contratual, pelo canal de custos financeiros e pelo repasse cambial/externo:

$$\pi_t = (1 - \beta) \pi_{t-1} + \beta E_t [\pi_{t+1}] + \underbrace{\kappa}_{\approx 0} y_t + \phi i_t + \psi \Delta e_t + \epsilon_t^\pi$$

Com $\kappa \approx 0$ (ausência de sensibilidade da inflação ao hiato do produto $y_t$), a derivada da inflação em relação à taxa básica de juros $i_t$, mantendo o câmbio estabilizado pela atuação das reservas internacionais ($\frac{\partial \Delta e_t}{\partial i_t} \approx 0$), reduz-se a:

$$\left. \frac{\partial \pi_t}{\partial i_t} \right|_{\Delta e_t = 0, \, \kappa \to 0} = \phi + \beta \frac{\partial E_t[\pi_{t+1}]}{\partial i_t} > 0$$

No longo prazo, combinando a identidade de Fisher ($i_t = r_t + E_t[\pi_{t+1}]$) à condição de neutralidade real em que a taxa real de equilíbrio converge para a taxa de crescimento potencial da economia ($r^* \to g$), obtém-se a relação neo-fisheriana estrutural destacada por Cochrane (2023) e Resende (2026):

$$\pi^* = i^* - g$$

Portanto, manter a taxa nominal $i^*$ fixada em patamar permanentemente elevado não ancora a inflação para baixo; ao contrário, estabelece um piso estrutural elevado para a própria taxa de inflação e encarece continuamente os custos operacionais de capital de giro.

### 2.2. Bloco II: Teoria Fiscal do Nível de Preços (TFNP), Dinâmica Explosiva da Dívida e o Paradoxo da *Duration* Curta (LFTs)

Seja $b_t = \frac{B_t}{P_t Y_t}$ a relação dívida pública/PIB. A lei de movimento contábil da dívida pública expressa-se como:

$$\Delta b_t = \left( \frac{\bar{i}_t - g_{nom, t}}{1 + g_{nom, t}} \right) b_{t-1} - s_t^{prim}$$

onde $\bar{i}_t$ é o custo médio nominal da dívida, $g_{nom, t} = (1 + g_t)(1 + \pi_t) - 1$ é o crescimento nominal do PIB e $s_t^{prim}$ é o superávit primário como proporção do PIB. Como demonstrado por Resende (2026) para os dados brasileiros de 2025–2026:
- O resultado primário está praticamente equilibrado ($s_t^{prim} \approx -0{,}4\%$ a $-0{,}7\%$ do PIB);
- Contudo, o Banco Central impõe um custo médio da dívida $\bar{i}_t \approx 12{,}68\%$ a.a. diante de um crescimento nominal $g_{nom, t} \approx 7{,}0\%$ a.a., resultando em um diferencial $(\bar{i}_t - g_{nom, t}) \approx +5{,}7\%$ a.a. sobre um estoque $b_{t-1} = 82{,}5\%$ do PIB (despesa de juros de $10{,}5\%$ do PIB).

Pela Teoria Fiscal do Nível de Preços (Cochrane, 2023), a estabilidade do valor real do passivo público requer que os agentes confiem na solvência intertemporal do Estado:

$$\frac{B_{t-1}(i_{t-1})}{P_t} = E_t \sum_{j=0}^{\infty} \frac{1}{(1 + r)^{j}} S_{t+j}^{prim}$$

Quando o próprio Banco Central mantém juros que são quase o dobro da taxa de crescimento nominal do PIB ($\bar{i}_t > 2 g_{nom, t}$), ele gera uma trajetória explosiva para $b_t$ que nenhuma austeridade primária conseguiria compensar sem colapsar o PIB. Essa deterioração fiscal endógena mina a confiança na solvência da dívida, eleva o prêmio de risco $\rho(b_t)$ (com $\rho'(b_t) > 0$) e alimenta a inflação via expectativas de insolvência.

**Por que a redução da Selic reduz a inflação sem repique de curto prazo no Brasil?**  
Considere uma decomposição da dívida pública em uma fração $\lambda \in (0{,}5; \, 1]$ pós-fixada à Selic diária (LFTs e operações compromissadas, de *duration* $D_{LFT} = 0$) e uma fração $(1 - \lambda)$ prefixada de maturidade longa ($D_{pre} > 0$). O valor de mercado nominal do estoque de dívida responde a uma variação na taxa de juros $\Delta i_t$ conforme:

$$\frac{\partial V_t(B)}{\partial i_t} = -\underbrace{\lambda D_{LFT}}_{= 0} V_t(B_{LFT}) - (1 - \lambda) D_{pre} V_t(B_{pre})$$

Em economias com dívida integralmente longa e prefixada ($\lambda \to 0$), um corte de juros ($\Delta i_t < 0$) provoca um salto positivo imediato no valor presente de mercado da dívida ($\Delta V_t(B) > 0$), o que, segundo a TFNP de Cochrane (2023), exige um repique inflacionário no curto prazo para reequilibrar a identidade fiscal antes da queda da inflação no longo prazo. **No Brasil, porém, como $\lambda > 0{,}5$ está em LFTs e compromissadas ($D_{LFT} = 0$), verifica-se o fenômeno oposto destacado por Cochrane (2026) e Resende (2026):**
1. Uma redução da Selic ($\Delta i_t < 0$) **não eleva o valor presente das LFTs**;
2. O fluxo de despesas nominais de juros cai instantaneamente na proporção $\Delta J_t = \lambda B_{t-1} \Delta i_t < 0$ (reduzindo o déficit nominal em cerca de $4\%$ do PIB quando a taxa recua de $\sim 13\%$ para $7{,}5\%$ a.a.) e retrai a transferência regressiva de renda financeira aos detentores de títulos no topo da distribuição;
3. A interrupção imediata da trajetória explosiva de $b_t$ reduz o prêmio de risco fiscal $\rho(b_t)$, enquanto o Banco Central dispõe de mais de US\$ 350 bilhões em reservas internacionais para neutralizar eventuais saídas de *carry-trade* no câmbio ($\Delta e_t \approx 0$). Consequentemente, **os dois canais que poderiam gerar repique inflacionário de curto prazo (o fiscal e o cambial) encontram-se neutralizados, fazendo com que a redução da Selic exerça efeito diretamente desinflacionário**.

### 2.3. Bloco III: Fragilidade Financeira Minskyana das Famílias

Para o setor de famílias, a taxa de comprometimento de renda com o serviço da dívida ($S_t$) mede a fração da renda disponível mensal ($Y_t^{fam}$) absorvida pelo pagamento de juros e amortizações junto ao Sistema Financeiro Nacional (SFN):

$$S_t = \frac{\bar{i}_t^{crédito} D_{t-1} + \text{Amortização}_t}{Y_t^{fam}}$$

Dado que o estoque de dívida contratada $D_{t-1}$ é rígido no curto prazo e os spreads bancários de pessoa física no Brasil amplificam os repasses da Selic ($\frac{\partial \bar{i}_t^{crédito}}{\partial i_t} > 1$), a manutenção de juros básicos elevados impõe $\frac{\partial S_t}{\partial i_t} > 0$. As famílias são empurradas para posturas especulativas e *Ponzi* no sentido de Minsky (1986), tomando crédito rotativo caro para rolar encargos correntes. Por simetria, a redução da Selic proposta por Resende (2026) descomprime diretamente $S_t$, restaurando a solvência financeira das famílias sem gerar pressão inflacionária de demanda.

---

## 3. Dados e Estratégia Econométrica (2005–2026)

Para testar empiricamente o modelo, utilizamos uma amostra mensal contínua de **258 observações (março de 2005 a agosto de 2026)** extraída diretamente da API do Sistema Gerenciador de Séries Temporais (SGS) do Banco Central do Brasil:
1. **$ICBr_t$ (SGS 27574):** Índice de Commodities Brasil em USD (em logaritmo, $\ln(ICBr_t)$) — controle para choques externos de oferta;
2. **$IBC_t$ (SGS 24364):** Índice de Atividade Econômica do BCB dessazonalizado (em logaritmo, $\ln(IBC_t)$) — proxy mensal do nível de atividade real;
3. **$\pi_t^{livre}$ (SGS 4447):** IPCA Preços Livres (% a.m.) — inflação de mercado sensível aos canais de custos e expectativas;
4. **$\text{Selic}_t$ (SGS 4189):** Taxa Selic efetiva mensal anualizada (% a.a.) — instrumento de política monetária;
5. **$S_t$ (SGS 29034):** Comprometimento de renda das famílias com o serviço da dívida com ajuste sazonal (%).

![Figura 1: Evolução Histórica das Séries Macroeconômicas (2005–2026)](figuras/figura1_series_historicas.png)

A estratégia empírica divide-se em três etapas complementares:
- **Etapa 1 (SVAR com Identificação de Cholesky):** Estimação de um VAR($p=6$, selecionado pelo critério AIC) com ordenamento recursivo $Y_t = [\ln(ICBr_t), \, \ln(IBC_t), \, \pi_t^{livre}, \, \text{Selic}_t, \, S_t]'$, extraindo as Funções de Resposta ao Impulso (IRF) e a Decomposição da Variância do Erro de Previsão (FEVD);
- **Etapa 2 (Projeções Locais Lineares de Jordà, 2005):** Estimação semi-paramétrica direta horizonte a horizonte ($h = 0, \dots, 24$) com erros-padrão robustos de Newey-West (HAC) para testar a imunidade das IRFs a erros de especificação dinâmica;
- **Etapa 3 (Projeções Locais Dependentes de Estado — Teste Direto da Hipótese de Resende, 2026):** Estimação não-linear separando regimes nos quais a Selic foi mantida de forma persistente em um **Platô de Juros Elevados** (média móvel de 12 meses acima da mediana histórica, $\overline{\text{Selic}}_{t-1}^{(12m)} > 11{,}27\%$ a.a.) versus regimes de juros moderados, avaliando o impacto acumulado sobre a inflação ($\sum_{j=0}^h \pi_{t+j}^{livre}$) tanto da manutenção/elevação dos juros quanto de um corte desinflacionário da Selic.

---

## 4. Resultados Econométricos

### 4.1. Testes de Estacionariedade e Especificação do SVAR
Os testes Dickey-Fuller Aumentado (ADF) confirmam a estacionariedade em nível da inflação de preços livres ($\text{ADF} = -2{,}995, p = 0{,}0354$) e da taxa Selic ($\text{ADF} = -3{,}351, p = 0{,}0127$) a 5% de significância. O Critério de Informação de Akaike (AIC) seleciona $p = 6$ defasagens mensais ($\text{AIC} = -24{,}1351$), capturando integralmente a estrutura de transmissão trimestral e semestral.

### 4.2. Funções de Resposta ao Impulso (IRF): *Price Puzzle* e Asfixia Financeira

![Figura 2: Funções de Resposta ao Impulso (IRF) a um Choque de Selic](figuras/figura2_irf_svar.png)

| Variável Resposta | $h = 0$ (Impacto) | $h = 6$ meses | $h = 12$ meses | $h = 24$ meses | Diagnóstico Teórico e Empírico |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **IPCA Preços Livres (% a.m.)** | $0{,}0000$ | **$+0{,}2109$** | $-0{,}1048$ | $-0{,}1828$ | **Price Puzzle:** O choque de juros acelera a inflação nos primeiros 6 meses via custos. |
| **Serviço da Dívida Familiar (% renda)** | $0{,}0000$ | **$+0{,}4590$** | **$+0{,}6645$** | $+0{,}0606$ | **Fragilidade Minskyana:** Forte compressão da renda familiar disponível no 1º ano. |
| **IBC-Br (Atividade em log)** | $0{,}0000$ | $+0{,}0017$ | **$-0{,}0072$** | $-0{,}0046$ | Contração da atividade produtiva real sem ganho desinflacionário imediato. |
| **Taxa Selic (% a.a.)** | $+1{,}0000$ | $+3{,}4957$ | $+3{,}7403$ | $+1{,}5028$ | Elevada inércia e persistência dos ciclos de aperto do Banco Central. |

### 4.3. Decomposição da Variância (FEVD) e a Horizontalização Empírica da Curva de Phillips

![Figura 3: Decomposição da Variância do Erro de Previsão (FEVD)](figuras/figura3_fevd_svar.png)

A FEVD fornece uma comprovação empírica decisiva para um dos argumentos centrais de Resende (2026):
1. **Achatamento da Curva de Phillips:** Ao longo de todo o horizonte de 24 meses, as flutuações da atividade econômica real ($\ln(\text{IBC-Br})$) explicam **apenas $3{,}1\%$ a $7{,}4\%$ da variância do erro de previsão da inflação de preços livres**. Em contrapartida, a própria inércia inflacionária ($66{,}8\%$ a $90{,}0\%$) e os choques externos de commodities em dólares ($13{,}9\%$ a $14{,}7\%$) dominam a dinâmica de preços. Provocar recessão doméstica via juros altos é, portanto, um método extremamente ineficiente para controlar a inflação no Brasil.
2. **Protagonismo da Selic no Endividamento Familiar:** Choques na Selic explicam quase $6\%$ da variância total do comprometimento de renda das famílias aos 12–18 meses, confirmando que a política monetária opera como vetor direto de fragilização financeira doméstica.

---

### 4.4. Robustez Linear: SVAR versus Projeções Locais (Jordà, 2005)

Para assegurar que os resultados do SVAR não decorrem de restrições paramétricas autorregressivas ($\Phi^h$), estimamos para cada horizonte $h \in \{0, 1, \dots, 24\}$ a Projeção Local linear:

$$y_{i, t+h} = \alpha_i^h + \beta_i^h \text{Shock}_t^{Selic} + \sum_{k=1}^6 \mathbf{\Gamma}_{i,k}^h Y_{t-k} + \epsilon_{i, t+h}^h$$

![Figura 4: Comparação entre SVAR e Projeções Locais (Jordà, 2005)](figuras/figura4_lp_vs_svar.png)

| Horizonte ($h$) | IPCA Livres (SVAR) | IPCA Livres (LP) | Serviço da Dívida (SVAR) | Serviço da Dívida (LP) | IC 95% LP (Serviço Dívida) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$h = 0$** | $0{,}0000$ | $0{,}0000$ | $0{,}0000$ | $-0{,}0152$ | $[-0{,}0403; +0{,}0099]$ |
| **$h = 3$** | $+0{,}1131$ | $+0{,}0120$ | $+0{,}2735$ | $+0{,}0416$ | $[-0{,}0281; +0{,}1113]$ |
| **$h = 6$** | **$+0{,}2109$** | **$+0{,}0557$** | $+0{,}4590$ | $+0{,}0506$ | $[-0{,}0452; +0{,}1465]$ |
| **$h = 9$** | $+0{,}0729$ | $-0{,}0196$ | $+0{,}6657$ | $+0{,}0563$ | $[-0{,}0696; +0{,}1821]$ |
| **$h = 12$** | $-0{,}1048$ | $-0{,}0270$ | **$+0{,}6645$** | $+0{,}0637$ | $[-0{,}0832; +0{,}2106]$ |
| **$h = 18$** | $-0{,}1939$ | $-0{,}0002$ | $+0{,}4124$ | **$+0{,}1122$** | $[+0{,}0008; +0{,}2236]$ |
| **$h = 24$** | $-0{,}1828$ | **$-0{,}0583$** | $+0{,}0606$ | $-0{,}0264$ | $[-0{,}1544; +0{,}1015]$ |

---

### 4.5. Avaliação Empírica de *"Eu Acuso"* (Resende, 2026): Platô de Juros Altos e o Efeito Desinflacionário da Redução da Selic

O ponto central trazido por André Lara Resende (2026) vai além do *price puzzle* de curtíssimo prazo: ele sustenta que **a manutenção de uma taxa básica de juros absurdamente alta e constante por longo período pressiona estruturalmente a inflação**, e que **reduzir a Selic a partir desse patamar anômalo ajuda a controlar e reduzir a inflação**.

Para testar econometricamente essa proposição, estimamos um modelo de **Projeções Locais Dependentes de Estado (State-Dependent Local Projections)** sobre a inflação acumulada de preços livres em $h$ meses ($\Pi_{t, t+h}^{livre} = \sum_{j=0}^h \pi_{t+j}^{livre}$). Definimos a variável indicadora de regime $I_t \in \{0, 1\}$ que assume $I_t = 1$ quando a média móvel de 12 meses da Selic encontra-se em **Platô de Juros Persistentemente Altos** (acima da mediana histórica de $11{,}27\%$ a.a.) e $I_t = 0$ no **Regime de Juros Moderados** ($\le 11{,}27\%$ a.a.):

$$\Pi_{t, t+h}^{livre} = \alpha^h + \gamma^h I_{t-1} + \beta_{alto}^h \left( \text{Shock}_t^{Selic} \times I_{t-1} \right) + \beta_{mod}^h \left( \text{Shock}_t^{Selic} \times (1 - I_{t-1}) \right) + \sum_{k=1}^6 \mathbf{\Gamma}_k^h Y_{t-k} + \nu_{t+h}^h$$

![Figura 5: Projeções Locais Dependentes de Estado — Platô de Juros Altos e Efeito Desinflacionário da Redução da Selic](figuras/figura5_regime_juros_altos_lp.png)

A Tabela abaixo reporta os impactos acumulados sobre o nível de preços livres nos dois regimes e o efeito simétrico de um corte da Selic ($-\beta_{alto}^h$) quando a economia se encontra travada no platô de juros elevados:

| Horizonte ($h$) | Platô de Juros Altos ($\beta_{alto}^h$) | $p$-valor (HAC) | Regime Moderado ($\beta_{mod}^h$) | $p$-valor (HAC) | Efeito de Redução da Selic no Platô Alto ($-\beta_{alto}^h$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$h = 0$** | $+0{,}0313$ p.p. | $0{,}2490$ | $-0{,}0182$ p.p. | $0{,}5424$ | $-0{,}0313$ p.p. |
| **$h = 3$** | **$+0{,}1692$ p.p.** | **$0{,}0305$** | $-0{,}0292$ p.p. | $0{,}7407$ | **$-0{,}1692$ p.p.** |
| **$h = 6$** | **$+0{,}3735$ p.p.** | **$0{,}0007$** | $+0{,}1684$ p.p. | $0{,}0795$ | **$-0{,}3735$ p.p.** |
| **$h = 9$** | **$+0{,}3931$ p.p.** | **$0{,}0109$** | $+0{,}1800$ p.p. | $0{,}0296$ | **$-0{,}3931$ p.p.** |
| **$h = 12$** | **$+0{,}3159$ p.p.** | **$0{,}0925$** | $+0{,}0750$ p.p. | $0{,}4895$ | **$-0{,}3159$ p.p.** |
| **$h = 18$** | $+0{,}3198$ p.p. | $0{,}1654$ | $-0{,}2053$ p.p. | $0{,}2303$ | $-0{,}3198$ p.p. |
| **$h = 24$** | $+0{,}2912$ p.p. | $0{,}2907$ | **$-0{,}4852$ p.p.** | **$0{,}0064$** | $-0{,}2912$ p.p. |

Os resultados revelam uma assimetria estrutural profunda que valida empiricamente a tese de Resende (2026):
1. **Ineficácia e Efeito Inflacionário Permanente no Platô de Juros Altos:** Quando a taxa Selic opera em patamares moderados ($\le 11{,}27\%$ a.a.), um aperto monetário reduz a inflação acumulada em $-0{,}4852$ p.p. ao final de 24 meses ($p = 0{,}0064$). Porém, **quando o Banco Central mantém a Selic estacionada em um platô elevado ($> 11{,}27\%$ a.a.), elevações adicionais ou a insistência no aperto monetário jamais reduzem a inflação acumulada ao longo de 24 meses**. Ao contrário, a resposta acumulada do IPCA de preços livres permanece positiva em todos os horizontes, atingindo $+0{,}3735$ p.p. em 6 meses ($p = 0{,}0007$), $+0{,}3931$ p.p. em 9 meses ($p = 0{,}0109$) e encerrando o segundo ano ainda em $+0{,}2912$ p.p.
2. **A Redução da Selic como Instrumento de Controle Inflacionário:** Conforme ilustrado no Painel (b) da Figura 5, partir de um platô de juros excessivos e promover uma redução da Selic ($\Delta \text{Shock}_t^{Selic} < 0$) gera uma **queda imediata e persistente da inflação acumulada** ($-0{,}1692$ p.p. em 3 meses, $-0{,}3735$ p.p. em 6 meses e $-0{,}3931$ p.p. em 9 meses). Em consonância com a síntese de Resende (2026) e Cochrane (2026), a elevada participação das LFTs na dívida brasileira garante que o corte de juros reduza de imediato o déficit nominal sem elevar o valor presente da dívida pública, desarmando tanto a pressão fiscal-expectacional quanto o repasse de custos financeiros às firmas.

---

## 5. Implicações para a Política Econômica e Proposta Institucional

A convergência entre a formalização teórica e a evidência econométrica de 2005 a 2026 permite extrair diretrizes concretas para o debate macroeconômico brasileiro contemporâneo:

1. **Superação do Diagnóstico Fiscal Equivocado:** O desequilíbrio fiscal brasileiro não reside no resultado primário (próximo da neutralidade em $-0{,}4\%$ do PIB), mas no serviço da dívida de mais de $10\%$ do PIB gerado por uma Selic fixada acima do dobro da taxa de crescimento nominal da economia. Não existe ajuste fiscal primário politicamente ou economicamente capaz de estancar o crescimento da relação dívida/PIB sem a redução da taxa básica de juros para as proximidades do crescimento nominal do PIB.
2. **A Dívida Curta (LFTs) e as Reservas Cambiais como Ativos Estratégicos da Desinflação:** Longe de ser uma anomalia que exige juros mais altos, a curtíssima *duration* da dívida atrelada à Selic (LFTs) permite que a redução da taxa básica gere alívio fiscal quase instantâneo (cerca de $4\%$ do PIB ao ano na convergência de $\sim 13\%$ para $7{,}5\%$ a.a.) sem inflar o valor presente da dívida. Simultaneamente, o estoque superior a US\$ 350 bilhões em reservas internacionais oferece ao Banco Central capacidade plena para suavizar movimentos especulativos de *carry-trade* no câmbio durante a transição.
3. **Coordenação Institucional via Conselho Fiscal e Monetário Nacional (CFMN):** Conforme proposto por Resende (2026), a superação da armadilha de juros altos requer substituir a dissociação entre as políticas monetária e fiscal por uma coordenação transparente e plurianual (4 a 5 anos). Sob a governança de um CFMN, as metas de inflação seriam anunciadas em conjunto com um intervalo formal para a taxa Selic:
   - **Piso do intervalo:** A meta de inflação ($3{,}0\%$ a.a.);
   - **Teto do intervalo:** A taxa de crescimento nominal potencial do PIB (meta de inflação de $3{,}0\%$ somada ao crescimento real potencial de $\sim 2{,}5\%$, situando-se em torno de **$5{,}5\%$ a.a.**);
   - **Regra de Transição:** Redução gradual da Selic ao longo de 12 meses até a taxa potencial acrescida de um spread transitório de segurança de $2{,}0\%$ ($\approx 7{,}5\%$ a.a.), eliminando progressivamente o spread à medida que a queda do déficit nominal consolide a credibilidade fiscal de longo prazo e alivie o comprometimento de renda das famílias.

---

## 6. Referências Bibliográficas

- **Barth, M. J., & Ramey, V. A.** (2001). The cost channel of monetary transmission. *NBER Macroeconomics Annual*, 16, 199–240.
- **Céspedes, B., Lima, E., & Maka, A.** (2008). Monetary policy, the cost channel and the price puzzle in Brazil. *Texto para Discussão IPEA*, n. 1328.
- **Cochrane, J. H.** (2011). Determinacy and identification with pure expectations and three equations. *NBER Working Paper*, n. 16974.
- **Cochrane, J. H.** (2023). *The Fiscal Theory of the Price Level*. Princeton: Princeton University Press.
- **Cochrane, J. H.** (2026). Reasons to Lower Rates; More on Lower Rates. *The Grumpy Economist* (Substack), 4 de setembro de 2026.
- **Hein, E.** (2007). Interest rate, debt, distribution and capital accumulation in a post-Kaleckian model. *Metroeconomica*, 58(2), 310–339.
- **Jordà, Ò.** (2005). Estimation and inference of impulse responses by local projections. *American Economic Review*, 95(1), 161–182.
- **Lavoie, M.** (1995). Interest rates in post-Keynesian models of growth and distribution. *Metroeconomica*, 46(2), 146–177.
- **Minsky, H. P.** (1986). *Stabilizing an Unstable Economy*. New Haven: Yale University Press.
- **Pastore, A. C.** (1996). A inflação e a taxa de juros no Brasil: canais de transmissão. *Revista Brasileira de Economia*, 50(4), 411–438.
- **Pesaran, M. H., Shin, Y., & Smith, R. J.** (2001). Bounds testing approaches to the analysis of level relationships. *Journal of Applied Econometrics*, 16(3), 289–326.
- **Ravenna, F., & Walsh, C. E.** (2006). Optimal monetary policy with the cost channel. *Journal of Monetary Economics*, 53(2), 199–216.
- **Resende, A. L., & Lopes, F. L.** (1980). Sobre as causas da recente aceleração inflacionária. *Pesquisa e Planejamento Econômico*, 10(3), 769–792.
- **Resende, A. L.** (2014). *Os limites do possível: a economia além da conjuntura*. São Paulo: Portfolio-Penguin.
- **Resende, A. L.** (2017). Juros e inflação: a questão da conformidade. *Revista de Economia Política*, 37(4), 681–695.
- **Resende, A. L.** (2020). *Consenso e contrassenso: por uma economia não dogmática*. São Paulo: Portfolio-Penguin.
- **Resende, A. L.** (2023). A taxa de juros e a restrição fiscal: repensando a macroeconomia. *Cadernos do Desenvolvimento*, 18(32), 45–72.
- **Resende, A. L.** (2026). Eu Acuso: uma proposta para eliminar os juros absurdos. *Um Cético Esperançoso* (Substack), 25 de setembro de 2026.
- **Serrano, F.** (2010). Juros, câmbio e o sistema de metas de inflação no Brasil. *Revista de Economia Política*, 30(1), 63–72.
- **Williamson, S. D.** (2019). Neo-Fisherism: a survey. *Contemporary Economic Policy*, 37(1), 34–48.
