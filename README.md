# Juros, Fragilidade Financeira e o Canal Fiscal-Custos

**Uma Formalização e Teste Empírico em SVAR e Projeções Locais da Hipótese de André Lara Resende para o Brasil (2005–2026)**

**Autor:** Ângelo Augusto Bonvenuto  

---

## 📌 Visão Geral do Projeto

Este repositório contém o artigo acadêmico completo, a base de dados macroeconômicos do Banco Central do Brasil (BCB/SGS) e o pacote de replicação econométrica que formaliza analiticamente e testa empiricamente as teses heterodoxas contemporâneas — com destaque para as formulações de André Lara Resende (2017, 2020, 2023) — acerca dos limites e potenciais efeitos perversos da política monetária no Brasil.

### 🎯 Questões Centrais Investigadas
1. **Canal de Custos da Firma:** Sob mercados imperfeitos e alta necessidade de capital de giro (*working capital*), choques de alta da taxa Selic encarecem a estrutura de custos empresariais e são repassados aos preços livres?
2. **Efeito Riqueza Fiscal e Dívida Flutuante:** Em uma economia cuja dívida pública e operações compromissadas são predominantemente indexadas à taxa flutuante diária (Selic/LFT), a elevação dos juros expande a renda financeira dos rentistas, alimentando pressões fiscais e contrabalançando a contração da demanda agregada?
3. **Fragilidade Financeira das Famílias (Minskyana):** A elevação da taxa terminal de juros comprime a liquidez e expande de forma imediata o comprometimento da renda das famílias com o serviço da dívida (juros + amortizações), antes que ocorra desalavancagem do estoque nominal?

---

## 🔬 Metodologia Econométrica

Para separar causalidade de endogeneidade da política monetária, foram implementadas duas abordagens complementares cobrindo uma amostra mensal contínua de **258 observações (março/2005 a agosto/2026)** extraídas diretamente da API de Séries Temporais do Banco Central do Brasil (SGS):

1. **VAR Estrutural (SVAR):**
   - Identificação recursiva via Decomposição de Cholesky.
   - Ordenamento causal estrutural:
     $$\mathbf{Y}_t = \begin{bmatrix} \ln(\text{IC-Br}_t) & \ln(\text{IBC-Br}_t) & \pi^{\text{livres}}_t & i_t & \text{Serviço Dívida}_t \end{bmatrix}'$$
   - Seleção ótima de defasagens por critérios de informação ($p = 6$ pelo critério AIC).
   - Cálculo de Funções de Resposta ao Impulso (IRF com IC de 95%) e Decomposição da Variância do Erro de Previsão (FEVD).

2. **Projeções Locais (Jordà, 2005):**
   - Teste de robustez semi-paramétrico horizonte a horizonte ($h = 0, 1, \dots, 24$).
   - Estimação com erros-padrão robustos a heterocedasticidade e autocorrelação de Newey-West (HAC) com largura de banda dependente de $h$.
   - Confirmação da dinâmica temporal e resistência a erros de especificação estrutural.

---

## 📊 Principais Resultados Empíricos

- **Evidência de *Price Puzzle* nos Preços Livres:** A inflação de preços livres reage positivamente ao choque monetário durante os primeiros 6 meses ($+0{,}2109$ p.p.), tornando-se desinflacionária de forma consistente apenas a partir do 12º mês.
- **Pico de Fragilidade Financeira das Famílias:** O comprometimento de renda das famílias com o serviço da dívida atinge seu pico positivo no 12º mês após o choque ($+0{,}6645$ p.p.), evidenciando que choques restritivos na Selic asfixiam a liquidez e a renda disponível das famílias devedoras muito antes de conter os estoques de crédito.
- **Convergência Robusta SVAR vs. LP:** A comparação das IRFs do SVAR com as Projeções Locais confirma a mesma trajetória dinâmica sob ambas as técnicas, atestando a robustez dos resultados.

### Gráficos Principais

| Figura | Descrição |
| :--- | :--- |
| ![Séries Históricas](figuras/figura1_series_historicas.png) | **Figura 1:** Evolução das séries temporais macroeconômicas (2005–2026). |
| ![IRF SVAR](figuras/figura2_irf_svar.png) | **Figura 2:** Funções de Resposta ao Impulso (IRF) a um choque de 100 bps na Selic. |
| ![FEVD SVAR](figuras/figura3_fevd_svar.png) | **Figura 3:** Decomposição da Variância do Erro de Previsão (FEVD). |
| ![SVAR vs LP](figuras/figura4_lp_vs_svar.png) | **Figura 4:** Comparação de Robustez: SVAR (Cholesky) vs. Projeções Locais (Jordà, 2005). |

---

## 📁 Estrutura do Repositório

```bash
artigo-politica-monetaria/
├── README.md                           # Documentação e apresentação do projeto
├── .gitignore                          # Arquivos e diretórios ignorados pelo Git
├── artigo_hipotese_lara_resende.md     # Artigo completo formatado em Markdown
├── artigo_svar_lara_resende.tex        # Manuscrito acadêmico em LaTeX (padrão periódico)
├── referencias.bib                     # Referências bibliográficas completas em BibTeX
├── data/
│   └── base_macro_bcb.csv              # Base de dados histórica mensal BCB/SGS (258 obs)
├── scripts/
│   ├── estimacao_svar_lara_resende.py  # Script de coleta, testes ADF, estimação SVAR e FEVD
│   ├── estimacao_local_projections.py  # Script de Projeções Locais (Jordà) e comparação
│   └── test_bcb_api.py                 # Script de teste de conectividade com a API SGS/BCB
├── resultados/
│   ├── resultados_svar_summary.txt     # Resumo estatístico do SVAR e valores numéricos das IRFs
│   └── comparacao_svar_vs_lp.txt       # Tabela de comparação ponto a ponto entre SVAR e LP
└── figuras/
    ├── figura1_series_historicas.png   # Gráficos das séries temporais
    ├── figura2_irf_svar.png            # Funções de Resposta ao Impulso do SVAR
    ├── figura3_fevd_svar.png           # Decomposição de Variância (FEVD)
    └── figura4_lp_vs_svar.png          # Comparativo de robustez SVAR vs Projeções Locais
```

---

## 🚀 Como Replicar a Estimação

### Pré-requisitos
- Python 3.10+
- Bibliotecas: `pandas`, `numpy`, `statsmodels`, `matplotlib`, `requests`

### Execução via `uv` (Recomendado)

Você pode executar diretamente sem necessidade de gerenciar ambientes virtuais manualmente utilizando o [`uv`](https://github.com/astral-sh/uv):

```bash
# 1. Estimar o SVAR, gerar gráficos 1, 2 e 3 e resumo estatístico:
uv run --with pandas,numpy,statsmodels,matplotlib,requests python3 scripts/estimacao_svar_lara_resende.py

# 2. Executar as Projeções Locais de Jordà (2005) e gerar a Figura 4 comparativa:
uv run --with pandas,numpy,statsmodels,matplotlib python3 scripts/estimacao_local_projections.py
```

### Execução via `pip` / `venv` tradicional

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy statsmodels matplotlib requests

python scripts/estimacao_svar_lara_resende.py
python scripts/estimacao_local_projections.py
```

---

## 📚 Citação

Se utilizar os dados, modelos ou código deste trabalho, favor citar:

```bibtex
@unpublished{bonvenuto2026juros,
  author    = {Bonvenuto, Angelo Augusto},
  title     = {Juros, Fragilidade Financeira e o Canal Fiscal-Custos: Uma Formaliza{\c{c}}{\~a}o e Teste Emp{\'\i}rico em SVAR da Hip{\'o}tese de Andr{\'e} Lara Resende para o Brasil (2005--2026)},
  year      = {2026},
  note      = {Manuscrito de Pesquisa e Pacote de Replica{\c{c}}{\~a}o Econom{\'e}trica},
  url       = {https://github.com/bonvenuto/artigo-politica-monetaria}
}
```
