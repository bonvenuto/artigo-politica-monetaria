# Juros Persistentes, Dominância Financeira da Dívida e Fragilidade das Famílias

**Formalização e Evidência Econométrica para a Hipótese de André Lara Resende no Brasil (2005–2026)**

**Autor:** Ângelo Augusto Bonvenuto  
*Pesquisador em Macroeconomia Aplicada e Econometria de Séries Temporais*

---

## 📌 Visão Geral do Projeto

Este repositório reúne um artigo acadêmico completo, a base de dados macroeconômicos oficiais do Banco Central do Brasil (BCB/SGS) e o pacote de replicação econométrica em Python voltados a enriquecer o debate contemporâneo sobre a política monetária brasileira. O estudo formaliza matematicamente e submete a testes empíricos as teses desenvolvidas por **André Lara Resende** (1980, 2017, 2020, 2023) e consolidadas em seu ensaio recente ***[Eu Acuso: uma proposta para eliminar os juros absurdos](Um%20C%C3%A9tico%20Esperan%C3%A7oso%20-%20Eu%20Acuso_%20uma%20proposta%20para%20eliminar%20os%20juros%20absurdos.pdf)*** (setembro de 2026).

### 🎯 Eixos Analíticos Investigados

1. **O Mito do Descontrole Fiscal Primário vs. A Conta de Juros:** Com um déficit primário entre os menores do mundo ($-0{,}4\%$ a $-0{,}7\%$ do PIB segundo o FMI e o BCB), o déficit nominal brasileiro de quase $10\%$ do PIB decorre do serviço da dívida ($10{,}5\%$ do PIB sobre a DBGG de $82{,}5\%$ do PIB, ou R\$ 1,4 trilhão ao ano). Uma Selic fixada acima do dobro do crescimento nominal do PIB faz a relação dívida/PIB crescer $\approx 5{,}7\%$ ao ano exclusivamente por efeito dos juros, corroendo endogenamente a credibilidade fiscal.
2. **Achatamento da Curva de Phillips e Efeito Neo-Fisheriano:** Sob moeda endógena, reservas remuneradas (operações compromissadas) e uma Curva de Phillips horizontalizada, manter a taxa básica de juros estacionada em patamares absurdamente elevados por longos períodos não ancorou a inflação; ao contrário, pressiona os preços via canal de custos do capital de giro e convergência neo-fisheriana ($\pi = i - r$).
3. **O Paradoxo da *Duration* Curta (LFTs) e o Efeito Desinflacionário da Redução da Selic:** Apoiando-se na Teoria Fiscal do Nível de Preços (Cochrane, 2023, 2026) e em Resende (2026), demonstra-se que, como mais da metade da dívida pública brasileira é indexada à Selic diária (LFTs, *duration* zero), **reduzir a Selic corta imediatamente o serviço da dívida sem elevar seu valor presente**, evitando o repique inflacionário fiscal de curto prazo (enquanto mais de US\$ 350 bilhões em reservas internacionais blindam o canal cambial de *carry-trade*).
4. **Fragilidade Financeira Minskyana das Famílias:** A elevação e manutenção da Selic em patamares extremos expandem o comprometimento da renda mensal das famílias com o serviço da dívida bancária antes de desacelerar o estoque de crédito.

---

## 🔬 Metodologia Econométrica (2005–2026)

Sobre uma amostra mensal contínua de **258 observações (março/2005 a agosto/2026)** extraídas da API SGS/BCB:

1. **VAR Estrutural (SVAR):** Identificação recursiva de Cholesky ($p = 6$ via AIC) sobre $\mathbf{Y}_t = [\ln(\text{IC-Br}_t), \, \ln(\text{IBC-Br}_t), \, \pi^{\text{livres}}_t, \, \text{Selic}_t, \, \text{Serviço Dívida}_t]'$, com estimação de IRFs e Decomposição de Variância (FEVD).
2. **Projeções Locais Lineares (Jordà, 2005):** Estimação direta horizonte a horizonte ($h = 0, \dots, 24$) com erros-padrão robustos de Newey-West (HAC).
3. **Projeções Locais Dependentes de Estado (State-Dependent LP):** Separação não-linear entre regimes de **Platô de Juros Persistentemente Altos** (média móvel de 12 meses da Selic $> 11{,}27\%$ a.a.) e **Regime de Juros Moderados** ($\le 11{,}27\%$ a.a.), avaliando o impacto acumulado sobre o nível de preços livres ($\sum_{j=0}^h \pi_{t+j}^{livre}$) e o efeito desinflacionário de cortes na Selic.

---

## 📊 Principais Resultados Empíricos

- **Curva de Phillips Horizontalizada na FEVD:** O nível de atividade ($\ln(\text{IBC-Br})$) explica apenas **$3{,}1\%$ a $7{,}4\%$** da variância da inflação livre em 24 meses, contra mais de $85\%$ explicados pela inércia inflacionária e choques de custos/commodities.
- ***Price Puzzle* e Asfixia Financeira das Famílias:** Choques de alta na Selic elevam a inflação livre nos primeiros 6 meses ($+0{,}2109$ p.p.) e provocam salto expressivo no comprometimento de renda das famílias com o serviço da dívida ($+0{,}6645$ p.p. no 12º mês).
- **Evidência Direta para *"Eu Acuso"* (Resende, 2026):** Nas Projeções Locais Dependentes de Estado, quando a economia se encontra em um **Platô de Juros Altos ($> 11{,}27\%$ a.a.)**, choques adicionais de juros **jamais reduzem a inflação acumulada em 24 meses** ($+0{,}3735$ p.p. em 6 meses, $p = 0{,}0007$; $+0{,}3931$ p.p. em 9 meses, $p = 0{,}0109$; $+0{,}2912$ p.p. em 24 meses). Simetricamente, **reduzir a Selic a partir desse platô elevado reduz a inflação acumulada de forma imediata e persistente**.

### Síntese Visual dos Resultados

| Figura | Descrição |
| :--- | :--- |
| ![Séries Históricas](figuras/figura1_series_historicas.png) | **Figura 1:** Evolução das séries temporais macroeconômicas (2005–2026). |
| ![IRF SVAR](figuras/figura2_irf_svar.png) | **Figura 2:** Funções de Resposta ao Impulso (IRF) a um choque positivo na Selic. |
| ![FEVD SVAR](figuras/figura3_fevd_svar.png) | **Figura 3:** Decomposição da Variância do Erro de Previsão (FEVD). |
| ![SVAR vs LP](figuras/figura4_lp_vs_svar.png) | **Figura 4:** Robustez Linear: SVAR (Cholesky) vs. Projeções Locais (Jordà, 2005). |
| ![Regime Juros Altos LP](figuras/figura5_regime_juros_altos_lp.png) | **Figura 5:** Projeções Locais Dependentes de Estado: Platô de Juros Altos e Efeito Desinflacionário da Redução da Selic. |

---

## 📁 Estrutura do Repositório

```bash
artigo-politica-monetaria/
├── README.md                                  # Documentação e síntese do projeto
├── artigo_hipotese_lara_resende.md            # Artigo completo em Markdown
├── artigo_svar_lara_resende.tex               # Manuscrito acadêmico em LaTeX
├── referencias.bib                            # Bibliografia completa em BibTeX
├── Um Cético Esperançoso - Eu Acuso_...pdf    # Ensaio de referência de André Lara Resende (set/2026)
├── data/
│   └── base_macro_bcb.csv                     # Base mensal BCB/SGS (258 observações: 2005-03 a 2026-08)
├── scripts/
│   ├── estimacao_svar_lara_resende.py         # Coleta BCB, testes ADF, SVAR, IRFs e FEVD
│   ├── estimacao_local_projections.py         # Projeções Locais lineares (Jordà, 2005)
│   ├── estimacao_regime_juros_altos.py        # Projeções Locais Dependentes de Estado (Platô de Juros)
│   └── test_bcb_api.py                        # Teste de conectividade com a API SGS/BCB
├── resultados/
│   ├── resultados_svar_summary.txt            # Resumo estatístico do SVAR
│   ├── comparacao_svar_vs_lp.txt              # Tabela comparativa SVAR vs. LP Linear
│   └── regime_juros_altos_lp.txt              # Tabela das Projeções Locais Dependentes de Estado
└── figuras/
    ├── figura1_series_historicas.png          # Evolução histórica das séries (2005–2026)
    ├── figura2_irf_svar.png                   # IRFs do modelo SVAR
    ├── figura3_fevd_svar.png                  # Decomposição de Variância (FEVD)
    ├── figura4_lp_vs_svar.png                 # Comparativo SVAR vs. Projeções Locais
    └── figura5_regime_juros_altos_lp.png      # Efeito do Platô de Juros Altos e Corte Desinflacionário
```

---

## 🚀 Como Replicar a Estimação

```bash
# 1. Estimar o SVAR e gerar as Figuras 1, 2 e 3:
uv run --with pandas,numpy,statsmodels,matplotlib,requests python3 scripts/estimacao_svar_lara_resende.py

# 2. Estimar as Projeções Locais lineares e gerar a Figura 4:
uv run --with pandas,numpy,statsmodels,matplotlib python3 scripts/estimacao_local_projections.py

# 3. Estimar as Projeções Locais Dependentes de Estado (Resende, 2026) e gerar a Figura 5:
uv run --with pandas,numpy,statsmodels,matplotlib python3 scripts/estimacao_regime_juros_altos.py
```
