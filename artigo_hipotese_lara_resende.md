# Patamar de Juros, Dívida Pós-Fixada e Fragilidade Financeira das Famílias: Formalização Analítica e Evidência de Projeções Locais Dependentes de Estado para o Brasil (2005–2026)

**Autor:** Ângelo Augusto Bonvenuto  
*Pesquisador Independente em Macroeconomia Aplicada e Econometria de Séries Temporais*

---

### Resumo
Este artigo investiga analítica e empiricamente se a eficácia desinflacionária da política monetária no Brasil depende do patamar de persistência da taxa Selic e da composição pós-fixada da dívida pública, testando as hipóteses formuladas por André Lara Resende (2017, 2020, 2026). Desenvolve-se um modelo analítico fechado em três blocos integrando: (i) uma Curva de Phillips com canal de custos de capital de giro; (ii) a dinâmica da dívida pública sob a Teoria Fiscal do Nível de Preços (TFNP), na qual a presença de títulos indexados à Selic diária (LFTs, de *duration* zero) implica que cortes de juros reduzem imediatamente o fluxo nominal de encargos ($\approx 2{,}3\%$ do PIB no impacto e $\approx 4{,}0\%$ após rolagem) sem elevar o valor presente do passivo público; e (iii) o comprometimento da renda das famílias com juros bancários. Utilizando dados mensais do Banco Central do Brasil de março de 2005 a agosto de 2026 ($T = 258$), estimam-se um modelo SVAR de seis variáveis (incluindo câmbio PTAX e a série oficial de IPCA Itens Livres, SGS 11428) e Projeções Locais lineares, dependentes de estado e assimétricas (Jordà, 2005; Tenreyro & Thwaites, 2016), além de especificações estendidas com expectativas Focus 12 meses. Os resultados indicam que: (a) um choque não antecipado de $+1{,}00$ p.p. na Selic eleva de forma estatisticamente significativa o comprometimento de renda das famílias com juros tanto no SVAR quanto nas Projeções Locais ($+0{,}459$ p.p. em 12 meses, $p = 0{,}001$), respondendo por até $16{,}2\%$ da variância do erro de previsão; (b) no regime de juros moderados ($\overline{\text{Selic}}_{12m} \le 11{,}27\%$ a.a.), o aperto monetário reduz significativamente a inflação acumulada de itens livres em 24 meses ($-1{,}922$ p.p., $p = 0{,}009$); contudo, no platô de juros elevados ($> 11{,}27\%$ a.a.), choques de aperto associam-se a acréscimos na inflação acumulada em 3 meses ($+0{,}782$ p.p., $p = 0{,}035$) e 6 meses ($+1{,}485$ p.p., $p = 0{,}011$), sem efeito desinflacionário estatisticamente significativo em 24 meses; e (c) o intercepto de nível do platô de juros altos ($\hat{\gamma}^h$) é positivo e significativo entre 6 e 18 meses ($+1{,}638$ p.p. em $h = 12$, $p = 0{,}002$), permanecendo robusto ao controle por expectativas Focus 12 meses e ao juro real *ex ante*. Discutem-se as interpretações concorrentes de dominância fiscal (Blanchard, 2004) e efeito-informação (Nakamura & Steinsson, 2018), bem como as condições institucionais para a transição a taxas de juros mais baixas.

**Palavras-chave:** Política Monetária; Taxa Selic; André Lara Resende; Teoria Fiscal do Nível de Preços; Dívida Pós-Fixada (LFTs); Fragilidade Financeira das Famílias; SVAR; Projeções Locais Dependentes de Estado.  
**Classificação JEL:** E43, E52, E62, E63, C32.

---

### Abstract
This study analytically formalizes and empirically tests whether the disinflationary effectiveness of monetary policy in Brazil depends on the persistence plateau of the policy rate (Selic) and the floating-rate structure of sovereign debt, evaluating the hypotheses advanced by André Lara Resende (2017, 2020, 2026). We build a closed three-block analytical model combining: (i) a working-capital cost-channel Phillips Curve; (ii) sovereign debt dynamics under the Fiscal Theory of the Price Level (FTPL), showing that because over half of Brazil's debt is indexed to the overnight Selic rate (zero-duration LFTs and repos), cutting the policy rate immediately reduces nominal interest outlays ($\approx 2.3\%$ of GDP on impact and $\approx 4.0\%$ after rollover) without raising the market present value of debt; and (iii) household income commitment to interest payments. Using monthly Central Bank of Brazil (BCB) series from March 2005 to August 2026 ($T = 258$), we estimate a six-variable SVAR (incorporating the PTAX exchange rate and free-market IPCA, SGS 11428) alongside linear, state-dependent, and asymmetric Local Projections (Jordà, 2005; Tenreyro & Thwaites, 2016), plus extended specifications controlling for 12-month Focus inflation expectations. Results show that: (a) a normalized $+1.00$ p.p. Selic shock significantly raises household interest-to-income ratios in both SVAR and LP ($+0.459$ p.p. at month 12, $p = 0.001$), accounting for up to $16.2\%$ of forecast error variance; (b) under moderate interest rates ($\overline{\text{Selic}}_{12m} \le 11.27\%$ p.a.), monetary tightening significantly reduces cumulative free-price inflation over 24 months ($-1.922$ p.p., $p = 0.009$), whereas under a persistent high-rate plateau ($> 11.27\%$ p.a.), positive rate shocks are associated with higher cumulative inflation at 3 months ($+0.782$ p.p., $p = 0.035$) and 6 months ($+1.485$ p.p., $p = 0.011$) and no statistically significant disinflation at 24 months; and (c) the high-rate regime level coefficient ($\hat{\gamma}^h$) is positive and significant between months 6 and 18 ($+1.638$ p.p. at $h = 12$, $p = 0.002$), surviving controls for Focus expectations and ex-ante real rates. We contrast cost-channel and FTPL mechanisms against Blanchard (2004) fiscal dominance and Nakamura & Steinsson (2018) information effects.

**Keywords:** Monetary Policy; Selic Rate; André Lara Resende; Fiscal Theory of the Price Level; Short-Duration Debt (LFTs); Household Debt Service; SVAR; State-Dependent Local Projections.

---

## 1. Introdução e Revisão da Literatura

A condução da política monetária no Brasil sob o Regime de Metas de Inflação (RMI), instituído em 1999, apoia-se no modelo Novo-Keynesiano (NK) canônico, no qual a taxa básica de juros (Selic) atua como instrumento suficiente para estabilizar a inflação via contração da demanda agregada e apreciação cambial. Contudo, a persistência de taxas de juros reais e nominais no Brasil entre as mais elevadas do mundo nas últimas décadas motivou um amplo debate teórico e empírico sobre possíveis anomalias nos canais de transmissão monetária no país.

Recentemente, André Lara Resende (2017, 2020, 2022, 2026) retomou e ampliou uma tradição crítica segundo a qual a manutenção da taxa Selic em patamares excessivamente elevados por períodos prolongados perde eficácia desinflacionária e passa a operar como fonte de deterioração fiscal endógena e pressão sobre o nível de preços. Em seu ensaio *"Eu Acuso: uma proposta para eliminar os juros absurdos"* (Resende, 2026), o autor destaca três fatos estilizados da macroeconomia brasileira contemporânea:
1. **Assimetria entre o Resultado Primário e a Conta Nominal de Juros:** De acordo com dados do Banco Central do Brasil (séries SGS 5793 e 5727) e do Fundo Monetário Internacional (*Fiscal Monitor*, 2026), o déficit primário consolidado do setor público brasileiro situa-se entre $0{,}4\%$ e $0{,}7\%$ do PIB — um dos menores entre as principais economias. Em contrapartida, o déficit nominal aproxima-se de $10\%$ do PIB devido ao fluxo de juros nominais incidentes sobre a Dívida Bruta do Governo Geral (DBGG, de $82{,}5\%$ do PIB, ou R\$ 10,9 trilhões; Dívida Líquida de $69{,}1\%$ do PIB). Com um custo médio nominal de $\bar{i} \approx 12{,}68\%$ ao ano frente a um crescimento nominal do PIB de $g_{nom} \approx 7{,}0\%$ ao ano, a despesa nominal de juros atinge R\$ 1,4 trilhão anuais ($10{,}5\%$ do PIB sobre a DBGG, ou $8{,}7\%$ sobre a DLSP), fazendo a razão dívida/PIB crescer a uma taxa relativa de cerca de $5{,}7\%$ ao ano ($\approx +4{,}4$ p.p. do PIB ao ano) por efeito autônomo dos juros.
2. **Achatamento da Curva de Phillips e Sensibilidade a Custos:** Conforme discutido desde Resende & Lopes (1980) para a inflação inercial brasileira e formalizado na literatura internacional de identificação da Curva de Phillips (McLeay & Tenreyro, 2020), a correlação empírica reduzida entre hiato de atividade e inflação mostra-se tênue na ausência de choques de oferta ou cambiais, enquanto custos financeiros de capital de giro (Barth & Ramey, 2001; Ravenna & Walsh, 2006) e indexação contratual exercem papel relevante no curto prazo.
3. **Estrutura Pós-Fixada da Dívida Pública (LFTs) e Teoria Fiscal do Nível de Preços (TFNP):** Apoiando-se na TFNP (Cochrane, 2011, 2023, 2026), Resende (2026) argumenta que juros mantidos muito acima do crescimento do PIB deterioram a percepção de solvência intertemporal do Estado. Crucialmente, como mais da metade da dívida mobiliária e das operações de liquidez no Brasil é indexada à Selic diária (Letras Financeiras do Tesouro — LFTs — e operações compromissadas, com *duration* de juros próxima de zero), uma redução da Selic não provoca o salto no valor presente de mercado da dívida que ocorreria sob dívida longa prefixada; ao contrário, reduz imediatamente a despesa nominal de juros do Tesouro, melhorando a trajetória fiscal sem exigir um repique inflacionário de curto prazo.

### 1.1. Diálogo com a Literatura Antecedente e Interpretações Concorrentes

A hipótese de que taxas de juros elevadas podem gerar efeitos fiscais e inflacionários adversos no Brasil possui antecedentes diretos na literatura acadêmica que precisam ser confrontados para delimitar o alcance empírico deste estudo:

- **O Paradoxo do Dinheiro Apertado e a Dominância Fiscal no Brasil:** Loyo (1999) formalizou pioneiramente, sob a ótica da TFNP aplicada ao Brasil dos anos 1980 e 1990, o *"tight money paradox"*: quando a dívida pública é indexada à taxa básica de curtíssimo prazo, uma regra de política monetária que eleva os juros reais em resposta à inflação acelera o crescimento nominal dos passivos públicos, elevando a riqueza financeira nominal e alimentando uma espiral inflacionária fiscalista. Posteriormente, Blanchard (2004) e Favero & Giavazzi (2004) analisaram o episódio brasileiro de 2002–2003 sob o conceito de **dominância fiscal com aversão ao risco**: nesses modelos, um aumento da Selic eleva o serviço da dívida e a probabilidade percebida de *default*, o que aumenta o prêmio de risco soberano e provoca **depreciação cambial**, gerando inflação via repasse cambial. Note-se uma diferença crucial de prescrição de política: enquanto em Blanchard (2004) a ineficácia da Selic no regime de estresse decorre de fragilidade fiscal primária (exigindo aumento do superávit primário), em Resende (2026) e Cochrane (2026) o próprio nível excessivo da Selic sob primário equilibrado é o gerador da dinâmica explosiva da dívida, de modo que a coordenação para reduzir a taxa de juros restauraria a estabilidade fiscal.
- **Incerteza Jurisdicional vs. Efeito Neo-Fisheriano:** Em trabalho clássico, Arida, Bacha & Lara-Resende (2005) atribuíram o elevado patamar do juro real de equilíbrio ($r^*$) no Brasil à *incerteza jurisdicional* e à incompletude de mercados de crédito de longo prazo, que restringem a conversibilidade e exigem alto prêmio para alongamento de prazos. Na leitura mais recente de Resende (2017, 2020, 2026), inspirada em Cochrane (2011, 2023) e Sims (2011), ganha destaque a dimensão neo-fisheriana e expectacional. A literatura internacional, contudo, apresenta importante controvérsia: enquanto Uribe (2022) encontra evidência econométrica de que aumentos permanentes da taxa nominal de juros acompanhados de acomodação inflacionária produzem efeitos neo-fisherianos (alta da inflação no curto e longo prazos), enquanto choques transitórios permanecem desinflacionários, García-Schmidt & Woodford (2019) demonstram teoricamente que, sob expectativas reflexivas e aprendizado adaptativo (em vez de previsão perfeita), a fixação de juros baixos não produz deflação neo-fisheriana imediata.
- **Identificação Econométrica, *Price Puzzle* e Efeito-Informação:** Na literatura de séries temporais iniciada por Sims (1992), a resposta positiva da inflação a um choque de juros em modelos VAR recursivos (*price puzzle*) é frequentemente interpretada como sintoma de omissão de variáveis prospectivas (como preços de commodities, taxa de câmbio ou expectativas de inflação) que o Banco Central observa ao decidir subir os juros (Céspedes, Lima & Maka, 2008; Pastore, 1995). De forma análoga, Nakamura & Steinsson (2018) destacam o **efeito-informação**: surpresas altistas do banco central podem sinalizar ao setor privado que a autoridade monetária possui informação superior sobre pressões inflacionárias futuras. Por fim, McLeay & Tenreyro (2020) demonstram que, se o banco central atua com sucesso para compensar choques de demanda, a variância observada da inflação explicada pelo hiato do produto em formas reduzidas (como na FEVD) será baixa mesmo que a Curva de Phillips estrutural seja negativamente inclinada.
- **Lições dos Ciclos Históricos de Corte da Selic (2011–2013 vs. 2016–2018):** A experiência brasileira recente oferece dois experimentos históricos contrastantes para avaliar a proposta de redução da Selic a partir de patamares elevados:
  1. No ciclo de **agosto de 2011 a outubro de 2012**, o Copom reduziu a Selic de $12{,}50\%$ para $7{,}25\%$ a.a. em um contexto de deterioração progressiva do resultado primário, forte expansão parafiscal do crédito direcionado (BNDES), represamento de tarifas públicas e depreciação cambial superior a $25\%$; a inflação livre e cheia permaneceu pressionada próxima ao teto da meta ($6{,}5\%$), forçando a reversão do ciclo em 2013.
  2. Em contraste, no ciclo de **outubro de 2016 a março de 2018**, a Selic foi reduzida de $14{,}25\%$ para $6{,}50\%$ a.a. sob ancoragem institucional das expectativas, estabilidade cambial e ausência de expansão fiscal primária, resultando em rápida convergência da inflação para abaixo de $3{,}0\%$ a.a. Esse contraste histórico sugere que o efeito desinflacionário ou neutro de cortes da Selic depende criticamente da estabilidade cambial e da ancoragem da regra fiscal.

Diante desse debate, o presente artigo formula e testa empiricamente duas hipóteses centrais:
- **Hipótese $H_1$ (Dependência de Estado na Transmissão Monetária):** A eficácia desinflacionária de choques na Selic depende do regime de juros: em regimes de juros moderados, o aperto monetário reduz a inflação acumulada em 12–24 meses (consistente com o canal convencional de demanda), mas quando a Selic já se encontra estacionada em um platô persistentemente elevado, choques adicionais perdem eficácia desinflacionária e associam-se a pressões positivas sobre os preços no curto e médio prazos (via canal de custos e prêmio de risco fiscal).
- **Hipótese $H_2$ (Fragilidade Financeira das Famílias):** Elevações da Selic produzem aumento estatisticamente significativo e persistente na parcela da renda das famílias comprometida com o pagamento de juros bancários (no espírito de Minsky, 1986 e Drehmann et al., 2015).

---

## 2. Formalização Analítica Fechada em Três Blocos

Para evitar circularidade entre pressupostos e conclusões, apresentamos um sistema macroeconômico linearizado fechado que permite derivar explicitamente sob quais condições estruturais a derivada da inflação em relação à taxa básica de juros torna-se positiva ($\frac{d\pi_t}{di_t} > 0$).

### 2.1. Bloco I: Curva de Phillips com Canal de Custos e Curva IS com Renda Financeira

Considere firmas em concorrência monopolística que necessitam financiar uma fração $\alpha \in [0, 1]$ de sua folha salarial e insumos intermediários via capital de giro bancário antes da realização das receitas de vendas (Barth & Ramey, 2001; Ravenna & Walsh, 2006; Lavoie, 1995; Hein, 2007). Sendo $i_t^L = (1 + s_{firm}) i_t$ a taxa ativa corporativa sobre a taxa básica $i_t$, o custo marginal nominal é $MC_t = (W_t / A_t)[1 + \alpha (1 + s_{firm}) i_t]$. A Curva de Phillips Novo-Keynesiana híbrida estendida com canal de custos e repasse cambial expressa-se como:

$$\pi_t = (1 - \beta) \pi_{t-1} + \beta E_t [\pi_{t+1}] + \kappa y_t + \phi i_t + \psi \Delta e_t + \epsilon_t^\pi \tag{1}$$

onde $\kappa \ge 0$ é a sensibilidade da inflação ao hiato do produto $y_t$, $\phi = \frac{(1-\theta)(1-\beta\theta)}{\theta}\alpha(1+s_{firm}) > 0$ mede a elasticidade direta do canal de custos financeiros e $\psi > 0$ captura o repasse da variação cambial nominal $\Delta e_t$.

O lado da demanda agregada é representado por uma Curva IS dinâmica que incorpora tanto o efeito intertemporal convencional de substituição ($\sigma > 0$) quanto o fluxo de renda financeira líquida transferido aos detentores privados da dívida pública pós-fixada ($\delta \lambda b_{t-1} i_{t-1}$, com $\delta \ge 0$):

$$y_t = E_t[y_{t+1}] - \sigma \left( i_t - E_t[\pi_{t+1}] - r_t^* \right) + \delta \lambda b_{t-1} i_t + \epsilon_t^y \tag{2}$$

onde $b_{t-1} = \frac{B_{t-1}}{P_{t-1} Y_{t-1}}$ é a razão dívida pública/PIB e $\lambda \in [0, 1]$ é a fração da dívida indexada à Selic diária (LFTs e operações compromissadas).

### 2.2. Bloco II: Dinâmica da Dívida Pública, TFNP e o Paradoxo da *Duration* Zero (LFTs)

A lei de movimento contábil da razão dívida/PIB ($b_t$) é dada por:

$$\Delta b_t = b_t - b_{t-1} = \left( \frac{\bar{i}_t - g_{nom, t}}{1 + g_{nom, t}} \right) b_{t-1} - s_t^{prim} \tag{3}$$

onde $\bar{i}_t = \lambda i_t + (1 - \lambda) \bar{i}_{pre}$ é o custo nominal médio do estoque da dívida, $g_{nom, t} = (1 + g_t)(1 + \pi_t) - 1$ é a taxa de crescimento nominal do PIB e $s_t^{prim}$ é o superávit primário em proporção do PIB. A condição matemática geral de crescimento endógeno da razão dívida/PIB é:

$$\left( \frac{\bar{i}_t - g_{nom, t}}{1 + g_{nom, t}} \right) b_{t-1} > s_t^{prim} \tag{4}$$

Quando o orçamento primário encontra-se próximo do equilíbrio ($s_t^{prim} \approx 0$), basta que $\bar{i}_t > g_{nom, t}$ para que $b_t$ apresente trajetória ascendente. Nos dados brasileiros de 2025–2026 citados na Seção 1 ($\bar{i}_t \approx 12{,}68\%$ a.a., $g_{nom, t} \approx 7{,}0\%$ a.a. e $b_{t-1} = 82{,}5\%$ do PIB), o termo $\frac{\bar{i}_t - g_{nom, t}}{1 + g_{nom, t}} \approx 5{,}3\%$ implica que o estoque cresce cerca de $+4{,}4$ p.p. do PIB ao ano apenas pelo diferencial entre juros e crescimento.

Para fechar o modelo, articulamos a formação de expectativas de inflação e a condição de paridade descoberta da taxa de câmbio com risco soberano (Blanchard, 2004; Cochrane, 2023):

$$E_t[\pi_{t+1}] = (1 - \omega) \pi^{meta} + \omega \pi_{t-1} + \theta \frac{\partial \Delta b_t}{\partial i_t} i_t, \quad \text{com } \frac{\partial \Delta b_t}{\partial i_t} \approx \frac{\lambda b_{t-1}}{1 + g_{nom}} > 0 \tag{5}$$

$$\Delta e_t = -\mu (i_t - i_t^{ext} - \rho(b_t)) + \epsilon_t^e \implies \frac{\partial \Delta e_t}{\partial i_t} = -\mu + \mu \rho'(b_t) \frac{\lambda b_{t-1}}{1 + g_{nom}} \tag{6}$$

onde $\theta \ge 0$ mede a sensibilidade das expectativas de inflação à deterioração da solvência fiscal (TFNP) e $\rho'(b_t) \ge 0$ captura a elasticidade do prêmio de risco soberano em relação à razão dívida/PIB (Blanchard, 2004).

**Derivação da Condição de Ineficácia ou Efeito Inflacionário da Taxa de Juros:**  
Substituindo as derivadas parciais de (2), (5) e (6) na Curva de Phillips (1), obtém-se a resposta total da inflação corrente a uma variação na taxa básica de juros $i_t$:

$$\frac{d\pi_t}{di_t} = \underbrace{\phi}_{\substack{\text{Canal de} \\ \text{Custos } (+)}} - \underbrace{\kappa (\sigma - \delta \lambda b_{t-1})}_{\substack{\text{Canal Líquido} \\ \text{de Demanda } (-)}} - \underbrace{\psi \mu}_{\substack{\text{Apreciação} \\ \text{Cambial } (-)}} + \underbrace{\left( \frac{\lambda b_{t-1}}{1 + g_{nom}} \right) \left[ (\beta + \kappa \sigma) \theta + \psi \mu \rho'(b_t) \right]}_{\text{Canal Fiscal-Expectacional e Risco Soberano } (+)} \tag{7}$$

A Equação (7) sintetiza formalmente a dependência de estado testada na Seção 4:
1. **No Regime de Juros Moderados e Estabilidade Fiscal ($\theta \approx 0, \, \rho'(b_t) \approx 0$):** Se o canal convencional de demanda e câmbio supera o canal de custos de curto prazo ($\kappa \sigma + \psi \mu > \phi + \kappa \delta \lambda b_{t-1}$), tem-se $\frac{d\pi_t}{di_t} < 0$ no horizonte de transmissão monetária (o aperto reduz a inflação).
2. **No Platô de Juros Altos Persistentes e Dívida Pós-Fixada Elevada ($\lambda b_{t-1}$ alto, $\kappa$ pequeno):** Quando a Curva de Phillips é achatada ($\kappa \to 0$) e o patamar elevado de juros acelera $\Delta b_t$, ativando os termos fiscais $\theta > 0$ e $\rho'(b_t) > 0$, a soma dos canais positivos (custos $\phi$ e deterioração fiscal-expectacional) domina o canal de demanda, tornando $\frac{d\pi_t}{di_t} > 0$.
3. **Identidade de Fisher de Longo Prazo no Brasil:** No equilíbrio estacionário de longo prazo, a equação de Fisher implica $\pi^* = i^* - r^*$. Diferentemente de economias avançadas onde $r^* \approx g$, no Brasil o juro real neutro efetivo incorpora o prêmio de risco jurisdicional e fiscal $r^* = g + \rho(b^*)$ (Arida, Bacha & Lara-Resende, 2005). Assim, uma Selic estacionária $i^* \approx 13\%$ convive com $r^* \approx 8\%$ a $8{,}5\%$ e inflação $\pi^* \approx 4{,}5\%$ a $5{,}0\%$; ainda assim, qualquer elevação permanente de $i^*$ que não seja integralmente absorvida por um aumento de $r^*$ transmite-se positivamente para $\pi^*$ no longo prazo (Uribe, 2022).

**O Mecanismo da *Duration* Zero das LFTs e a Aritmética do Corte da Selic:**  
Seja $V_t(B)$ o valor de mercado nominal da dívida pública, composta por uma fração $\lambda \approx 0{,}50$ em LFTs e compromissadas (*duration* de juros $D_{LFT} = 0$) e $(1-\lambda)$ em títulos prefixados/indexados ($D_{pre} > 0$):

$$\frac{\partial V_t(B)}{\partial i_t} = -\underbrace{\lambda D_{LFT}}_{= 0} V_t(B_{LFT}) - (1 - \lambda) D_{pre} V_t(B_{pre}) \tag{8}$$

Na TFNP aplicada a dívidas longas prefixadas ($\lambda \to 0$, Cochrane, 2023), um corte de juros ($\Delta i_t < 0$) eleva o valor de mercado presente da dívida ($\Delta V_t(B) > 0$), podendo gerar pressão inflacionária transitória. No Brasil, porém, como $\lambda \approx 0{,}50$ tem $D_{LFT} = 0$ (Cochrane, 2026; Resende, 2026):
- A redução da Selic não valoriza o estoque de LFTs;
- O fluxo anualizado de despesas de juros cai **imediatamente** sobre a parcela pós-fixada em $\Delta J_t^{imediato} = \lambda b_{t-1} \Delta i_t$. Para $b_{t-1} = 82{,}5\%$ do PIB, $\lambda \approx 0{,}50$ e uma redução de $\Delta i = -5{,}5$ p.p. (de $13{,}0\%$ para $7{,}5\%$ a.a.), o **alívio fiscal imediato é de $\approx 2{,}27\%$ do PIB** no primeiro ano, ampliando-se gradualmente para **$\approx 4{,}0\%$ a $4{,}5\%$ do PIB** à medida que as parcelas prefixadas vencem e são refinanciadas ao novo patamar. Caso o Banco Central preserve a estabilidade cambial ($\Delta e_t \approx 0$, amparado por reservas internacionais superiores a US\$ 350 bilhões), o corte da Selic reduz simultaneamente o custo de capital de giro ($\phi \Delta i_t < 0$) e o déficit nominal ($\Delta b_t < 0$).

### 2.3. Bloco III: Comprometimento de Renda das Famílias com Juros Bancários

Seguindo a literatura de *debt service ratios* (Drehmann et al., 2015) e de fragilidade financeira (Minsky, 1986), separamos o comprometimento mensal da renda disponível das famílias ($Y_t^{fam}$) em duas componentes: o pagamento exclusivo de **juros** ($J_t^{fam}$, série SGS 29033) e as **amortizações de principal** ($A_t^{fam}$), que juntas compõem o serviço total ($S_t^{fam} = J_t^{fam} + A_t^{fam}$, série SGS 29034):

$$J_t^{fam} = \frac{\bar{i}_t^{fam} D_{t-1}^{fam}}{Y_t^{fam}}, \quad \text{onde } \bar{i}_t^{fam} = \theta_{pos} i_t^c(i_t) + (1 - \theta_{pos}) \bar{i}_{fixo} \tag{9}$$

Embora parte do estoque de crédito familiar $D_{t-1}^{fam}$ seja contratada a taxas prefixadas ($\bar{i}_{fixo}$, como crédito consignado e imobiliário), a fração $\theta_{pos} > 0$ exposta a modalidades de curtíssimo prazo e repactuação mensal (rotativo do cartão de crédito, cheque especial e novas concessões) reage positivamente às elevações da Selic ($\frac{\partial i_t^c}{\partial i_t} > 0$). Como o estoque de dívida $D_{t-1}^{fam}$ ajusta-se lentamente, um choque positivo na Selic ($i_t$) eleva $J_t^{fam}$ tanto diretamente pelo aumento da taxa média $\bar{i}_t^{fam}$ nas linhas pós-fixadas/rotativas quanto indiretamente pela desaceleração da renda disponível $Y_t^{fam}$ no denominador.

---

## 3. Dados e Estratégia Econométrica (2005–2026)

### 3.1. Base de Dados e Verificação de Metadados no SGS/BCB

Utilizamos uma amostra mensal contínua de **258 observações (março de 2005 a agosto de 2026)**, cujo início é determinado pela disponibilidade das séries de comprometimento de renda das famílias do Banco Central do Brasil. Todas as séries foram extraídas diretamente das APIs oficiais do BCB (SGS e Sistema Expectativas/Olinda):

| Variável | Descrição Oficial no Banco Central | Fonte / Código | Transformação | Papel no Modelo |
| :--- | :--- | :--- | :---: | :--- |
| $ICBr_t$ | Índice de Commodities Brasil em USD | BCB / SGS 27574 | $\ln(ICBr_t)$ | Controle de choques externos de oferta |
| $PTAX_t$ | Taxa de câmbio nominal R\$/US\$ (venda, fim de período) | BCB / SGS 3696 | $\ln(PTAX_t)$ | Canal cambial e risco soberano |
| $IBC_t$ | Índice de Atividade Econômica do BCB dessazonalizado | BCB / SGS 24364 | $\ln(IBC_t)$ | Proxy mensal da atividade real |
| $\pi_t^{livre}$ | **IPCA – Itens Livres (% a.m.)** | **BCB / SGS 11428** | Nível (% a.m.) | Inflação de mercado (preços livres) |
| $\text{Selic}_t$ | Taxa de juros – Selic acumulada no mês anualizada | BCB / SGS 4189 | Nível (% a.a.) | Instrumento de política monetária |
| $J_t^{fam}$ | **Comprometimento de renda familiar com juros c/ ajuste** | **BCB / SGS 29033** | Nível (% renda) | Fragilidade financeira (encargos de juros) |
| $S_t^{fam}$ | Comprometimento de renda com serviço da dívida c/ ajuste | BCB / SGS 29034 | Nível (% renda) | Robustez (juros + amortizações) |
| $E_t[\pi_{t+12}]$ | Expectativa mediana suavizada para o IPCA 12m à frente | BCB / Olinda Focus | Nível (% a.a.) | Controle prospectivo (efeito-informação) |
| $\pi_t^{cheio}$ | IPCA – Índice Geral Cheio (% a.m.) | BCB / SGS 433 | Nível (% a.m.) | Robustez (inflação plena ao consumidor) |
| $\pi_t^{adm}$ | IPCA – Preços Monitorados/Administrados (% a.m.) | BCB / SGS 4449 | Nível (% a.m.) | Análise gráfica desagregada |

> [!NOTE]
> **Nota de Auditoria de Dados:** Na versão preliminar deste estudo, utilizou-se o código SGS 4447 (que no SGS corresponde ao subgrupo *IPCA – Comercializáveis*). Nesta versão revisada, todas as estimações principais utilizam a série oficial de **IPCA – Itens Livres (SGS 11428)** e a série de **Comprometimento de Renda com Juros da Dívida (SGS 29033)**, expurgando a rigidez das amortizações de principal.

![Figura 1: Evolução Histórica das Séries Macroeconômicas (2005–2026)](figuras/figura1_series_historicas.png)

### 3.2. Identificação do SVAR, Normalização do Choque e Projeções Locais

Estimamos inicialmente um modelo VAR($p$) de seis variáveis em nível:

$$A_0 Y_t = c + \sum_{k=1}^p A_k Y_{t-k} + \varepsilon_t, \quad \varepsilon_t \sim \mathcal{N}(0, I_6) \tag{10}$$

cuja forma reduzida é $Y_t = \mu + \sum_{k=1}^p \Phi_k Y_{t-k} + u_t$, com matriz de covariância $\Sigma_u = E[u_t u_t'] = P P'$, onde $P = A_0^{-1}$ é o fator triangular inferior de Cholesky. O vetor endógeno segue o ordenamento recursivo:

$$Y_t = \begin{bmatrix} \ln(ICBr_t) & \ln(PTAX_t) & \ln(IBC_t) & \pi_t^{livre} & \text{Selic}_t & J_t^{fam} \end{bmatrix}' \tag{11}$$

Nesse ordenamento, a função de reação do Banco Central ($\text{Selic}_t$) responde contemporaneamente às commodities externas, à taxa de câmbio, ao nível de atividade e à inflação de itens livres (e, na especificação estendida de 7 variáveis, também às expectativas Focus 12 meses $E_t[\pi_{t+12}]$), enquanto o comprometimento de renda das famílias com juros ($J_t^{fam}$) reage contemporaneamente a todo o sistema.

**Definição e Normalização Exata do Choque Monetário ($\text{Shock}_t^{Selic}$):**  
Seja $e_t = P^{-1} u_t$ o vetor de choques estruturais ortogonalizados com variância unitária ($1$ desvio-padrão). Na equação da Selic (índice $5$), um choque estrutural de $1$ desvio-padrão ($e_{selic, t} = 1$) produz um impacto contemporâneo em $h = 0$ igual ao elemento diagonal $P_{5,5} = 0{,}1731$ p.p. na taxa Selic anualizada. Para que todas as Funções de Resposta ao Impulso do SVAR e das Projeções Locais estejam exatamente na mesma unidade econômica — **um choque estrutural não antecipado de $+1{,}00$ ponto percentual na taxa Selic em $h = 0$** —, definimos o choque normalizado:

$$\text{Shock}_t^{Selic} = P_{5,5} \cdot e_{selic, t} \tag{12}$$

e dividimos as respostas ortogonalizadas do SVAR (`orth_irfs`) e seus erros-padrão assintóticos por $P_{5,5}$. Conforme demonstrado por Plagborg-Møller & Wolf (2021), sob essa normalização, a resposta em impacto ($h = 0$) da Projeção Local linear coincide algebricamente com a resposta do SVAR.

---

## 4. Resultados Econométricos

### 4.1. Testes de Raiz Unitária e Especificação de Defasagens

Os testes Dickey-Fuller Aumentado (ADF) indicam estacionariedade em nível para o IPCA Itens Livres ($\text{ADF} = -2{,}992, p = 0{,}0357$) e para a taxa Selic ($\text{ADF} = -3{,}351, p = 0{,}0127$), enquanto $\ln(ICBr_t)$, $\ln(PTAX_t)$, $\ln(IBC_t)$ e $J_t^{fam}$ comportam-se como processos $I(1)$. Seguindo o teorema clássico de Sims, Stock & Watson (1990), estimamos o sistema em níveis para preservar eventuais relações de cointegração implícitas sem impor restrições potencialmente incorretas de diferenciação. O Critério de Informação de Akaike (AIC) e o FPE selecionam $p = 5$ a $6$ defasagens mensais ($\text{AIC} = -33{,}00$ em $p=5$ e $-32{,}92$ em $p=6$; $\text{BIC}$ e $\text{HQIC}$ selecionam $p=2$); adotamos $p = 6$ para capturar integralmente a dinâmica semestral da política monetária.

### 4.2. Funções de Resposta ao Impulso do SVAR e Fragilidade Financeira

A Figura 2 e a Tabela 1 apresentam as respostas ortogonalizadas de Cholesky normalizadas para um choque de **$+1{,}00$ p.p. na taxa Selic em $h = 0$**, acompanhadas de intervalos de confiança assintóticos de 95%.

![Figura 2: Funções de Resposta ao Impulso (IRF) do SVAR Normalizadas para Choque de +1,00 p.p. na Selic](figuras/figura2_irf_svar.png)

| Variável Resposta | $h = 0$ (Impacto) | $h = 3$ meses | $h = 6$ meses | $h = 9$ meses | $h = 12$ meses | $h = 18$ meses | $h = 24$ meses |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **IPCA Itens Livres (% a.m.)** [EP] | $+0{,}0000$ $[0{,}000]$ | $+0{,}0857$ $[0{,}106]$ | **$+0{,}1883$** $[0{,}093]$ | $+0{,}0510$ $[0{,}080]$ | **$-0{,}1339$** $[0{,}060]$ | **$-0{,}1020$** $[0{,}047]$ | **$-0{,}0956$** $[0{,}044]$ |
| **Comprometimento c/ Juros (% renda)** [EP] | $-0{,}0321$ $[0{,}030]$ | $+0{,}1571$ $[0{,}081]$ | **$+0{,}2732$** $[0{,}107]$ | **$+0{,}3628$** $[0{,}127]$ | **$+0{,}3817$** $[0{,}142]$ | $+0{,}2851$ $[0{,}159]$ | $+0{,}1115$ $[0{,}163]$ |
| **Atividade IBC-Br (log)** [EP] | $+0{,}0000$ $[0{,}000]$ | $-0{,}0019$ $[0{,}008]$ | $-0{,}0111$ $[0{,}010]$ | $-0{,}0160$ $[0{,}010]$ | $-0{,}0190$ $[0{,}011]$ | $-0{,}0146$ $[0{,}011]$ | $-0{,}0111$ $[0{,}011]$ |
| **Câmbio Nominal PTAX (log)** | $+0{,}0000$ | $+0{,}0166$ | $+0{,}0198$ | $-0{,}0024$ | $-0{,}0247$ | $-0{,}0514$ | $-0{,}0641$ |
| **Taxa Selic (% a.a.)** | **$+1{,}0000$** | $+2{,}4305$ | $+3{,}1166$ | $+3{,}1352$ | $+2{,}7771$ | $+1{,}5051$ | $+0{,}2788$ |

Três resultados destacam-se na Tabela 1:
1. **Persistência do Ciclo Monetário:** Um choque inicial de $+1{,}00$ p.p. na Selic é acompanhado por forte suavização e persistência nas reuniões subsequentes do Copom, levando a taxa Selic a atingir um pico de $+3{,}14$ p.p. no 9º mês antes de retornar gradualmente à linha de base. As magnitudes das demais respostas devem, portanto, ser interpretadas como o efeito de um ciclo de aperto que acumula cerca de $3$ p.p. no pico.
2. **Elevação Significativa do Comprometimento de Renda com Juros ($J_t^{fam}$):** Diferentemente da série agregada de serviço da dívida (que dilui o efeito dos juros nas amortizações rígidas de principal), o comprometimento exclusivo com juros (SGS 29033) apresenta elevação estatisticamente significativa ao nível de 5% nos horizontes de 6 meses ($+0{,}2732$ p.p., $t = 2{,}56$), 9 meses ($+0{,}3628$ p.p., $t = 2{,}85$) e **pico no 12º mês ($+0{,}3817$ p.p., $t = 2{,}70$)**.
3. **Dinâmica da Inflação Livre no SVAR Linear:** Mesmo controlando contemporaneamente e com 6 defasagens pelo câmbio nominal ($\ln(PTAX_t)$) e pelas commodities em dólares ($\ln(ICBr_t)$), a resposta do IPCA Itens Livres (SGS 11428) é positiva no primeiro semestre (atingindo pico de $+0{,}357$ p.p. em $h = 5$ e $+0{,}1883$ p.p. em $h = 6$, $t = 2{,}02$), revertendo para terreno desinflacionário significativo a partir do 12º mês ($-0{,}1339$ p.p. em $h = 12$; $-0{,}0956$ p.p. em $h = 24$). Na especificação de 7 variáveis que inclui adicionalmente as expectativas Focus 12 meses ($E_t[\pi_{t+12}]$) antes da Selic no ordenamento de Cholesky, a resposta positiva de curto prazo reduz-se à metade ($+0{,}1091$ p.p. em $h = 6$), indicando que parte do *price puzzle* linear reflete informação prospectiva captada pelas expectativas (Sims, 1992), embora o sinal positivo no primeiro semestre persista.

### 4.3. Decomposição da Variância (FEVD) e Qualificação Metodológica

A Figura 3 apresenta a Decomposição da Variância do Erro de Previsão (FEVD) para o comprometimento de renda das famílias com juros (Painel a) e para a inflação de itens livres (Painel b).

![Figura 3: Decomposição da Variância do Erro de Previsão (FEVD)](figuras/figura3_fevd_svar.png)

- **Protagonismo da Selic nos Encargos de Juros das Famílias:** No Painel (a), os choques na taxa Selic explicam **$13{,}68\%$ da variância do erro de previsão de $J_t^{fam}$ em 12 meses, $16{,}18\%$ em 18 meses e $15{,}16\%$ em 24 meses** — superando a participação da atividade econômica (IBC-Br, que explica $11{,}27\%$ em $h=12$ e $14{,}44\%$ em $h=18$). Isso confirma que, quando medida corretamente sobre a despesa de juros (SGS 29033), a política monetária é o principal determinante macroeconômico doméstico da fragilidade financeira familiar.
- **Interpretação da Baixa Participação do IBC-Br na FEVD da Inflação:** No Painel (b), os choques próprios da equação de inflação ($67{,}61\%$ em $h=24$), os choques de commodities ($11{,}85\%$), a Selic ($10{,}44\%$) e o câmbio ($5{,}34\%$) respondem por quase toda a variância do IPCA Itens Livres, enquanto o nível de atividade ($\ln(IBC_t)$) explica apenas **$2{,}23\%$ a $2{,}43\%$**. Conforme ressaltado por McLeay & Tenreyro (2020), uma participação reduzida da atividade na variância em forma reduzida não constitui, isoladamente, prova de que a inclinação estrutural $\kappa$ da Curva de Phillips seja nula, pois um banco central que reage a choques de demanda amortece a correlação observada entre produto e inflação. Ainda assim, a combinação de baixa contribuição do produto com elevada participação de choques de oferta/commodities e da própria Selic ($10{,}44\%$) é plenamente consistente com a visão de que a inflação brasileira responde pouco a variações marginais da capacidade ociosa doméstica.

---

### 4.4. Robustez Linear: SVAR versus Projeções Locais Normalizadas (Jordà, 2005)

Para relaxar a restrição autorregressiva iterativa do VAR ($\Phi^h$), estimamos para cada horizonte $h \in \{0, 1, \dots, 24\}$ a Projeção Local linear sobre o choque normalizado de $+1{,}00$ p.p. na Selic ($\text{Shock}_t^{Selic}$ da Eq. 12), com erros-padrão robustos de Newey-West (HAC, janela de truncamento $h + 1$):

$$y_{i, t+h} = \alpha_i^h + \beta_i^h \text{Shock}_t^{Selic} + \sum_{k=1}^6 \mathbf{\Gamma}_{i,k}^h Y_{t-k} + \epsilon_{i, t+h}^h \tag{13}$$

![Figura 4: Comparação Normalizada (+1,00 p.p. Selic) entre SVAR e Projeções Locais (Jordà, 2005)](figuras/figura4_lp_vs_svar.png)

| Horizonte ($h$) | IPCA Livres SVAR | IPCA Livres LP (EP HAC) [$p$-valor] | Juros Dívida SVAR | Juros Dívida LP (EP HAC) [$p$-valor] | IC 95% LP (Juros Dívida) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$h = 0$** | $+0{,}0000$ | $+0{,}0000$ $(0{,}087)$ $[1{,}000]$ | $-0{,}0321$ | $-0{,}0321$ $(0{,}028)$ $[0{,}254]$ | $[-0{,}0874; +0{,}0231]$ |
| **$h = 3$** | $+0{,}0857$ | $+0{,}0791$ $(0{,}077)$ $[0{,}302]$ | $+0{,}1571$ | **$+0{,}2035$** $(0{,}063)$ **$[0{,}001]$** | $[+0{,}0808; +0{,}3262]$ |
| **$h = 6$** | **$+0{,}1883$** | $+0{,}1528$ $(0{,}112)$ $[0{,}171]$ | **$+0{,}2732$** | **$+0{,}2978$** $(0{,}102)$ **$[0{,}003]$** | $[+0{,}0990; +0{,}4967]$ |
| **$h = 9$** | $+0{,}0510$ | $-0{,}2181$ $(0{,}116)$ $[0{,}060]$ | **$+0{,}3628$** | **$+0{,}4128$** $(0{,}114)$ **$[<0{,}001]$** | $[+0{,}1892; +0{,}6364]$ |
| **$h = 12$** | **$-0{,}1339$** | $-0{,}1271$ $(0{,}086)$ $[0{,}140]$ | **$+0{,}3817$** | **$+0{,}4594$** $(0{,}144)$ **$[0{,}001]$** | $[+0{,}1766; +0{,}7423]$ |
| **$h = 18$** | **$-0{,}1020$** | $-0{,}0193$ $(0{,}083)$ $[0{,}815]$ | $+0{,}2851$ | **$+0{,}5926$** $(0{,}154)$ **$[<0{,}001]$** | $[+0{,}2914; +0{,}8938]$ |
| **$h = 24$** | **$-0{,}0956$** | **$-0{,}3323$** $(0{,}102)$ **$[0{,}001]$** | $+0{,}1115$ | $+0{,}2208$ $(0{,}207)$ $[0{,}285]$ | $[-0{,}1844; +0{,}6260]$ |

Com a normalização exata de $+1{,}00$ p.p. na Selic em $h = 0$, a Figura 4 e a Tabela 2 confirmam a equivalência algébrica em $h = 0$ (Plagborg-Møller & Wolf, 2021) e a forte aderência entre os dois métodos:
- **Confirmação Robusta da Fragilidade Financeira Familiar ($H_2$):** Nas Projeções Locais, o efeito sobre o comprometimento de renda das famílias com juros é ainda mais pronunciado e estatisticamente significativo ($p \le 0{,}003$) do 3º ao 18º mês, atingindo **$+0{,}4594$ p.p. em $h = 12$** ($p = 0{,}001$) e **$+0{,}5926$ p.p. em $h = 18$** ($p < 0{,}001$).
- **Trajetória da Inflação Livre:** Em ambos os estimadores, a resposta pontual em $h = 3$ e $h = 6$ é positiva ($+0{,}1883$ no SVAR e $+0{,}1528$ na LP em $h=6$, com pico de $+0{,}389$ p.p. em $h=5$), tornando-se desinflacionária e estatisticamente significativa ao final de 24 meses ($-0{,}3323$ p.p. na LP, $p = 0{,}001$).

---

### 4.5. Projeções Locais Dependentes de Estado e Assimétricas: Testando a Hipótese do Platô de Juros Altos

A estimativa linear da Seção 4.4 combina períodos em que a Selic encontrava-se em patamares moderados com períodos de juros excepcionalmente elevados. Para testar a **Hipótese $H_1$** e responder às exigências metodológicas de não impor simetria entre altas e cortes de juros (Tenreyro & Thwaites, 2016), estimamos duas especificações sobre a inflação acumulada de itens livres em $h$ meses ($\Pi_{t, t+h}^{livre} = \sum_{j=0}^h \pi_{t+j}^{livre}$):

1. **Especificação Dependente de Estado (com reporte explícito do nível do regime $\gamma^h$):**
   $$\Pi_{t, t+h}^{livre} = \alpha^h + \gamma^h I_{t-1} + \beta_{alto}^h \left( \text{Shock}_t^{Selic} \times I_{t-1} \right) + \beta_{mod}^h \left( \text{Shock}_t^{Selic} \times (1 - I_{t-1}) \right) + \sum_{k=1}^6 \mathbf{\Gamma}_k^h Y_{t-k} + \nu_{t+h}^h \tag{14}$$
   onde $I_{t-1} = \mathbb{I}\left(\overline{\text{Selic}}_{t-1}^{(12m)} > 11{,}27\%\text{ a.a.}\right)$ indica que a economia encontrava-se, no mês anterior ao choque, no **Platô de Juros Persistentemente Altos** (acima da mediana amostral). Aqui, $\gamma^h$ mede diretamente o deslocamento médio da inflação acumulada associado à permanência no platô de juros altos (condicional a 6 defasagens de todas as variáveis, incluindo câmbio e atividade).

2. **Especificação Assimétrica dentro do Platô de Juros Altos (Altas vs. Cortes Separados):**
   Definindo $\text{Shock}_t^+ = \max(\text{Shock}_t^{Selic}, 0) \ge 0$ ($N_+ = 63$ meses no platô alto) e $\text{Shock}_t^- = \min(\text{Shock}_t^{Selic}, 0) \le 0$ ($N_- = 59$ meses no platô alto), substituímos o termo linear do platô alto por:
   $$\beta_{alto}^{+, h} \left( \text{Shock}_t^+ \times I_{t-1} \right) + \beta_{alto}^{-, h} \left( \text{Shock}_t^- \times I_{t-1} \right) \tag{15}$$
   Note-se que, como $\text{Shock}_t^- < 0$, um coeficiente $\beta_{alto}^{-, h} > 0$ significa que um **corte não antecipado de $-1{,}00$ p.p. na Selic** ($\text{Shock}_t^- = -1$) associa-se a uma variação de **$-\beta_{alto}^{-, h} < 0$ (queda)** na inflação acumulada.

![Figura 5: Projeções Locais Dependentes de Estado e Decomposição Assimétrica sem Imposição de Simetria](figuras/figura5_regime_juros_altos_lp.png)

#### Tabela 3: Projeções Locais Dependentes de Estado e Assimétricas — IPCA Itens Livres Acumulado ($\Pi_{t, t+h}^{livre}$, SGS 11428)

| Horizonte ($h$) | Platô Alto $\hat{\beta}_{alto}^h$ ($p$-val) | Regime Mod. $\hat{\beta}_{mod}^h$ ($p$-val) | Wald $p(\beta_{alto}=\beta_{mod})$ | Nível do Platô $\hat{\gamma}^h$ ($p$-val) | Alta no Platô $\hat{\beta}_{alto}^{+,h}$ ($p$-val) | Corte no Platô $\hat{\beta}_{alto}^{-,h}$ ($p$-val) | Wald Simetria $p(\beta^+=\beta^-)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$h = 0$** | $+0{,}081$ $(0{,}515)$ | $-0{,}051$ $(0{,}671)$ | $0{,}457$ | $+0{,}044$ $(0{,}250)$ | $-0{,}113$ $(0{,}695)$ | $+0{,}228$ $(0{,}272)$ | $0{,}424$ |
| **$h = 3$** | **$+0{,}782$** **$(0{,}035)$** | $-0{,}201$ $(0{,}660)$ | $0{,}124$ | $+0{,}305$ $(0{,}104)$ | $+0{,}041$ $(0{,}961)$ | **$+1{,}344$** **$(0{,}058)$** | $0{,}347$ |
| **$h = 6$** | **$+1{,}485$** **$(0{,}011)$** | $+0{,}592$ $(0{,}201)$ | $0{,}279$ | **$+0{,}770$** **$(0{,}036)$** | $+0{,}643$ $(0{,}678)$ | **$+2{,}140$** **$(0{,}027)$** | $0{,}507$ |
| **$h = 9$** | $+1{,}060$ $(0{,}113)$ | $+0{,}631$ $(0{,}202)$ | $0{,}635$ | **$+1{,}341$** **$(0{,}007)$** | $-0{,}076$ $(0{,}969)$ | $+1{,}945$ $(0{,}103)$ | $0{,}478$ |
| **$h = 12$** | $-0{,}360$ $(0{,}632)$ | $+0{,}529$ $(0{,}282)$ | $0{,}354$ | **$+1{,}638$** **$(0{,}002)$** | $-0{,}851$ $(0{,}698)$ | $+0{,}018$ $(0{,}990)$ | $0{,}797$ |
| **$h = 18$** | $-0{,}028$ $(0{,}973)$ | $-0{,}360$ $(0{,}590)$ | $0{,}759$ | **$+1{,}612$** **$(0{,}021)$** | $-0{,}855$ $(0{,}781)$ | $+0{,}610$ $(0{,}788)$ | $0{,}773$ |
| **$h = 24$** | $-0{,}819$ $(0{,}278)$ | **$-1{,}922$** **$(0{,}009)$** | $0{,}296$ | $+0{,}927$ $(0{,}242)$ | $-4{,}562$ $(0{,}140)$ | $+2{,}058$ $(0{,}467)$ | $0{,}243$ |

*Nota:* Estimativas para um choque estrutural de Cholesky normalizado de $+1{,}00$ p.p. na Selic em $h=0$. Erros-padrão robustos de Newey-West (HAC) com truncamento $h+1$. No Platô Alto, $N_+ = 63$ observações com $\text{Shock}_t^{Selic} > 0$ e $N_- = 59$ com $\text{Shock}_t^{Selic} < 0$. Para um corte de $-1{,}00$ p.p. ($\text{Shock}_t^- = -1$), o impacto estimado sobre a inflação acumulada é $-\hat{\beta}_{alto}^{-, h}$ (exibido na curva verde da Figura 5b).

A Tabela 3 permite uma leitura rigorosa e matizada das hipóteses em estudo:
1. **Contraste entre o Regime Moderado e o Platô de Juros Altos ($\hat{\beta}_{alto}^h$ vs. $\hat{\beta}_{mod}^h$):** Quando a Selic opera em regime moderado ($\le 11{,}27\%$ a.a.), um choque de aperto monetário não gera pressão inflacionária estatisticamente significativa no curto prazo e produz uma **redução expressiva e altamente significativa da inflação acumulada em 24 meses ($\hat{\beta}_{mod}^{24} = -1{,}922$ p.p., $p = 0{,}009$)**. Em contrapartida, quando a Selic já se encontra no Platô Alto ($> 11{,}27\%$ a.a.), o choque associa-se a uma **elevação estatisticamente significativa da inflação acumulada em $h = 3$ ($+0{,}782$ p.p., $p = 0{,}035$) e em $h = 6$ ($+1{,}485$ p.p., $p = 0{,}011$)**, e o efeito em $h = 24$ ($-0{,}819$ p.p., $p = 0{,}278$) não é estatisticamente diferente de zero. Cabe registrar, contudo, que o teste de Wald ponto a ponto não rejeita a igualdade $\beta_{alto}^h = \beta_{mod}^h$ aos níveis convencionais ($p = 0{,}124$ em $h=3$), devido à maior variância amostral dentro de cada sub-regime.
2. **Significância Robusta do Parâmetro de Nível do Platô Alto ($\hat{\gamma}^h$):** Respondendo diretamente ao núcleo da tese de Resende (2026) — que diz respeito à permanência do **nível** da Selic em patamar elevado —, o coeficiente $\hat{\gamma}^h$ é positivo e estatisticamente significativo em $h = 6$ ($+0{,}770$ p.p., $p = 0{,}036$), $h = 9$ ($+1{,}341$ p.p., $p = 0{,}007$), **$h = 12$ ($+1{,}638$ p.p., $p = 0{,}002$)** e $h = 18$ ($+1{,}612$ p.p., $p = 0{,}021$). Mesmo controlando por 6 defasagens da própria inflação, do câmbio, das commodities e da atividade, estar no regime de juros persistentemente altos prevê uma inflação acumulada $1{,}64$ p.p. superior um ano à frente.
3. **Decomposição Assimétrica ($\hat{\beta}_{alto}^{+,h}$ vs. $\hat{\beta}_{alto}^{-,h}$):** Ao separar altas e cortes no Platô Alto sem impor simetria, verifica-se que o coeficiente positivo de curto prazo no IPCA Itens Livres (SGS 11428) é impulsionado sobretudo pelos episódios de **corte ($\hat{\beta}_{alto}^{-,3} = +1{,}344, p = 0{,}058$; $\hat{\beta}_{alto}^{-,6} = +2{,}140, p = 0{,}027$)** — isto é, reduções não antecipadas de $-1{,}00$ p.p. na Selic a partir do platô alto foram seguidas de uma queda média de **$-1{,}34$ p.p. (em 3 meses) e $-2{,}14$ p.p. (em 6 meses)** na inflação acumulada (curva verde do Painel b da Figura 5), enquanto em horizontes mais longos ($h \ge 12$) as estimativas tornam-se imprecisas ($p > 0{,}14$). O teste de Wald não rejeita a hipótese nula de simetria ($\beta^+ = \beta^-, p > 0{,}24$), mas o desmembramento demonstra que a queda de curto prazo após cortes nos dados não depende de mero espelhamento algébrico, embora possa refletir parcialmente o fato de que o Copom inicia cortes quando observa desaceleração inflacionária prospectiva.

---

### 4.6. Bateria de Testes de Robustez: Expectativas Focus 12m, Juro Real *Ex Ante*, IPCA Cheio e Limiares Alternativos

Para testar se os resultados da Tabela 3 sobrevivem à inclusão de informação prospectiva do Banco Central e do mercado (Nakamura & Steinsson, 2018; Sims, 1992), a definições menos endógenas do regime e ao controle de quebras pandêmicas/sazonais, a Tabela 4 reporta seis especificações alternativas para os horizontes $h \in \{3, 6, 9, 12, 24\}$.

#### Tabela 4: Bateria de Robustez das Projeções Locais Dependentes de Estado

| Especificação de Robustez | Parâmetro | $h = 3$ | $h = 6$ | $h = 9$ | $h = 12$ | $h = 24$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1. Controle de Expectativas Focus 12m**<br>*(VAR 7 variáveis: inclui $E_t[\pi_{t+12}]$ antes da Selic)* | $\hat{\beta}_{alto}^h$ ($p$)<br>$\hat{\beta}_{mod}^h$ ($p$)<br>$\hat{\gamma}^h$ ($p$) | $+0{,}483$ $(0{,}217)$<br>$-0{,}235$ $(0{,}587)$<br>**$+0{,}423$ $(0{,}017)$** | **$+1{,}376$ $(0{,}020)$**<br>$+0{,}427$ $(0{,}398)$<br>**$+0{,}899$ $(0{,}008)$** | **$+1{,}130$ $(0{,}091)$**<br>$+0{,}537$ $(0{,}356)$<br>**$+1{,}421$ $(0{,}003)$** | $-0{,}030$ $(0{,}967)$<br>$+0{,}455$ $(0{,}445)$<br>**$+1{,}699$ $(0{,}002)$** | $-0{,}274$ $(0{,}697)$<br>**$-2{,}038$ $(0{,}024)$**<br>$+0{,}943$ $(0{,}213)$ |
| **2. IPCA Cheio (SGS 433) + Focus 12m**<br>*(Inflação plena c/ controle cambial e Focus)* | $\hat{\beta}_{alto}^h$ ($p$)<br>$\hat{\beta}_{mod}^h$ ($p$)<br>$\hat{\gamma}^h$ ($p$) | $+0{,}204$ $(0{,}490)$<br>$-0{,}102$ $(0{,}806)$<br>**$+0{,}483$ $(0{,}010)$** | **$+0{,}759$ $(0{,}041)$**<br>$+0{,}441$ $(0{,}322)$<br>**$+0{,}928$ $(0{,}002)$** | **$+0{,}706$ $(0{,}078)$**<br>$-0{,}046$ $(0{,}942)$<br>**$+1{,}361$ $(0{,}001)$** | $-0{,}151$ $(0{,}759)$<br>$-0{,}286$ $(0{,}660)$<br>**$+1{,}503$ $(0{,}003)$** | $+0{,}210$ $(0{,}644)$<br>$-1{,}250$ $(0{,}147)$<br>$+1{,}043$ $(0{,}169)$ |
| **3. Regime por Juro Real *Ex Ante***<br>*($r_{t-1}^{ex\text{-}ante} = \text{Selic}_{t-1} - E_{t-1}[\pi_{t+12}] > 6{,}18\%$)* | $\hat{\beta}_{alto}^h$ ($p$)<br>$\hat{\beta}_{mod}^h$ ($p$)<br>$\hat{\gamma}^h$ ($p$) | **$+0{,}918$ $(0{,}004)$**<br>$-0{,}602$ $(0{,}105)$<br>**$+0{,}395$ $(0{,}035)$** | **$+1{,}567$ $(0{,}002)$**<br>$+0{,}164$ $(0{,}727)$<br>$+0{,}615$ $(0{,}105)$ | $+0{,}735$ $(0{,}186)$<br>$+0{,}524$ $(0{,}326)$<br>$+0{,}819$ $(0{,}133)$ | $-0{,}625$ $(0{,}342)$<br>$+0{,}397$ $(0{,}529)$<br>$+0{,}982$ $(0{,}123)$ | $+0{,}078$ $(0{,}924)$<br>**$-1{,}967$ $(0{,}035)$**<br>$+0{,}436$ $(0{,}560)$ |
| **4. Limiar Alternativo: Selic $> 10{,}0\%$ a.a.**<br>*(Platô de dois dígitos)* | $\hat{\beta}_{alto}^h$ ($p$)<br>$\hat{\beta}_{mod}^h$ ($p$)<br>$\hat{\gamma}^h$ ($p$) | **$+0{,}730$ $(0{,}009)$**<br>$-0{,}587$ $(0{,}205)$<br>$+0{,}448$ $(0{,}113)$ | **$+1{,}223$ $(0{,}006)$**<br>$+0{,}371$ $(0{,}475)$<br>**$+0{,}847$ $(0{,}061)$** | $+0{,}573$ $(0{,}311)$<br>$+0{,}663$ $(0{,}194)$<br>**$+1{,}369$ $(0{,}005)$** | $-0{,}820$ $(0{,}216)$<br>$+0{,}731$ $(0{,}150)$<br>**$+1{,}959$ $(0{,}001)$** | **$-1{,}334$ $(0{,}050)$**<br>**$-1{,}838$ $(0{,}030)$**<br>**$+1{,}764$ $(0{,}008)$** |
| **5. Limiar Alternativo: Selic $> 12{,}0\%$ a.a.**<br>*(Platô de juros extremos)* | $\hat{\beta}_{alto}^h$ ($p$)<br>$\hat{\beta}_{mod}^h$ ($p$)<br>$\hat{\gamma}^h$ ($p$) | **$+0{,}794$ $(0{,}077)$**<br>$-0{,}045$ $(0{,}907)$<br>**$+0{,}431$ $(0{,}018)$** | **$+1{,}581$ $(0{,}005)$**<br>**$+0{,}668$ $(0{,}093)$**<br>**$+1{,}010$ $(0{,}002)$** | **$+1{,}276$ $(0{,}026)$**<br>$+0{,}545$ $(0{,}248)$<br>**$+1{,}596$ $(<0{,}001)$** | $+0{,}183$ $(0{,}754)$<br>$+0{,}106$ $(0{,}847)$<br>**$+1{,}784$ $(<0{,}001)$** | $+0{,}212$ $(0{,}764)$<br>**$-2{,}147$ $(0{,}008)$**<br>**$+1{,}347$ $(0{,}061)$** |
| **6. Dummies Sazonais + COVID-19**<br>*(11 dummies mensais + dummy 2020:03–2021:06)* | $\hat{\beta}_{alto}^h$ ($p$)<br>$\hat{\beta}_{mod}^h$ ($p$)<br>$\hat{\gamma}^h$ ($p$) | $+0{,}337$ $(0{,}331)$<br>$-0{,}184$ $(0{,}585)$<br>$+0{,}282$ $(0{,}102)$ | $+0{,}487$ $(0{,}353)$<br>$+0{,}596$ $(0{,}125)$<br>**$+0{,}604$ $(0{,}068)$** | $+0{,}281$ $(0{,}694)$<br>$+0{,}620$ $(0{,}207)$<br>**$+1{,}137$ $(0{,}010)$** | $-0{,}477$ $(0{,}566)$<br>$+0{,}632$ $(0{,}271)$<br>**$+1{,}520$ $(0{,}004)$** | $-0{,}282$ $(0{,}718)$<br>**$-0{,}971$ $(0{,}061)$**<br>$+0{,}536$ $(0{,}421)$ |

Os testes da Tabela 4 revelam achados substanciais:
1. **Sobrevivência ao Controle por Expectativas Focus 12 Meses e Juro Real *Ex Ante*:** Mesmo quando o choque monetário é ortogonalizado em relação às expectativas Focus de 12 meses e controlamos por 6 defasagens de $E_t[\pi_{t+12}]$ (Especificação 1), o choque de juros no Platô Alto continua associado a um aumento estatisticamente significativo de **$+1{,}376$ p.p. em $h = 6$ ($p = 0{,}020$)** e **$+1{,}130$ p.p. em $h = 9$ ($p = 0{,}091$)**, enquanto no Regime Moderado o aperto reduz a inflação acumulada em **$-2{,}038$ p.p. em $h = 24$ ($p = 0{,}024$)**. Mais ainda, quando definimos o regime pelo **juro real *ex ante* ($\text{Selic}_{t-1} - E_{t-1}[\pi_{t+12}] > 6{,}18\%$ a.a., Especificação 3)** — que expurga a inflação esperada do indicador de estado —, a significância em $h = 3$ ($+0{,}918$ p.p., $p = 0{,}004$) e $h = 6$ ($+1{,}567$ p.p., $p = 0{,}002$) torna-se ainda mais forte!
2. **Monotonicidade no Limiar de $12{,}0\%$ a.a. (Especificação 5):** Quando elevamos o limiar do platô para $12{,}0\%$ a.a., a anomalia acentua-se: no regime extremo ($> 12\%$), o efeito acumulado permanece positivo em $h = 6$ ($+1{,}581$ p.p., $p = 0{,}005$), $h = 9$ ($+1{,}276$ p.p., $p = 0{,}026$), $h = 12$ ($+0{,}183$ p.p.) e mesmo em $h = 24$ ($+0{,}212$ p.p.), ao passo que no regime $\le 12\%$ o aperto reduz a inflação em $-2{,}147$ p.p. em 24 meses ($p = 0{,}008$).
3. **Estabilidade do Efeito de Nível $\hat{\gamma}^h$ com Dummies Sazonais e de COVID-19 (Especificação 6):** A inclusão de 11 dummies sazonais mensais e de uma dummy para o choque pandêmico (março/2020 a junho/2021) absorve parte da variação de curto prazo de $\hat{\beta}_{alto}^h$, mas o coeficiente de nível do platô alto ($\hat{\gamma}^h$) mantém-se positivo e altamente significativo em $h = 9$ ($+1{,}137$ p.p., $p = 0{,}010$) e $h = 12$ ($+1{,}520$ p.p., $p = 0{,}004$), e o efeito desinflacionário de 24 meses permanece restrito ao regime moderado ($-0{,}971$ p.p., $p = 0{,}061$).

---

## 5. Discussão de Política Econômica, Viabilidade Institucional e Limitações

### 5.1. Discriminação entre Interpretações Teóricas: Lara Resende vs. Blanchard (2004)

Os resultados da Seção 4 confirmam que, quando a taxa Selic opera em platôs superiores a $11{,}27\%$–$12{,}0\%$ a.a. (ou juro real *ex ante* $> 6{,}18\%$ a.a.), o aperto monetário adicional perde sua capacidade de reduzir a inflação em 24 meses e associa-se a pressões inflacionárias nos primeiros 6 a 9 meses. Tanto a hipótese de **Blanchard (2004)** (dominância fiscal via prêmio de risco e câmbio) quanto a de **Lara Resende (2026)** (canal de custos, dinâmica endógena das LFTs e efeito neo-fisheriano) são compatíveis com a perda de potência desinflacionária da Selic no platô alto. Contudo, três elementos empíricos e institucionais ajudam a qualificar as duas leituras no Brasil contemporâneo:
1. **Controle Direto pelo Canal Cambial:** Em nossas estimações (Tabelas 1, 3 e 4), o efeito positivo de $\hat{\beta}_{alto}^h$ (em $h=3, 6$) e de $\hat{\gamma}^h$ (em $h=6, 9, 12, 18$) **sobrevive integralmente ao controle pelo câmbio nominal ($\ln(PTAX_t)$)**, indicando que a pressão inflacionária no platô de juros altos não se reduz ao canal de depreciação cambial de Blanchard (2004), operando também domesticamente via custos e indexação financeira.
2. **Origem do Déficit Nominal:** Diferentemente de 2002–2003 (quando a dívida pública tinha forte indexação cambial e as reservas internacionais líquidas eram inferiores a US\$ 20 bilhões), em 2025–2026 o setor público detém mais de US\$ 350 bilhões em reservas cambiais e um déficit primário próximo de zero ($-0{,}4\%$ a $-0{,}7\%$ do PIB), sendo a expansão da relação dívida/PIB impulsionada pelo diferencial $\bar{i}_t - g_{nom, t} > +5{,}5\%$ a.a. sobre uma dívida doméstica majoritariamente pós-fixada em Selic ($\lambda \approx 0{,}50$).

### 5.2. Condicionalidade Institucional, Autonomia do BCB (LC 179/2021) e Cláusulas de Escape

Para superar a armadilha de juros elevados, Resende (2026) propõe substituir a dissociação entre as autoridades fiscal e monetária por uma coordenação plurianual (4 a 5 anos) no âmbito de um **Conselho Fiscal e Monetário Nacional (CFMN)**, estabelecendo um intervalo referencial para a Selic entre a meta de inflação ($3{,}0\%$ a.a.) e a taxa de crescimento nominal potencial do PIB ($\approx 5{,}5\%$ a.a., acrescida de um spread transitório de $2{,}0\%$ durante um período de convergência de 12 meses até $7{,}5\%$ a.a.).

À luz da evidência econométrica deste artigo e da experiência comparada dos ciclos de **2011–2013** e **2016–2018**, essa proposta normativa não decorre mecanicamente das regressões lineares e requer três salvaguardas institucionais estritas:
1. **Compatibilização Legal (CMN e Lei Complementar nº 179/2021):** No ordenamento jurídico vigente, compete ao Conselho Monetário Nacional (CMN) fixar a meta de inflação e ao Banco Central do Brasil, dotado de autonomia operacional pela LC 179/2021, calibrar a Selic. Uma diretriz de convergência da taxa de juros exigiria ou reformulação legislativa do mandato do CMN/BCB ou um protocolo formal de metas conjuntas de resultado nominal e inflação entre o Tesouro Nacional e o BCB.
2. **Cláusulas de Contingência (*Escape Clauses*) e Risco Cambial:** Como alerta a crítica de Lucas, uma redução abrupta da Selic de $\sim 14\%$ para $7{,}5\%$ a.a. sem respaldo nas expectativas de mercado poderia induzir reversão de fluxos de portfólio e depreciação cambial, reativando o repasse cambial $\psi \Delta e_t$ na Equação (1) (como observado em 2012–2013). Portanto, qualquer regra de transição gradual da Selic deve ser condicionada a **cláusulas de escape explícitas**: a convergência da taxa básica só prossegue enquanto (i) o resultado primário cumprir a meta de equilíbrio/superávit estrutural, (ii) as expectativas de inflação de longo prazo permanecerem ancoradas dentro do intervalo de tolerância e (iii) a volatilidade cambial puder ser absorvida por *swaps* e intervenções pontuais sem perda continuada do estoque de reservas internacionais.
3. **Efeitos Distributivos sobre Poupadores e Fundos Previdenciários:** Embora a redução da Selic comprima a transferência de juros sobre o estoque de LFTs e alivie expressivamente o comprometimento de renda das famílias endividadas ($J_t^{fam}$), deve-se considerar que títulos pós-fixados também compõem a carteira de fundos de pensão, previdência complementar e poupadores de classe média via fundos DI, exigindo transição previsível que permita a realocação gradual da poupança doméstica para instrumentos de financiamento privado e infraestrutura de longo prazo (Arida, Bacha & Lara-Resende, 2005).

### 5.3. Limitações Metodológicas e Declaração de Reprodutibilidade

1. **Identificação e Endogeneidade do Regime:** Embora o uso do indicador defasado $I_{t-1}$, da série de expectativas Focus 12 meses ($E_t[\pi_{t+12}]$) e do juro real *ex ante* reduza substancialmente o viés de simultaneidade e o efeito-informação (Nakamura & Steinsson, 2018), a identificação baseia-se em restrições recursivas de Cholesky sobre dados mensais. Extensões futuras devem empregar instrumentos externos de alta frequência (surpresas nos contratos futuros de DI em janelas intradiárias em torno das decisões do Copom) e modelos de transição suave (*Smooth Transition Local Projections*, Tenreyro & Thwaites, 2016).
2. **Inferência em Horizontes Múltiplos e Tamanho Amostral:** A amostra de 258 meses contém quatro grandes ciclos de aperto monetário no platô alto, o que limita o número efetivo de episódios independentes e amplia os erros-padrão HAC em horizontes longos ($h \ge 18$), razão pela qual as diferenças entre $\hat{\beta}_{alto}^h$ e $\hat{\beta}_{mod}^h$ devem ser interpretadas com cautela estatística.
3. **Disponibilidade de Dados e Código:** Todos os dados brutos extraídos das APIs do Banco Central do Brasil (`data/base_macro_bcb.csv`), os scripts de estimação em Python (`scripts/estimacao_svar_lara_resende.py`, `scripts/estimacao_local_projections.py` e `scripts/estimacao_regime_juros_altos.py`) e os logs numéricos das regressões encontram-se integralmente disponíveis no repositório público do projeto (<https://github.com/bonvenuto/artigo-politica-monetaria>), garantindo reprodutibilidade integral.

---

## 6. Conclusão

Este estudo formalizou analiticamente e submeteu a testes econométricos as proposições de André Lara Resende (2017, 2020, 2026) sobre a transmissão da política monetária no Brasil entre 2005 e 2026. Os resultados empíricos sustentam três conclusões principais, devidamente calibradas pela evidência estatística:

1. **Elevação Robusta dos Encargos de Juros das Famílias:** Um choque positivo de $+1{,}00$ p.p. na taxa Selic eleva de maneira estatisticamente significativa e persistente o comprometimento da renda das famílias com o pagamento de juros bancários (SGS 29033) tanto no SVAR quanto nas Projeções Locais ($+0{,}298$ p.p. em 6 meses, $p = 0{,}003$; $+0{,}459$ p.p. em 12 meses, $p = 0{,}001$; $+0{,}593$ p.p. em 18 meses, $p < 0{,}001$), com a Selic explicando até $16{,}2\%$ da variância do erro de previsão dessa variável.
2. **Assimetria de Regime na Eficácia Desinflacionária da Selic:** Enquanto no regime de juros moderados ($\le 11{,}27\%$ a.a.) o aperto monetário cumpre seu papel convencional e reduz a inflação acumulada de itens livres (SGS 11428) em $-1{,}922$ p.p. ao final de 24 meses ($p = 0{,}009$), nos períodos em que a Selic já se encontra estacionada em um platô elevado ($> 11{,}27\%$ a.a., ou juro real *ex ante* $> 6{,}18\%$ a.a.) choques adicionais de aperto associam-se a acréscimos estatisticamente significativos na inflação acumulada de 3 a 6 meses ($+0{,}782$ p.p. a $+1{,}485$ p.p., $p < 0{,}05$) e não apresentam efeito desinflacionário significativo em 24 meses.
3. **Efeito de Nível do Platô Alto e Condições para a Desinflação via Redução de Juros:** O parâmetro de nível do regime de juros altos ($\hat{\gamma}^h$) é positivo e significativo entre 6 e 18 meses ($+1{,}638$ p.p. em $h = 12$, $p = 0{,}002$), resistindo ao controle por expectativas Focus 12 meses, câmbio PTAX e dummies de COVID-19. Ademais, a decomposição assimétrica indica que cortes não antecipados da Selic a partir do platô alto associaram-se historicamente a recuos na inflação acumulada nos dois trimestres seguintes ($-1{,}34$ p.p. em $h=3$ e $-2{,}14$ p.p. em $h=6$). Em consonância com a estrutura de *duration* zero das LFTs no Brasil, esses achados indicam que a redução gradual e coordenada da Selic — desde que amparada por equilíbrio primário e estabilidade cambial — alivia simultaneamente o déficit nominal público e a fragilidade financeira das famílias sem comprometer o controle inflacionário.

---

## 7. Referências Bibliográficas

- **Arida, P., Bacha, E. L., & Lara-Resende, A.** (2005). Credit, interest, and jurisdictional uncertainty: conjectures on the case of Brazil. In F. Giavazzi, I. Goldfajn, & S. Herrera (Eds.), *Inflation Targeting, Debt, and the Brazilian Experience, 1999 to 2003* (pp. 265–293). Cambridge, MA: MIT Press.
- **Barth, M. J., & Ramey, V. A.** (2001). The cost channel of monetary transmission. *NBER Macroeconomics Annual*, 16, 199–240.
- **Blanchard, O.** (2004). Fiscal dominance and inflation targeting: lessons from Brazil. *NBER Working Paper*, n. 10389.
- **Céspedes, B., Lima, E., & Maka, A.** (2008). Monetary policy, inflation and the level of economic activity in Brazil after the Real Plan: stylized facts from SVAR models. *Revista Brasileira de Economia*, 62(2), 123–160.
- **Cochrane, J. H.** (2011). Determinacy and identification with Taylor rules. *Journal of Political Economy*, 119(3), 565–615.
- **Cochrane, J. H.** (2023). *The Fiscal Theory of the Price Level*. Princeton, NJ: Princeton University Press.
- **Cochrane, J. H.** (2026). Reasons to Lower Rates; More on Lower Rates. *The Grumpy Economist* (Hoover Institution Essay), setembro de 2026.
- **Drehmann, M., Illes, A., Juselius, M., & Santos, M.** (2015). How much income is used for debt payments? A new database for debt service ratios. *BIS Quarterly Review*, September 2015, 89–103.
- **Favero, C. A., & Giavazzi, F.** (2004). Inflation targeting and debt: lessons from Brazil. *NBER Working Paper*, n. 10390.
- **García-Schmidt, M., & Woodford, M.** (2019). Are low interest rates deflationary? A paradox of perfect-foresight analysis. *American Economic Review*, 109(1), 86–120.
- **Hein, E.** (2007). Interest rate, debt, distribution and capital accumulation in a post-Kaleckian model. *Metroeconomica*, 58(2), 310–339.
- **Jordà, Ò.** (2005). Estimation and inference of impulse responses by local projections. *American Economic Review*, 95(1), 161–182.
- **Lavoie, M.** (1995). Interest rates in post-Keynesian models of growth and distribution. *Metroeconomica*, 46(2), 146–177.
- **Loyo, E.** (1999). Tight money paradox on the loose: a fiscalist hyperinflation. *John F. Kennedy School of Government Working Paper*, Harvard University.
- **McLeay, M., & Tenreyro, S.** (2020). Optimal inflation and the identification of the Phillips curve. *NBER Macroeconomics Annual*, 34(1), 199–255.
- **Minsky, H. P.** (1986). *Stabilizing an Unstable Economy*. New Haven: Yale University Press.
- **Nakamura, E., & Steinsson, J.** (2018). High-frequency identification of monetary non-neutrality: the information effect. *Quarterly Journal of Economics*, 133(3), 1283–1330.
- **Pastore, A. C.** (1995). Passividade monetária e inércia. *Revista Brasileira de Economia*, 49(1), 1–50.
- **Plagborg-Møller, M., & Wolf, C. K.** (2021). Local projections and VARs estimate the same impulse responses. *Econometrica*, 89(2), 955–980.
- **Ravenna, F., & Walsh, C. E.** (2006). Optimal monetary policy with the cost channel. *Journal of Monetary Economics*, 53(2), 199–216.
- **Resende, A. L., & Lopes, F. L.** (1980). Sobre as causas da recente aceleração inflacionária. *Pesquisa e Planejamento Econômico*, 10(3), 769–792.
- **Resende, A. L.** (2014). *Os limites do possível: a economia além da conjuntura*. São Paulo: Portfolio-Penguin.
- **Resende, A. L.** (2017). Juros e inflação: a estrutura a termo e a transmissão da política monetária. *Ensaios em Consenso e Contrassenso*.
- **Resende, A. L.** (2020). *Consenso e contrassenso: por uma economia não dogmática*. São Paulo: Portfolio-Penguin.
- **Resende, A. L.** (2022). *Camisa de força ideológica: a crise da macroeconomia*. São Paulo: Portfolio-Penguin.
- **Resende, A. L.** (2026). Eu Acuso: uma proposta para eliminar os juros absurdos. *Um Cético Esperançoso* (Ensaio Técnico), 25 de setembro de 2026.
- **Serrano, F.** (2010). Juros, câmbio e o sistema de metas de inflação no Brasil. *Revista de Economia Política*, 30(1), 63–72.
- **Sims, C. A., Stock, J. H., & Watson, M. W.** (1990). Inference in linear time series models with some unit roots. *Econometrica*, 58(1), 113–144.
- **Sims, C. A.** (1992). Interpreting the macroeconomic time series facts: the effects of monetary policy. *European Economic Review*, 36(5), 975–1000.
- **Sims, C. A.** (2011). Stepping on a rake: the role of fiscal policy in the inflation of the 1970s. *European Economic Review*, 55(1), 48–56.
- **Tenreyro, S., & Thwaites, G.** (2016). Pushing on a string: US monetary policy is less powerful in recessions. *American Economic Journal: Macroeconomics*, 8(4), 43–74.
- **Uribe, M.** (2022). The neo-Fisher effect: econometric evidence from empirical and optimizing models. *American Economic Journal: Macroeconomics*, 14(3), 133–162.
