# O Patamar dos Juros Altera a Transmissão da Política Monetária?

**Evidência de Projeções Locais Dependentes de Estado e do Comprometimento de Renda das Famílias no Brasil (2005–2026)**

**Autor:** Ângelo Augusto Bonvenuto
*Pesquisador independente*

---

## Visão geral

Este repositório reúne o artigo (LaTeX, PDF compilado e espelho em Markdown), as séries do Banco Central do Brasil (SGS e Olinda/Focus) e o código de replicação em Python.

O artigo pergunta se a resposta da inflação a surpresas da Selic muda quando os juros estão em um platô persistentemente alto. A hipótese é inspirada nas teses de André Lara Resende, em particular no ensaio ***[Eu Acuso: uma proposta para eliminar os juros absurdos](https://andrelararesende.substack.com/p/eu-acuso-uma-proposta-para-eliminar)*** (setembro de 2026). O artigo separa os componentes da tese que testa dos que não testa (Tabela 1 do artigo):

- **Testados:** a dependência de estado ($H_1$), o nível associado ao platô ($H_1'$) e o comprometimento de renda das famílias com juros ($H_2$).
- **Não testados:** o componente neo-fisheriano (mudanças permanentes do patamar de juros), o canal da dívida pública pós-fixada e a proposta de redução coordenada da Selic.

## Principais resultados

- **Dependência de estado ($H_1$) — inconclusiva.** Na especificação-base, não se detecta diferença entre a resposta da inflação de itens livres no platô (Selic MM12 > 11,27% a.a.) e no regime moderado. O sup-Wald sobre uma grade de limiares, calibrado por bootstrap sob a nula de linearidade (999 réplicas, com reestimação do VAR, do choque e do estado), não rejeita a igualdade. O teste tem pouco poder: diferenças menores que 0,23 a 0,42 p.p. por choque de 1 desvio-padrão (até 0,52 com EP EWC) são detectadas com probabilidade inferior a 80%. As evidências pontuais favoráveis à hipótese — a LP com controles interagidos (Wald p = 0,001 nos valores críticos assintóticos) e o limiar de 14% — perdem significância quando calibradas (p ≈ 0,10 e sup-Wald p = 0,13; 0,46 com trimming de 15%).
- **Regime moderado.** O efeito desinflacionário de 24 meses (−2,20 p.p. por 1 p.p.; p = 0,012; Holm p = 0,073) só é significativo com 6 (e, marginalmente, 9) defasagens e perde significância com a meta Selic de fim de mês (SGS 432) e com o IPCA cheio.
- **Nível do platô ($H_1'$).** A permanência no platô associa-se a inflação acumulada 1,6 p.p. mais alta em 12 meses (p = 0,003; EWC p = 0,013), associação compatível com a equação de Fisher e com a regra de reação. Ela some com o juro real *ex ante* e para limiares acima de 13%, e não é significativa sob bootstrap (p = 0,093).
- **Canal das famílias ($H_2$).** Um choque de 1 desvio-padrão eleva o comprometimento de renda com juros (SGS 29033) em 0,07 a 0,09 p.p. em 12 a 18 meses (Holm p = 0,012 em 12 meses), resultado que resiste à meta Selic, ao corte em 2023 e ao choque agregado por trimestre. Com valor crítico calibrado por bootstrap (3,06 contra t = 2,76), porém, o efeito em 12 meses é marginal (p ≈ 0,08). O efeito vem da taxa implícita J/E (+6,4 pontos logarítmicos por 1 p.p.), não do estoque: com controles padronizados, o endividamento não responde. Não se detecta efeito no serviço total, e a assimetria entre surpresas positivas e negativas não é robusta (Holm p = 0,34). O resultado documenta o repasse convencional da Selic, e não evidência a favor ou contra a tese.
- **Aritmética fiscal em termos reais.** Com inflação rígida, o corte gradual da Selic para 7,5% reduziria a razão DBGG/PIB em 1,1–1,3 p.p. no primeiro ano; o alívio se anula com repasse à inflação de cerca de metade (ω* ≈ 0,5–0,6), já levando em conta os títulos indexados ao IPCA. Depois da rolagem de toda a dívida, a economia de cerca de 4% do PIB citada no ensaio é um limite superior (inflação rígida, prêmio a termo nulo).

## Dados

Amostra mensal de **258 observações (mar/2005 a ago/2026)**, extraída em 9/11/2026 (`data/safra_dados.txt`).

| Arquivo / coluna | Código BCB | Descrição |
| :--- | :---: | :--- |
| `base_macro_bcb.csv`: `selic` | SGS 4189 | Selic acumulada no mês, anualizada (% a.a.) |
| `ipca_livres` | SGS 11428 | IPCA – itens livres (% a.m., sem ajuste sazonal) |
| `ipca_cheio`, `ipca_adm`, `ipca_comerc` | SGS 433, 4449, 4447 | IPCA cheio, monitorados e comercializáveis (% a.m.) |
| `juros_divida`, `servico_divida`, `endividamento` | SGS 29033, 29034, 29037 | Comprometimento com juros e com serviço total; endividamento (% renda) |
| `ibc_br`, `ptax` | SGS 24364, 3696 | IBC-Br dessazonalizado; PTAX venda, fim de período |
| `ic_br` | SGS 27574 | IC-Br **em R\$** (usado só na robustez) |
| `exp_ipca_12m` | Olinda/Focus | Mediana suavizada do IPCA 12 meses à frente |
| `base_complementar_bcb.csv`: `ic_br_usd` | SGS 29042 | IC-Br **em US\$** (especificação-base) |
| `meta_selic` | SGS 432 | Meta Selic, último dia do mês (robustez) |
| `amortizacao`, `servico_sem_hab`, `endiv_sem_hab` | SGS 29036, 29035, 29038 | Amortização; serviço sem habitacional; endividamento sem habitacional |
| `dbgg`, `dlsp`, `nfsp_nominal_12m`, `nfsp_primario_12m` | SGS 13762, 4513, 5727, 5793 | Insumos fiscais (% PIB) |
| `ipca_12m`, `pib_12m` | SGS 13522, 4382 | IPCA 12 meses; PIB acumulado em 12 meses (R\$ milhões) |

As séries de comprometimento são estimativas do BCB, com renda em média móvel trimestral mensalizada por Denton-Cholette (Nota Técnica 55/2021). A composição e o custo da Dívida Pública Federal vêm do Relatório Mensal da Dívida do Tesouro (setembro de 2026).

## Estratégia empírica

1. **SVAR(6)** com 11 dummies sazonais exógenas, identificação recursiva de Cholesky sobre $[\ln \text{IC-Br}^{US\$}, \ln \text{PTAX}, \ln \text{IBC-Br}, \pi^{livre}, \text{Selic}, J^{fam}]$ e choque escalado para +1 p.p. de impacto (desvio-padrão do choque: 0,156 p.p.). Intervalos por bootstrap com correção de viés (Kilian, 1998).
2. **LPs lineares** com os mesmos regressores e dummies sazonais. A igualdade com o SVAR em h = 0 vale por construção.
3. **LPs dependentes de estado e assimétricas** (Tenreyro & Thwaites, 2016), com inferência Newey-West, EWC (Lazarus et al., 2018), bootstrap de blocos com bandas sup-t, bootstrap recursivo sob a nula de linearidade e p-valores de Holm na família h ∈ {3, …, 24}.
4. **Inferência sobre o nulo:** IC, limites unilaterais e efeito mínimo detectável da diferença entre regimes; LP totalmente interagida calibrada sob a nula; variante *wild* do bootstrap; sup-Wald com e sem trimming; sensibilidade a p ∈ {2, 4, 6, 9, 12}; primeiro estágio da Selic por regime; grade de limiares de 9% a 14% com sup-Wald; episódios do platô.
5. **Robustez (10 especificações):** sem sazonais; dummy COVID-19; Focus; IPCA cheio; juro real *ex ante*; limiares de 10% e 12%; choque de VAR sem sazonais; meta Selic de fim de mês; IC-Br em R\$.
6. **Canal das famílias:** o mesmo choque para juros, amortização, serviço total, serviço sem habitacional, endividamento e taxa implícita. Robustez de $H_2$ a estoque defasado, MA(2), EWC, amostra trimestral, amostra até 2023 e assimetria.

## Estrutura do repositório

```bash
artigo-politica-monetaria/
├── README.md
├── artigo_svar_lara_resende.tex          # Manuscrito (fonte principal)
├── artigo_svar_lara_resende.pdf          # Artigo compilado (32 páginas)
├── artigo_anonimo.tex / .pdf             # Versão anônima para submissão (sem autor, URL e apêndice de versões)
├── artigo_hipotese_lara_resende.md       # Espelho em Markdown, gerado a partir do .tex
├── referencias.bib
├── (ensaio Eu Acuso: não versionado; ver link no topo)
├── data/
│   ├── base_macro_bcb.csv                # Base principal (258 obs.)
│   ├── base_complementar_bcb.csv         # Séries complementares (IC-Br US$, meta Selic, 2903x, fiscais)
│   └── safra_dados.txt                   # Data de extração
├── scripts/
│   ├── comum.py                          # Especificação-base, choque, LPs, EWC, Holm
│   ├── coleta_series_complementares.py   # Baixa as séries (e a base principal, se ausente)
│   ├── estimacao_svar_lara_resende.py    # SVAR, bootstrap de Kilian, FEVD, Figuras 1–3
│   ├── estimacao_local_projections.py    # LP linear vs. SVAR, Figura 4
│   ├── estimacao_regime_juros_altos.py   # LPs de estado, sup-t, robustez, câmbio, Figura 5
│   ├── inferencia_regimes.py             # Poder, LP interagida, p, bootstrap sob a nula, grade, Figura 6
│   ├── canal_familias.py                 # Decomposição do comprometimento e robustez de H2
│   ├── aritmetica_fiscal.py              # Insumos fiscais e cenários em termos reais
│   ├── tex_para_markdown.py              # Gera o espelho em Markdown
│   └── test_bcb_api.py
├── resultados/                           # Saídas numéricas de cada script
├── figuras/                              # Figuras 1–6
└── revisao/                              # Pareceres e painel de revisão independente
```

## Como replicar

```bash
UV="uv run -q --with pandas,numpy,statsmodels,matplotlib,scipy,requests python3"
cd scripts
$UV coleta_series_complementares.py      # séries do BCB
$UV estimacao_svar_lara_resende.py       # ~15 s
$UV estimacao_local_projections.py
$UV estimacao_regime_juros_altos.py      # ~3 min (bootstrap de blocos)
$UV inferencia_regimes.py                # alguns minutos (bootstrap sob a nula, 999 réplicas, 8 processos)
$UV canal_familias.py
$UV aritmetica_fiscal.py
cd ..
latexmk -pdf -interaction=nonstopmode artigo_svar_lara_resende.tex
latexmk -pdf -interaction=nonstopmode artigo_anonimo.tex     # versão anônima
python3 scripts/tex_para_markdown.py
```

As sementes dos geradores aleatórios estão fixadas nos scripts.
