# Decisão Editorial e Roteiro de Revisão

**Manuscrito**: "Patamar de Juros, Dívida Pós-Fixada e Comprometimento de Renda das Famílias: Formalização Analítica e Evidência de Projeções Locais Dependentes de Estado para o Brasil (2005–2026)"
**Data da decisão**: 9 de novembro de 2026
**Rodada**: 1ª rodada deste painel simulado (o manuscrito se declara revisão pós-parecer de uma versão anterior)
**Papel**: `editorial_synthesizer_agent` (Fase 2). Este documento sintetiza e arbitra. Não acrescenta críticas próprias.

`calibration_status: NOT_CALIBRATED`
`criteria_binding_unavailable`: não há periódico-alvo confirmado. Nenhum juízo abaixo afirma adequação a um periódico específico.

---

## 1. Proveniência e limites

### 1.1 Painel

| Assento | Papel | Insumo lido | Recomendação | Confiança (autodeclarada) |
|---|---|---|---|---|
| EIC | Journal-Fit Reviewer | `relatorios/eic.md` | Major Revision | 4 |
| R1 | Metodologia (SVAR/LP) | `relatorios/r1_metodologia.md` + `r1_replica/r1_checks*` | Major Revision | 4 |
| R2 | Domínio (política monetária e fiscal) | `relatorios/r2_dominio.md` | Major Revision | 4 |
| R3 | Perspectiva (finanças das famílias) | `relatorios/r3_perspectiva.md` | Major Revision | 4 |
| DA | Devil's Advocate | `relatorios/devils_advocate.md` | não vota (só achados) | por achado |

Li os cinco relatórios por inteiro. Também li as passagens do manuscrito (`manuscrito/artigo_svar_lara_resende.tex`) necessárias para conferir as alegações em disputa. A confiança de 1 a 5 é só a declaração de escopo de cada assento: não serviu como peso, voto nem critério de desempate.

### 1.2 Eixos de proveniência

Não há artefato tipado `review-panel-provenance/1.0`. Os valores abaixo vêm do que o despacho declarou e do que os próprios relatórios afirmam. Não foram validados por replay.

| Eixo | Status |
|---|---|
| Separação de papéis | `true`. Cinco papéis distintos, cada um com foco e ponto cego declarados. |
| Contextos de invocação separados no painel | `unknown`. Foi declarado pelo despacho, mas não foi verificado por artefato. |
| Cegueira aos relatórios dos pares | `unknown`. Foi declarada pelo despacho e pelo DA ("nenhum outro relatório foi lido"), mas não foi verificada. |
| Família de modelo distinta | `false`. Os cinco assentos são o mesmo modelo. |
| Provedor distinto | `false` |
| Revisor humano distinto | `false`. Não houve revisor humano. |

**Divulgação de erro correlacionado.** Os cinco assentos são o mesmo modelo em contextos separados. Quando dois ou mais assentos concordam, isso mostra que papéis diferentes chegaram ao mesmo ponto. Não mostra que os erros sejam independentes: um viés ou uma leitura errada do modelo pode se repetir em todos os assentos. Em particular, R1 e DA fizeram reanálises com o mesmo código-base e chegaram aos mesmos números, por exemplo na trajetória da Selic por regime (R1-W4b e DA-M6). Isso confirma que a conta é reproduzível. Não equivale a uma segunda medição independente. Por isso, as contagens de consenso da Seção 3 devem ser lidas como cobertura de papéis, não como votos independentes.

### 1.3 O que não foi executado

Nesta rodada **não** foram executados: o protocolo mecânico de sprint contract (matriz de dimensões, `failure_conditions`, precedência), os manifests de blocos, os sidecars JSON (`revision-roadmap/1.0`, Schema 6), os scripts de checagem (`check_re_review_synthesis.py`, `check_pipeline_integrity.py`), o checkpoint cross-model e os anexos automáticos (checagem de acrônimos, checagem de referências sugeridas e reviewer claim check). As listas de referências sugeridas por R2 e R3 seguem como estão nos relatórios, sem verificação bibliográfica automática. A decisão segue o caminho sem contrato (`editorial_decision_standards.md`, matriz de recomendações e Synthesis Protocol).

### 1.4 Verificações feitas pelo sintetizador

Fiz estas verificações só para arbitrar alegações dos revisores. Elas não geram críticas novas.
- API pública do SGS/BCB (`api.bcb.gov.br/dados/serie/bcdata.sgs.<código>/dados`), consultada em 9 nov. 2026: séries 27574, 29042, 3698 (PTAX média mensal de venda), 5793, 5727, 13762 e 13522. Os arquivos estão em `scratchpad/verif_bcb/`.
- Script de comparação do IC-Br: `scratchpad/verif_icbr.py`. Reestimação do VAR(6) com 27574 e com 29042: `scratchpad/verif_icbr_var.py`. Ambos foram executados sobre a base do pacote.
- Reexecução de `r1_replica/r1_checks4.py` e de uma cópia de `r1_checks3.py` (em `scratchpad/r1_rerun/`), porque duas saídas citadas por R1 não estavam salvas em arquivo.
- Busca na web sobre a definição do IC-Br. O metadado oficial das séries 27574 e 29042 **não** foi localizado: a busca no catálogo `dadosabertos.bcb.gov.br` retornou zero resultados e a página do dataset retornou 404.

---

## 2. Decisão e justificativa

### Decisão: **Major Revision**

Os quatro assentos que pontuam recomendam Major Revision. O DA não registrou nenhum achado CRÍTICO. Pela matriz (Major/Major/Major/Major), a decisão é Major Revision, e as arbitragens abaixo não dão razão para afastar-se dela.

**Por que não Minor.** Três grupos de problemas exigem reanálise e reescrita estrutural, e não só ajustes.
- **Enquadramento.** O título, o resumo, o rótulo "modelo fechado" e a §5.2 prometem um teste confirmatório da tese e uma base para a proposta de política que a evidência não entrega (EIC-W1/W3/W4/W5, R2-W1/W7, R3-W5; DA-M1/M8/M9).
- **Inferência sobre H1.** Faltam poder do teste, intervalo da diferença entre regimes, robustez de β_mod^24 à escolha de p, inferência HAC robusta e invariância do choque entre regimes (R1-W1 a W5; DA-M4/M5/M6).
- **Exatidão de dados e números.** O IC-Br está em reais, e não em dólares (verificado, V1). A aritmética fiscal do Bloco II mistura bases e taxas (R2-W2, EIC-W5/W8). A construção das séries de comprometimento não é documentada (R3-W1).

**Por que não Reject.** Nenhum assento aponta falha fatal de desenho. O núcleo empírico é reproduzível byte a byte (R1-S1). H2 resiste às verificações independentes (R1-S3, R3-S3). O texto já relata os nulos com franqueza (EIC-S1, R1-S2, R2-S1, DA "pontos fortes"). Os quatro assentos afirmam que os defeitos podem ser corrigidos. O EIC avisa que, se o manuscrito voltar com o mesmo enquadramento, passaria a recomendar Reject (EIC, "Recomendação e Justificativa"). O autor deve ler isso como condição desta decisão.

### Questões bloqueantes (3, em ordem de origem)

| Ref. | Questão bloqueante | Assentos | Âncora | Itens do roteiro |
|---|---|---|---|---|
| B1 | O enquadramento e as alegações de política vão além da evidência: título e resumo "testando as hipóteses", "modelo analítico fechado", dívida pós-fixada fora do desenho empírico e §5.2 apoiada numa aritmética fiscal que contradiz o bloco de Fisher do próprio modelo | EIC, R2, R3, DA | `text: Resumo (PT), 1ª frase`; `text: §5.2, 1º parágrafo "A avaliação da proposta apoia-se..."` | REV-01, 03, 04, 05, 21 |
| B2 | A inferência sobre H1 e β_mod^24 não quantifica poder, sensibilidade a p, robustez HAC nem invariância do choque | R1, EIC, DA | `text: §4.5, item 2 "não encontra apoio nos dados"`; `table: Tabela 4, h=24` | REV-02, 12, 13, 14, 15 |
| B3 | Exatidão de séries e números: IC-Br rotulado em USD, aritmética fiscal com bases incompatíveis, séries 29033/29034 sem documentação | R2, EIC, R3, R1 | `table: Tabela 1, linha ICBr`; `text: §2 Bloco II "alívio fiscal imediato"` | REV-22, 29, 32 |

---

## 3. Consenso

**Regra de contagem.** O denominador são os quatro assentos que pontuam (EIC, R1, R2, R3). A posição do DA é registrada à parte. "Silêncio" não conta como concordância, e o ponto cego declarado de cada assento aparece indicado. Rótulos usados: **C-4** = 4/4; **C-3** = 3/4, com o quarto silente; **Corr.** = 2/4; **Único** = 1/4; **SPLIT** = há posição contrária, arbitrada na Seção 4. A severidade é a de cada assento, transportada sem reclassificação.

| SC | Subalegação | Assentos (severidade) | Contagem | DA | Rótulo |
|---|---|---|---|---|---|
| SC-1 | Título, resumo e palavras-chave prometem teste confirmatório; nome de pessoa nas palavras-chave | EIC-W1 (Major), R2-W7 (Major) | 2/4 | M2, dim. 8 | Corr. |
| SC-2 | Contribuição líquida não declarada; o nulo de H1 não é informativo sem IC e MDE da diferença entre regimes | EIC-W2 (Major), R1-W1 (Major) | 2/4 | diverge na direção (obs. "subvenda") | SPLIT com DA → D1 |
| SC-3 | Dívida pós-fixada e canal fiscal ausentes do desenho empírico | EIC-W3 (Major), R2-W8 (Major, parte "sem CDS/EMBI não separa") | 2/4 | M9 | Corr. |
| SC-4 | Bloco teórico "fechado" sem sê-lo, sem predição testável e desproporcional | EIC-W4 (Major) | 1/4 | M8, m1 | SPLIT com R2-S4 → D2 |
| SC-5 | Item 3 do Bloco II (r*, π*, prêmio de ~6 p.p.) sem fonte | EIC-W4 (Major), R2 (questão menor) | 2/4 | m4 | Corr. |
| SC-6 | "TFNP" usada para um canal de solvência, sem equação de valoração | R2-W5 (Minor) | 1/4 | M8(i) | Único |
| SC-7 | Alívio fiscal nominal incompatível com o mecanismo fisheriano invocado | R2-W1 (Major) | 1/4 | M1 | Único (+DA) |
| SC-8 | Aritmética do Bloco II: custo médio da DPF aplicado à DBGG, Selic confundida com custo médio, Δi de 5,5 contra 6,5 p.p. (13% contra ~14%) | R2-W2 (Major), EIC-W5 (Major, parte cenário) | 2/4 | — | Corr. |
| SC-9 | 5,7% contra 5,3% contra >5,5%; Fiscal Monitor sem referência | EIC-W8 (Minor), R2-W2.5 (Major) | 2/4 | m3 | Corr. (verificado, V3) |
| SC-10 | Alívio de 4,0–4,5% "após rolagem" supõe convergência de toda a curva | R2-W3 (Major) | 1/4 | m7 (Minor) | Único (+DA); severidade → D5 |
| SC-11 | "Duration zero" / "sem elevar o valor presente" contraria a própria Eq. de V_t(B) | R2-W4 (Major) | 1/4 | — | Único (verificado, V5) |
| SC-12 | §5.2 (governança e distribuição) não é sustentada pelas estimativas | EIC-W5 (Major), R2-W6 (Major, "base da avaliação"), R3-W5 (Major) | 3/4 (R1 silente, ponto cego declarado) | M7, m5 | **C-3** |
| SC-13 | Ciclos 2011–13 contra 2016–18 usados como evidência, com n=2 e sem dados | EIC-W5/W8, R2-W6 (Major) | 2/4 | M7 | Corr. (caracterização fiscal → V2) |
| SC-14 | H1 testa surpresas transitórias; o componente neo-fisheriano (permanente) não é testado | R2-W9 (Major) | 1/4 | M2 | Único (+DA) |
| SC-15 | §5.1: discriminação Blanchard × Lara Resende com critério errado ou impossível | R2-W8 (Major), EIC-W9 (Minor) | 2/4 | m2 | Corr. |
| SC-16 | Enquadramento centrado em um autor, com literatura cinzenta; lacunas de literatura revisada por pares | EIC-W6 (Major), R2-W13 (Minor), R2-W7 (Major) | 2/4 | — | Corr.; severidade → D5 |
| SC-17 | γ̂ é associação de nível (Fisher, causalidade reversa) e não deve ser vendido como "resultado mais estável" nem como "compatível com LR" | EIC ("Relevância"), R1-W9 (Minor), R2-W10 (Minor) | 3/4 (R3 silente, ponto cego declarado) | M3 (Major) | **C-3**; severidade → D5 |
| SC-18 | β_mod^24 depende de p=6 e de Holm aplicado de forma desigual; "estável entre especificações" é indevido | R1-W2 (Major) | 1/4 | M4 | Único (+DA; verificado, V4) |
| SC-19 | HAC com janela h+1 otimista, ~4 episódios efetivos, sem sup-t, Holm limitado | R1-W3 (Major), R1-W12 (Minor) | 1/4 | M4 (Holm) | Único; inferência de γ̂ → D3 |
| SC-20 | Choque não invariante entre regimes (placebo PTAX em h=0; Selic menos persistente no platô) | R1-W4 (Major) | 1/4 | M6 | Único (+DA; verificado, V4) |
| SC-21 | Cholesky sobre a Selic média mensal: o "choque" não é surpresa do Copom | R1-W5 (Major) | 1/4 | M5 | Único (+DA) |
| SC-22 | O SVAR-base não tem dummies sazonais, ao contrário do que diz o resumo; o price puzzle é em boa parte sazonal | R1-W6 (Major) | 1/4 | — | Único (verificado, V5) |
| SC-23 | A equivalência LP–SVAR em h=0 é mecânica | R1-W7 (Minor) | 1/4 | diverge (obs.) | SPLIT com DA → D4 |
| SC-24 | A normalização em +1 p.p. extrapola; a unidade principal deveria ser 1 DP | EIC-W11, R1-W8, R3-W7 (todos Minor) | 3/4 (R2 silente) | m5 | **C-3** |
| SC-25 | Limiar na mediana não testado; indicador construído com a própria Selic | R1-W9 (Minor) | 1/4 | "premissa não examinada" | Único (+DA) |
| SC-26 | VAR com raiz quase unitária: viés e bandas no limite | R1-W10 (Minor) | 1/4 | — | Único |
| SC-27 | Inconsistências numéricas pequenas (+0,357 contra +0,344; "quatro" contra cinco episódios; convenção da FEVD) | R1-W11 (Minor) | 1/4 | m8 | Único (+DA; verificado) |
| SC-28 | SGS 27574 é o IC-Br em reais, não em USD | R2-W11 (Major) | 1/4 | — | Único (**verificado: procede**, V1) |
| SC-29 | Atribuição a Cochrane (2026) de teses sobre o Brasil | R2-W12 (Minor) | 1/4 | — | Único |
| SC-30a | Séries 29033/29034 sem documentação de construção e sem safra | R3-W1 (Major), R1 ("Coleta de dados": safra) | 2/4 | — | Corr. |
| SC-30b | Média móvel trimestral (MA(2)) subestima erros-padrão em horizontes curtos | R3-W1 (Major) | 1/4 | — | Único |
| SC-31 | H2 não separada da identidade; falta decompor taxa × estoque | R3-W2 (Major); EIC-W2 (H2 "quase mecânico") | 2/4 | obs. "e daí?" | Corr. |
| SC-32 | "Não se transmite" ao serviço total: não testado e estimado com choques diferentes | R3-W3 (Major) | 1/4 | m6 (Minor) | Único (+DA); severidade → D5 |
| SC-33 | Descrição de η_pos imprecisa (tetos, estoque × fluxo, TR) | R3-W4 (Minor) | 1/4 | alt. 6 | Único |
| SC-34 | Título do painel (b) da Figura 2 ("Fragilidade Financeira") contradiz o texto | R3-W6 (Minor) | 1/4 | — | Único (verificado no script, V5) |
| SC-35 | Manuscrito não anonimizado; histórico de versões no texto | EIC-W7 (Minor) | 1/4 | — | Único |
| SC-36 | Resumo longo (~460/380 palavras) | EIC-W10 (Minor) | 1/4 | — | Único |
| SC-37 | Bibliografia: entradas não citadas, Fiscal Monitor ausente, chave e conteúdo de `pastore1996reforma`, versões publicadas de Blanchard (2004) | EIC (questões menores), R2 (questões menores) | 2/4 | — | Corr. |

**Leitura de conjunto.** Nenhuma subalegação chega a C-4. Isso decorre da divisão de papéis: cada assento declarou um ponto cego, e R1 e R3 não avaliam enquadramento nem política. As duas C-3 de maior peso são SC-12 (a §5.2 não é sustentada) e SC-17 (o γ̂ é apresentado além do que mostra). A convergência mais significativa vai além dos rótulos: os quatro assentos e o DA, por caminhos diferentes, chegam à mesma conclusão. O artigo que os dados sustentam é um nulo bem documentado sobre dependência de estado mais a quantificação do canal de juros das famílias, e não um teste confirmatório da tese.

---

## 4. Divergências e arbitragens

### 4.1 Divergências entre assentos

**D1 — Como ler o nulo de H1 (SC-2)**
- *EIC-W2 e R1-W1*: o nulo precisa ser apresentado de forma informativa. R1 mostra que o teste quase não tem poder (MDE de 80% ≈ 2,8 p.p. em h=12 e 2,5 p.p. em h=24; IC 95% da diferença de [−3,05; +0,89] em h=12 e de [−0,72; +2,81] em h=24) e pede trocar "não encontra apoio" por "inconclusivo".
- *DA (observação "subvenda do resultado negativo"; contra-argumento, 3º ponto)*: a evidência "se inclina para a transmissão convencional", e o artigo deveria dizê-lo com mais força.
- *Tipo*: direção.
- *Resolução*: prevalece a leitura de R1 (inconclusivo, com IC e MDE).
- *Fundamento*: a evidência e a competência são de R1. Os intervalos da diferença incluem valores dos dois sinais. Reexecutei a LP totalmente interagida de R1, que não estava no arquivo de saída salvo. Em h=24 ela dá β_alto = +1,76 (p=0,029), β_mod = −2,27 (p=0,005) e Wald p=0,001, isto é, um sinal *favorável* a H1 (R1 a apresenta como evidência de fragilidade da especificação, não como apoio a H1). Uma leitura que se incline para a transmissão convencional exigiria descartar essa especificação, e o DA não faz isso. A leitura direcional do DA em M6 também é só parcialmente sustentada (ver adjudicação de M6). O autor deve adotar "inconclusivo" e pode discutir a leitura do DA como uma das interpretações compatíveis.

**D2 — Valor da formalização da Seção 2 (SC-4)**
- *R2-S4*: a formalização "torna a tese verbal falsificável" e deixa claro quais parâmetros teriam de prevalecer.
- *EIC-W4 e DA-M8*: o bloco não gera predição confrontada com as estimativas; a dependência de estado é suposta, não derivada; o rótulo "fechado" é incorreto.
- *Tipo*: existência (é ou não é um defeito).
- *Resolução*: prevalece EIC/DA quanto ao papel do bloco na evidência. O mérito expositivo apontado por R2 fica registrado.
- *Fundamento*: o próprio manuscrito declara que "os demais parâmetros (φ, κ, σ, μ, ρ′) não são estimados neste artigo, e a posição do Brasil em relação a θ* depende..." (§2, parágrafo após a Eq. de θ*) e que a Eq. de dπ/di é tomada "sem resolver o equilíbrio dinâmico do sistema". Uma condição que não é calibrada nem confrontada não está sendo falsificada pelas LPs. A clareza taxonômica que R2 elogia sobrevive a uma versão condensada (opção (a) de EIC-W4). A escolha entre condensar e calibrar fica com o autor (REV-04).

**D3 — Robustez inferencial de γ̂¹² (SC-17/SC-19)**
- *DA (observações)*: γ̂¹² continua significativo com HAC de 24 e 36 defasagens e em todas as exclusões de um platô por vez. "O problema está na interpretação, não na estatística."
- *R1-W3*: com EWC, p=0,013. Com bootstrap por blocos, t=1,95. Nenhum horizonte é significativo na banda sup-t.
- *Tipo*: severidade e avaliação da evidência.
- *Resolução*: as duas posições são compatíveis no ponto estimado (+1,5 a +1,8, estável) e divergem na significância. Prevalece a exigência de R1: reportar inferência robusta (EWC ou fixed-b), sup-t e a contagem de episódios.
- *Fundamento*: R1 é o assento de metodologia. As variantes do DA mudam a janela do núcleo Bartlett, o que não resolve o viés de amostra pequena com regressor de estado persistente apontado por R1. EWC e bootstrap tratam desse problema. As saídas de R1 conferem (`r1_checks2_output.txt` §3; `r1_checks_output.txt` §H).

**D4 — Equivalência LP–SVAR em h=0 (SC-23)**
- *R1-W7*: por Frisch-Waugh-Lovell, a igualdade vale por construção e não confirma nada.
- *DA (observações)*: é um "ponto de credibilidade".
- *Resolução*: prevalece R1.
- *Fundamento*: é álgebra. A LP usa como regressor o resíduo ortogonalizado do próprio VAR, com as mesmas defasagens. A inflação em h=0 tem coeficiente exatamente 0 com p=1,000 na Tabela 3, o que confirma a construção. A reprodução exata dos coeficientes, que o DA também elogia, é outro ponto e continua sendo um mérito.

**D5 — Divergências de severidade** (as severidades seguem transportadas; a obrigação editorial é definida pelo peso na decisão e pelo custo do remédio)
- R3-W3 (Major) × DA-m6 (Minor), sobre o serviço total. *Resolução*: `must_fix`. A troca de palavras é barata, mas a subalegação (c) de R3-W3, de que os resultados vêm de choques diferentes, envolve reanálise. Com o mesmo choque, R3 obteve h=18 +0,81 (p=0,035), o que pode mudar a conclusão do Apêndice A. Nota: o texto já diz "não se transmite **de forma significativa**" (Resumo; §5.3, item 5). As citações de R3 e do DA omitem o qualificador (V5).
- R2-W3 (Major) × DA-m7 (Minor), sobre a rolagem de 4%. *Resolução*: declarar o número como limite superior condicional é `must_fix` (texto). Os cenários com cronograma e prêmio a termo são `should_fix`. Se a §5.2 for condensada (REV-05), o peso do número cai.
- EIC-W6 (Major) × R2-W13 (Minor), sobre a literatura. R2 rebaixou a própria severidade por `[FIELD-NORM UNVERIFIED]`. *Resolução*: `should_fix`. A parte de EIC-W6 sobre "fatos estilizados" ancorados no ensaio vai para REV-08 (`must_fix`), porque toca a exatidão dos números.
- R1-W9 e R2-W10 (Minor) × DA-M3 (Major), sobre o γ̂. *Resolução*: `must_fix` (reescrita barata, C-3 com o DA a favor).
- R3-W5 (Major) × DA-m5 (Minor), sobre o alívio "expressivo". *Resolução*: `must_fix` (C-3 em SC-12).

**D6 — Consistência interna da evidência de R1-S5 (não é divergência entre assentos)**
R1-S5 afirma que o choque não é previsível (teste F clássico das defasagens 7–12, p=0,90) e diz que esse resultado "só saiu no console". Reexecutei `r1_checks4.py` e obtive F=0,70 com p=0,8965, o que confirma o número. Mas `r1_checks3_output.txt`, salvo pelo próprio R1, mostra o teste HAC-Wald da mesma hipótese (com sazonais e Focus no conjunto de regressores) com **p=0,0000**, e R1 não menciona esse resultado. *Resolução*: S5 procede parcialmente. O resultado depende do tipo de inferência (Wald HAC com cerca de 37 restrições e 6 defasagens, que tende a rejeitar demais em amostra pequena, contra F clássico). Como S5 é um ponto forte e não pesa na decisão, a consequência é só que o autor, se reportar esse diagnóstico, apresente as duas versões (incluído em REV-15).

### 4.2 Verificações factuais

**V1 — R2-W11: a SGS 27574 é o IC-Br em reais, e não em dólares → PROCEDE**
- *Texto do manuscrito*: na Tabela 1, "Índice de Commodities Brasil em USD & BCB / SGS 27574". Na §4.2, item 3, "pelas commodities em dólares ($\ln(ICBr_t)$)". O script `estimacao_svar_lara_resende.py`, linha 80, também diz "em USD".
- *Base usada*: a coluna `ic_br` do CSV é a 27574. Os valores coincidem com a API: 106,82 em 2005-03 e 456,24 em 2026-08.
- *Evidência*: 261 meses (jan/2005–set/2026) da API do SGS.
  - A razão 27574/29042 cresce ×1,9104 e a PTAX média mensal (SGS 3698) cresce ×1,9104.
  - A razão normalizada entre (27574/29042) e a PTAX fica entre 0,9956 e 1,0028 em toda a amostra.
  - A correlação entre Δln(27574) − Δln(29042) e Δln(PTAX) é 1,000.
  - Logo, 27574 ≈ 29042 × PTAX (R$/US$): a 27574 é a versão em reais e a 29042, a versão em dólares. Isso concorda com a descrição pública do IC-Br como "média ponderada de preços, em reais", com variação em dólar calculada à parte ([bpmoney](https://bpmoney.com.br/agro/ic-br-do-bc-avanca-janeiro-2025)).
- *Limite*: o metadado oficial não foi localizado. A classificação se apoia na identidade aritmética, que é decisiva.
- *Alcance* (R2 deixou a consequência para R1, que não tratou do ponto). Reestimei o VAR(6)-base trocando 27574 por 29042, com o resto inalterado:
  - correlação entre os dois choques da Selic: 0,993;
  - inflação de itens livres: h=12 −0,1339 contra −0,1330; h=24 −0,0956 contra −0,0932;
  - J^fam: h=12 +0,3817 contra +0,3721; h=24 +0,1115 contra +0,0939;
  - FEVD da inflação em h=24: commodities 11,85% → 14,49%, câmbio 5,34% → 3,06%;
  - a IRF do próprio ICBr muda muito: h=24 −10,2 contra −3,9.
- *Conclusão*: o erro de rótulo é real e contamina a interpretação do primeiro bloco do ordenamento e as frações da FEVD entre commodities e câmbio (§4.3). Os resultados sobre a Selic, a inflação e J^fam no SVAR mudam pouco. Não reestimei as LPs dependentes de estado. Com choques quase colineares, é plausível que mudem pouco, mas o autor precisa confirmar. A reestimação é obrigatória (REV-29) e barata, mas não deve alterar a decisão.

**V2 — R2-W6: o resultado primário dos ciclos está "invertido" no §1.1 → PROCEDE PARCIALMENTE**
- *Texto exato do manuscrito* (§1.1, último item): no ciclo de ago/2011 a out/2012, "em um contexto de **deterioração progressiva do resultado primário**". No ciclo de out/2016 a mar/2018, "sob ancoragem institucional das expectativas, estabilidade cambial e **contenção fiscal primária**".
- *Dados* (SGS 5793, NFSP primário em 12 meses, % do PIB; valor negativo = superávit):

  | Ponto | Ciclo 1 | Ciclo 2 |
  |---|---|---|
  | Início | ago/2011: superávit de 3,53 | out/2016: déficit de 2,21 |
  | Durante | dez/2011: 2,94 | dez/2016: 2,48; pico de 2,87 em out/2017; dez/2017: 1,68 |
  | Fim do ciclo | out/2012: superávit de 2,07 | mar/2018: déficit de 1,62 |
  | Depois | 2013: 1,71; 2014: déficit de 0,56 | — |

  Os valores anuais de dezembro citados por R2 (2011–2013 e 2016–2018) conferem exatamente.
- *Arbitragem*:
  - Como descrições de **tendência**, as duas expressões do manuscrito estão corretas. Houve deterioração contínua do superávit entre 2011 e 2014. O déficit encolheu cerca de 0,6 p.p. entre o início e o fim do ciclo de 2016–18, embora de forma não monotônica.
  - Em **nível**, R2 está certo: o ciclo de 2011–12 teve superávits de 2–3,5% do PIB e o de 2016–18, déficits de 1,4–2,9%.
  - "Fatos fiscais invertidos" exagera, porque não há erro factual estrito. Mas descrever como "contenção fiscal primária" um período de déficits primários maiores que os de qualquer outro ciclo da amostra, sem dar os níveis, induz o leitor ao erro que R2 aponta. A sugestão de R2 (separar fluxo corrente de expectativas de superávit futuro, como a EC 95) procede.
- *Outros números do mesmo item*:
  - "depreciação cambial superior a 25%": PTAX média de 1,5970 em ago/2011 e 2,0298 em out/2012, +27,1%. **Procede.**
  - "inflação para abaixo de 3,0%": IPCA cheio em 12 meses abaixo de 3% de jun/2017 a mar/2018, com mínimo de 2,46% em ago/2017 (SGS 13522). **Procede.**
- *Consequência para a decisão*: nenhuma isoladamente. A parte de R2-W6 que pesa na decisão (n=2, sem dados, usado como "base" da avaliação da proposta) não depende da caracterização fiscal e é corroborada por EIC-W5/W8 e DA-M7.

**V3 — Outras alegações numéricas usadas na arbitragem**

| Alegação | Assento | Resultado | Evidência |
|---|---|---|---|
| 5,7% (§1) contra 5,3% (§2) | EIC-W8, R2-W2.5, DA-m3 | **Procede** | (12,68 − 7,0)/1,07 = 5,31%; 4,4/82,5 = 5,33%; 5,68 é o diferencial antes da divisão por 1+g |
| Δi de −5,5 p.p. (13,0→7,5) no Bloco II contra "~14% para 7,5%" e "6,5 p.p." na §5.2 | EIC-W5, R2-W2.2 | **Procede** | manuscrito: Bloco II ("de 13,0% para 7,5% a.a.") e §5.2 ("da ordem de 6,5 p.p.") |
| Alívio de 2,27% = 0,50 × 0,825 × 5,5 | R2-W2 | **Procede** (a conta confere; a crítica é à escolha dos insumos) | aritmética |
| Juros nominais NFSP em ago/2026 ≈ 8,9% do PIB | R2-W2.1 | **Procede** | SGS 5727 = 9,48; SGS 5793 = 0,62; diferença = 8,86 |
| Primário de 12 meses em jun/2026 = déficit de 1,19%, fora de "0,4% a 0,7%" | R2 (precisão factual) | **Procede parcialmente** | jun/2026: 1,19, mas dez/2025: 0,43, jul/2026: 0,67 e ago/2026: 0,62 ficam dentro do intervalo. O ponto real é fixar a data de referência |
| O texto usa DBGG de 82,5% "(junho)" | R2 (precisão factual) | **Não procede quanto ao mês** | SGS 13762: jun/2026 81,95; jul/2026 82,55; ago/2026 82,87. Os 82,5% do texto correspondem a julho. Imaterial |
| Composição e custo da DPF (12,63%, 48,3% e 52%, 4,10 anos, 19,95% vincendo em 12 meses) | R2-W2/W3 | **Não verificável nesta síntese** | fonte citada por R2 (RMD de set/2026, via Poder360) não consultada por mim |

**V4 — Verificações por execução de R1, conferidas nos arquivos salvos**
- MDE e IC da diferença (`r1_checks_output.txt` §E), sensibilidade de β_mod^24 a p (`r1_checks2_output.txt` §1), placebo de h=0 (§D), resposta da Selic por regime (§C), EWC (`checks2` §3), bootstrap por blocos e sup-t (§H; `checks2` §4), cinco episódios de platô (§B) e SVAR com sazonais (`checks2` §2): **conferem** com o que R1 relata.
- LP totalmente interagida: **não estava salva**. Reexecutada em cópia, reproduz exatamente o que R1 relata.
- F clássico de previsibilidade: reproduzido (p=0,8965), com a ressalva de D6.
- DA-M3(iii), γ̂¹⁸ com defasagens 7–12: corroborado pela saída de R1 (`checks_output` §F, "+ ambos": h=18 +1,01, p=0,207).

**V5 — Citações do manuscrito decisivas para itens do roteiro**
- R2-W4: o resumo diz "sem elevar o valor presente do passivo público", enquanto a Eq. de V_t(B) atribui D_pre > 0 à fração (1−λ). **Procede.**
- R1-W6: o resumo diz "com dummies sazonais na especificação-base", enquanto o §4.4 diz que a LP linear da Tabela 3 é "sem termos determinísticos sazonais" e o SVAR não as inclui. **Procede.**
- R3-W6: "[Canal de Fragilidade Financeira das Famílias]" aparece em `estimacao_svar_lara_resende.py`, linha 207 (verificado no script; não inspecionei a imagem da figura). **Procede.**
- R1-W11.3 e DA-m8: o §5.3 fala em "quatro grandes ciclos de aperto no platô alto", contra cinco episódios no indicador. **Procede.**
- R1-W2 e DA-M4: a Conclusão, item 2, diz "resultado estável entre especificações". **Procede.**
- R3-W3(a) e DA-m6: o texto diz "não se transmite **de forma significativa**". **Procede parcialmente**: o qualificador já existe, mas a formulação continua afirmando ausência, e a troca sugerida ("não se detecta transmissão significativa") é mais exata.

---

## 5. Adjudicação do Devil's Advocate

`da_critical_adjudications: []`. O DA não registrou achados CRÍTICOS e justificou isso explicitamente: os resultados de cabeçalho estão qualificados o bastante para sobreviver, cada um, a qualquer defeito isolado. Concordo. Nenhum relatório que pontua aponta falha fatal.

| ID | Achado do DA (resumo) | Corroboração | Adjudicação | Resposta exigida do autor |
|---|---|---|---|---|
| M1 | Alívio fiscal nominal × Fisher do próprio modelo | R2-W1 | **Validado.** A álgebra decorre da Eq. (3) do manuscrito: se π e g_nom caem com i, (ī − g_nom) não muda | REV-21 |
| M2 | H1 não é a previsão do ensaio de 2026 | R2-W9, R2-W8 | **Validado parcialmente.** Vale para o ensaio de 2026, o único texto de Lara Resende no pacote. As obras de 2017, 2020 e 2022 não foram verificadas por nenhum assento | REV-27; o autor deve indicar em que obra cada componente de H1 se apoia |
| M3 | γ̂: contagem de votos esconde que a especificação pela taxa real falha; perfil transitório; perda em h=18 com defasagens 7–12 | EIC, R1-W9, R2-W10 (C-3); R1 `checks_output` §F | **Validado.** (iii) foi reproduzido pela saída de R1 | REV-28 |
| M4 | β_mod^24: Holm 0,061, cai à metade com COVID, não significativo com IPCA cheio; Holm aplicado de forma desigual | R1-W2 (sensibilidade a p) | **Validado.** Os números estão nas Tabelas 4 e 5 e foram conferidos | REV-12 |
| M5 | A Selic média mensal faz o "choque" não ser surpresa | R1-W5 | **Validado** | REV-15 |
| M6 | Trajetória da Selic por regime não reportada; normalizar tornaria o platô *mais* potente | R1-W4 | **Validado quanto à omissão; parcial quanto à direção.** Com os números de R1 (`checks_output` §C), a razão β/Selic acumulada é −0,025 no platô contra +0,014 no regime moderado em h=12, mas −0,028 contra −0,054 em h=24. A direção depende do horizonte | REV-14; o autor reporta a normalização sem presumir a direção |
| M7 | Os ciclos 2011–13 × 2016–18 como base da proposta são cherry-picking; os cinco platôs não são descritos | EIC-W5/W8, R2-W6 | **Validado** quanto ao uso como evidência. Os números de inflação por episódio são reanálise do DA e **não foram verificados** por mim | REV-26; REV-38 (`consider`) |
| M8 | O modelo impõe o resultado de platô e não gera restrição testável | EIC-W4 (R2-S4 diverge) | **Validado** (D2) | REV-04, REV-25 |
| M9 | O estado do modelo (λ·b) é diferente do estado empírico (MM12 da Selic) | EIC-W3 | **Validado.** As colunas do CSV não incluem dívida, LFT, resultado nominal nem CDS/EMBI (conferido no cabeçalho do CSV) | REV-03 |
| m1 | "Modelo analítico fechado" | EIC-W4 | Validado | REV-04 |
| m2 | O canal de custos é atribuído ao ensaio de 2026, que não o menciona | — | Achado só do DA, não contestado. Fica para o autor conferir | REV-27 |
| m3 | 5,7% contra 5,3% | EIC-W8, R2 | Validado (V3) | REV-08 |
| m4 | r* e π* do item 3 sem fonte | EIC-W4, R2 | Validado | REV-04 |
| m5 | "alivie expressivamente" | R3-W5 | Validado | REV-05 |
| m6 | "não se transmite" | R3-W3 | Validado parcialmente (V5) | REV-34 |
| m7 | Rolagem de 4–4,5% | R2-W3 | Validado | REV-23 |
| m8 | "quatro grandes ciclos" | R1-W11 | Validado (V5) | REV-20 |

Os caminhos alternativos (Taylor + Fisher, persistência de choques de oferta, homogeneidade com baixo poder, confundidores dos ciclos, alternativas de gestão da dívida, spreads bancários) e as partes interessadas ausentes não exigem resposta item por item. Os três primeiros já estão cobertos por REV-02, REV-28 e REV-14. Os demais ficam como `consider` (REV-39) e perdem relevância se a §5.2 for condensada.

---

## 6. Roteiro de Revisão

**Convenções**
- Os itens estão em **ordem de origem** (EIC → R1 → R2 → R3 → DA e, dentro de cada assento, pela numeração do achado). A ordem não indica prioridade. Itens equivalentes foram fundidos na posição do primeiro assento que os levantou.
- `Obrigação` é o filtro editorial e não indica ordem de trabalho.
- `Custo`: **texto** (só reescrita); **reestimação** (código e dados do pacote); **dados novos** (séries ou fontes que não estão na base, mesmo que públicas).
- `Tipo`: **R** = reescrita; **A** = exige análise nova; **R+A** = ambos.
- As severidades são as dos assentos.

### 6.1 Must fix

| ID | Origem | Severidade | O que fazer | Critério de aceitação verificável | Custo | Tipo |
|---|---|---|---|---|---|---|
| REV-01 | EIC-W1; R2-W7; DA-M2 | Major (EIC, R2); DA Major | Reenquadrar título, resumo e palavras-chave em torno da pergunta e do resultado. Abrir o resumo com a pergunta e o nulo. Tirar o nome próprio das palavras-chave | Título sem "Dívida Pós-Fixada" como objeto testado, salvo se REV-03(b) for feito. A 1ª frase de resultado do resumo trata do nulo de H1. Palavras-chave (PT e EN) sem nome de pessoa | texto | R |
| REV-02 | EIC-W2; R1-W1; (D1) | Major (EIC, R1) | Incluir um parágrafo de contribuição na introdução. Para cada h, reportar β_alto − β_mod com IC 95%, banda simultânea e MDE. Trocar "não encontra apoio" por "inconclusivo", com a magnitude não detectável. Reportar a LP totalmente interagida (ou a de Tenreyro–Thwaites com controles interagidos) e discutir a divergência em h=24 | Uma tabela ou figura com a diferença, IC e MDE em h=3…24. A expressão "não encontra apoio" não aparece mais no resumo, no §4.5 nem na Conclusão. A especificação interagida é reportada com N e número de regressores | reestimação | R+A |
| REV-03 | EIC-W3; R2-W8 (parte); DA-M9 | Major (EIC, R2); DA Major | (a) Mínimo: declarar no resumo, na introdução e na §5 que o canal da dívida pós-fixada não é testado, e apresentar o Bloco II como motivação contábil. (b) Opcional, ver REV-03b em `consider` | O texto contém uma declaração explícita de que λ, a composição da dívida e o prêmio soberano não entram em nenhuma especificação estimada. A frase "a Eq. (dpi_di) sintetiza a dependência de estado testada na Seção 4" é removida ou corrigida | texto | R |
| REV-04 | EIC-W4; DA-M8, m1, m4; R2 (questão menor); (D2) | Major (EIC); DA Major/Minor | Tirar "fechado" do título da §2, da abertura e do resumo. Condensar a §2 em um arcabouço motivador ou calibrar φ, κ, σ, μ e ρ′ com estimativas externas e ligar o resultado a uma predição testável. Documentar com fonte ou remover o item 3 (r*, π*, i*) | "fechado" não aparece no texto. O item 3 tem fonte ou foi removido. Se houver calibração, há uma tabela de parâmetros com fonte e uma predição de sinal ou magnitude confrontada com as LPs | texto (ou reestimação, na calibração) | R (ou R+A) |
| REV-05 | EIC-W5; R2-W6 (parte "base"); R3-W5; DA-M7, m5 | Major (EIC, R2, R3) — C-3 | Reduzir a §5.2 a um parágrafo sobre o que a evidência *não* informa. Retirar o detalhamento do CFMN, das cláusulas de escape e dos efeitos distributivos, ou documentá-los com dados. Retirar "alivie expressivamente". Marcar como hipótese não testada a afirmação sobre poupadores e fundos. Retirar a frase de que a avaliação "apoia-se" na comparação entre ciclos. Harmonizar o cenário (Δi único) | Não há afirmação distributiva sem dado ou sem o rótulo de hipótese. Não aparece "expressivamente". O mesmo Δi aparece no Bloco II, na §5.2 e na Conclusão. O último parágrafo da Conclusão não defende a redução com base na aritmética de equilíbrio parcial | texto | R |
| REV-07 | EIC-W7 | Minor | Anonimizar (nome, afiliação, URL do GitHub, §5.3 item 6) e reescrever as menções à "versão anterior" e à "v2" como especificações alternativas | Uma busca no .tex por "v2", "versão anterior", "github" e o nome do autor não retorna nada na versão anônima | texto | R |
| REV-08 | EIC-W8; EIC-W6 (fatos estilizados); R2-W2.5, R2 (datas); DA-m3 | Minor (EIC-W8); Major (R2-W2, parte-mãe) | Documentar cada número da introdução com fonte primária datada (STN, BCB, FMI). Incluir o Fiscal Monitor nas referências ou removê-lo. Harmonizar 5,7%, 5,3% e >5,5%, dizendo qual é o diferencial e qual é a taxa de crescimento. Fixar a data de referência do primário e da DBGG | Todo número do §1, itens 1–3, tem fonte e data. As três ocorrências da taxa de crescimento da dívida são consistentes e estão definidas. As séries SGS citadas no texto aparecem na Tabela 1 ou em nota | texto | R |
| REV-09 | R2-W8; EIC-W9 | Major (R2); Minor (EIC) | Reescrever a §5.1: corrigir a leitura do ensaio (que adota o canal cambial no curto prazo), usar critérios que de fato separam as teorias (primário × nível do juro, prêmio soberano, fatia de dívida cambial) e declarar que o desenho atual não discrimina entre elas. Levar a Tabela 6 para a §4 e renomear a seção pelos canais, não pelos autores | O título da seção não promete discriminação. O texto não atribui ao ensaio a exclusão do canal cambial. Há uma frase explícita de não discriminação | texto | R |
| REV-12 | R1-W2; DA-M4 | Major (R1); DA Major | Incluir na Tabela 5 a sensibilidade de β_mod^24, β_alto^24, γ¹² e J^fam a p ∈ {2, 4, 6, 9, 12}. Rebaixar a implicação (i) de H1 para "sugestiva e não robusta" no resumo e na Conclusão. Retirar "estável entre especificações". Aplicar Holm de forma consistente a todos os coeficientes de cabeçalho. Considerar LP com lag augmentation | Há uma linha ou painel de sensibilidade a p. A Conclusão, item 2, não contém "estável entre especificações". O resumo não afirma efeito desinflacionário sem informar p_Holm e a sensibilidade | reestimação | R+A |
| REV-13 | R1-W3, R1-W12; DA-M4 (Holm); (D3) | Major (R1-W3); Minor (R1-W12) | Adotar ou acrescentar inferência robusta (EWC/fixed-b, ou lag augmentation com EHW). Incluir bandas sup-t na Figura 5. Fazer um bootstrap que reestime VAR e choque a cada réplica. Informar episódios e observações por regime e por h. Declarar quais testes são confirmatórios | As Tabelas 4 e 5 trazem p-valores EWC (ou equivalentes) ao lado dos NW. A Figura 5 tem banda simultânea. Há uma tabela de episódios (cinco) com N por regime e h. Há uma lista de testes confirmatórios. As conclusões sobre γ¹² e β_mod^24 são condicionadas a essa inferência | reestimação | R+A |
| REV-14 | R1-W4; DA-M6 | Major (R1); DA Major | Reportar a resposta da Selic por regime ("primeiro estágio"). Normalizar a inflação pela Selic acumulada em cada regime (razão de integrais ou LP-IV). Tratar o placebo da PTAX em h=0 como diagnóstico da identificação, não como fato econômico. Opcional: identificação dependente de estado (ver REV-14b em `consider`) | Há uma tabela ou figura da Selic por regime. Há uma comparação normalizada entre regimes, com a direção reportada sem presunção. O texto da Tabela 6 em h=0 não interpreta a apreciação no platô como resultado | reestimação | R+A |
| REV-15 | R1-W5; DA-M5; (D6) | Major (R1); DA Major | Reestimar ao menos uma alternativa de menor custo: meta Selic de fim de mês (SGS 432) ou Selic do último dia útil, ou amostra por reunião do Copom, para as LPs lineares, de estado e H2. Qualificar ou retirar "não antecipado" no resumo. Se o diagnóstico de previsibilidade do choque for reportado, apresentar o F clássico e o Wald HAC | Há uma especificação adicional na Tabela 5 (ou em apêndice) com a SGS 432 ou equivalente. O resumo não usa "não antecipado" sem qualificação | dados novos (série pública) + reestimação | A |
| REV-16 | R1-W6 | Major | Tornar padrão o SVAR com dummies sazonais exógenas. Reapresentar a Tabela 2, as Figuras 2 e 3 e a §4.2, item 3. Manter a versão sem dummies como robustez. Reportar os testes de autocorrelação residual. Corrigir no resumo a afirmação sobre a "especificação-base" | A Tabela 2 vem da especificação com sazonais. A narrativa do price puzzle em h=5–6 e da reversão em h=12 é reescrita de acordo. O resumo distingue as especificações-base do SVAR e das LPs | reestimação | R+A |
| REV-20 | R1-W11; DA-m8 | Minor | Corrigir +0,357 para o valor reestimado em h=5. Trocar "abaixo de 0,01" por "≤ 0,010". Trocar "quatro grandes ciclos" por cinco episódios, com lista. Declarar a convenção de horizonte da FEVD | Os números do texto conferem com `resultados/`. O §5.3 lista os episódios | texto | R |
| REV-21 | R2-W1; DA-M1 | Major (R2); DA Major | Reescrever o Bloco II em termos reais. Decompor Δb em queda do juro real e queda de π e g_nom. Apresentar ao menos dois cenários (inflação rígida no 1º ano; ajuste fisheriano pleno). Retirar do resumo e da Conclusão o número de 2,3% do PIB como alívio sem qualificação | Há uma tabela ou equação com os dois cenários e o efeito sobre a **razão** b. Os 2,3% só aparecem condicionados a um cenário explícito | texto (com cálculo simples) | R+A |
| REV-22 | R2-W2; EIC-W5 (parte) | Major | Incluir uma tabela de insumos fiscais com fonte, data e conceito (DBGG 13762, DLSP 4513, NFSP 5727/5793, RMD). Usar a base líquida e as NFSP para fluxos e a DBGG para estoques. Distinguir a Selic (LFT e compromissadas) do custo médio. Fazer o alívio seguir a trajetória gradual da proposta. Apresentar uma grade de sensibilidade em λ, Δi e base | A tabela de insumos existe. Cada número do Bloco II remete a uma linha dela. Há uma grade de sensibilidade com ao menos λ × Δi | dados novos (públicos) | R+A |
| REV-23 | R2-W3; DA-m7; (D5) | Major (R2); DA Minor | Declarar que 4,0–4,5% é limite superior, condicional a prêmio a termo nulo e rolagem integral (o cenário detalhado está em REV-23b, `should_fix`) | O texto e o resumo qualificam os 4% como limite superior condicional | texto | R |
| REV-24 | R2-W4 | Major | Substituir "sem elevar o valor presente do passivo" por "elevando apenas a parcela de duration positiva (≈ metade do estoque)", no resumo (PT e EN) e no §1, item 3 | Nenhuma ocorrência de "sem elevar o valor presente" ou "without raising the market present value". O texto é coerente com a Eq. de V_t(B) | texto | R |
| REV-26 | R2-W6; EIC-W5/W8; DA-M7; (V2) | Major (R2) | Corrigir a caracterização fiscal dos ciclos, dando os níveis do primário (superávit em 2011–12, déficit em 2016–18) ao lado da tendência e separando fluxo corrente de expectativas (EC 95). Ou reduzir a comparação a uma ilustração narrativa declarada, ou transformá-la num estudo de caso com dados (Focus, primário, hiato, câmbio, alimentos, juro real ex ante) | Os níveis do primário dos dois ciclos estão no texto ou numa tabela com fonte. A comparação não é usada como base de avaliação da proposta | texto (ou dados novos, no estudo de caso) | R (ou R+A) |
| REV-27 | R2-W9; DA-M2, m2 | Major (R2); DA Major/Minor | Declarar quais componentes da tese cada hipótese testa. Reconhecer explicitamente que a dimensão neo-fisheriana (mudanças permanentes) não é testada por surpresas transitórias, ou acrescentar uma decomposição permanente × transitória no espírito de Uribe (2022). Conferir a atribuição do canal de custos ao ensaio de 2026 | Há uma tabela ou parágrafo "componente da tese × hipótese × testado/não testado". As citações dos canais remetem à obra em que cada um aparece | texto (ou reestimação, na decomposição) | R (ou R+A) |
| REV-28 | R2-W10; R1-W9 (parte); EIC (Relevância); DA-M3 — C-3 | Minor (R1, R2); DA Major | Apresentar γ̂ como associação descritiva, compatível com Fisher e com a regra de reação. Não usar contagem de votos ("sete de oito"). Destacar que a especificação pelo juro real ex ante, a mais próxima da tese, não é significativa. Rever "resultado mais estável do artigo" | O resumo e a Conclusão não usam "compatível com a hipótese de Lara Resende" sem mencionar a especificação 5. "Mais estável" está qualificado ou foi removido | texto | R |
| REV-29 | R2-W11; (V1) | Major | Corrigir o rótulo da SGS 27574 (IC-Br em R$). Reestimar com a SGS 29042 (USD) como especificação-base, ou manter a 27574 com o rótulo correto e justificar o ordenamento antes da PTAX. Rever a §4.3 (FEVD commodities × câmbio) e a §4.2, item 3 ("commodities em dólares") | A Tabela 1 e o script rotulam corretamente. Se a 29042 for adotada, as Tabelas 2–6 e a FEVD são reestimadas e a mudança é reportada. Nenhuma ocorrência de "em dólares" ligada à 27574 | reestimação (série 29042 é pública) | A |
| REV-32 | R3-W1; R1 (safra) | Major | Documentar a construção de 29033 e 29034 (estimativa do BCB, RNDBF restrita mensalizada por Denton-Cholette, média móvel trimestral, retropolação pré-2012; NT 55 e nota de 28/12/2021). Informar a safra de extração. Reestimar H2 com dados trimestrais não sobrepostos ou com erros-padrão que tratem a estrutura MA(2). Discutir h=0 à luz da média móvel | Há um apêndice ou parágrafo de construção com as referências do BCB e a data de extração. Há uma especificação robusta à MA(2) reportada | reestimação | R+A |
| REV-33 | R3-W2; EIC-W2 (H2 quase mecânico) | Major | Com o mesmo choque, estimar LPs para J, A (29036), S (29034), E (29037) e J/E. Reportar H2 com controle pelo estoque | Há uma tabela única de decomposição taxa × estoque. H2 é reportada também com defasagens de 29037 | dados novos (29036 pública) + reestimação | A |
| REV-34 | R3-W3; DA-m6; (D5, V5) | Major (R3); DA Minor | Usar o mesmo choque-base para todas as séries de comprometimento. Estimar a resposta da amortização. Testar a diferença J − S. Trocar a formulação por "não se detecta transmissão significativa" e discutir os mecanismos alternativos (anuidade, alongamento, desalavancagem) | O Apêndice A usa o choque da especificação-base. Há um teste J − S reportado. A formulação é corrigida no resumo, na §4.2, na Limitação 5 e na Conclusão | reestimação | R+A |

### 6.2 Should fix

| ID | Origem | Severidade | O que fazer | Critério de aceitação verificável | Custo | Tipo |
|---|---|---|---|---|---|---|
| REV-06 | EIC-W6; R2-W13; R2-W7 (parte); R3 (leituras) | Major (EIC); Minor (R2-W13); (D5) | Reorganizar a introdução em torno da pergunta científica. Incorporar a literatura revisada por pares de LPs dependentes de estado, os fundamentos da TFNP (Sargent–Wallace, Leeper, Sims, Woodford), a transmissão e a dominância fiscal no Brasil (Minella; Tanner–Ramos; Ayres et al.), a evidência contrária a ABL (Gonçalves–Holland–Spacov) e a literatura de finanças das famílias (Drehmann–Juselius; Cloyne et al.; Auclert). Usar os blogs só como referência secundária | Os blogs e o ensaio não sustentam nenhuma afirmação factual. A evidência contrária a ABL é discutida onde ABL fundamenta r* | texto | R |
| REV-10 | EIC-W10 | Minor | Reduzir o resumo para no máximo 250 palavras | Contagem ≤ 250 (PT e EN) | texto | R |
| REV-11 | EIC-W11; R1-W8; R3-W7; DA-m5 — C-3 | Minor | Usar 1 DP (ou 25 pb) como unidade principal no resumo, na Conclusão e nas Tabelas 4–6. Reportar J^fam por DP e por p.p. de Selic acumulada. Manter +1 p.p. só na comparação com o SVAR | O resumo e a Conclusão apresentam primeiro os efeitos por DP. A Tabela 3 tem uma conversão para J^fam | texto (com conversão trivial) | R |
| REV-17 | R1-W7; (D4) | Minor | Declarar que a igualdade LP–SVAR em h=0 vale por construção. Tirar da família de Holm os horizontes nulos por construção. Trocar "forte aderência" pela descrição das divergências | O texto não usa "forte aderência". Holm é recalculado sem h=0 nulo | texto (+ recálculo) | R |
| REV-18 | R1-W9; DA ("premissa não examinada") | Minor | Mostrar γ^h e β^h ao longo de uma grade de limiares (9%–14%) com bandas. Fazer o teste sup-Wald com bootstrap. Acrescentar um indicador de estado que não dependa da Selic | Há uma figura da grade de limiares. O p-valor sup-Wald é reportado | reestimação | A |
| REV-19 | R1-W10 | Minor | Usar bandas do SVAR por bootstrap com correção de viés (Kilian, 1998). Tirar o negrito das respostas no limite | A Tabela 2 traz intervalos bootstrap. O negrito segue esse critério | reestimação | A |
| REV-23b | R2-W3 | Major | Simular a rolagem com o cronograma efetivo de vencimentos e cenários de prêmio a termo e juro real longo | Há uma tabela de cenários com fonte do cronograma | dados novos | A |
| REV-25 | R2-W5; DA-M8(i) | Minor (R2); DA Major | Renomear o canal da Eq. de expectativas como "solvência fiscal e prêmio de risco" e reservar "TFNP" para a equação de valoração, ou escrevê-la | A sigla TFNP não rotula a Eq. de expectativas sem equação de valoração | texto | R |
| REV-30 | R2-W12 | Minor | Citar Cochrane (2026) só pelo que os posts dizem, com URL completo de cada post. Atribuir a Lara Resende as proposições sobre o Brasil | O .bib tem os URLs completos. Nenhuma tese sobre a Selic é atribuída a Cochrane sem citação literal | texto | R |
| REV-31 | EIC (questões menores); R2 (questões menores) | — (abaixo do limiar de achado) | Remover ou citar `serrano2010juros` e `resende2014limites`. Conferir `pastore1996reforma` (ano e conteúdo) e `resende1980causas`. Preferir as versões publicadas de Blanchard (2004) e Favero–Giavazzi (2004). Tratar o sobrenome {Lara Resende}. Fixar `\date`. Tirar a linha do IPCA monitorado da Tabela 1 ou fazer a análise. Corrigir o cabeçalho da Tabela 3. Reduzir o negrito. Uniformizar "platô" e "patamar". Corrigir as imprecisões sobre Uribe (2022) e García-Schmidt–Woodford (2019) | Não há entrada do .bib sem citação. As chaves conferem com ano e conteúdo. `\date` é fixa | texto | R |
| REV-35 | R3-W4 | Minor | Corrigir a descrição de η_pos (estoque × concessões, tetos do rotativo e do cheque especial, TR no imobiliário — pontos que R3 marcou "a confirmar"). Reestimar H2 com 29035 (sem habitacional) | O Bloco III não classifica concessões como fração do estoque. Há uma especificação com 29035 reportada | dados novos (pública) + reestimação | R+A |
| REV-36 | R3-W6 | Minor | Trocar o subtítulo do painel (b) da Figura 2 por "Comprometimento de renda com juros (SGS 29033)" | A figura e o script não contêm "Fragilidade" | texto (regerar figura) | R |

### 6.3 Consider

| ID | Origem | Severidade | O que fazer | Critério de aceitação verificável | Custo | Tipo |
|---|---|---|---|---|---|---|
| REV-03b | EIC-W3(b); R2-W8 | Major (EIC) | Levar o canal da dívida para a evidência: interagir o choque com a participação de pós-fixados (se ela variou), ou incluir custo nominal da dívida ou CDS/EMBI | Há uma especificação estimada com uma variável fiscal ou de risco soberano | dados novos | A |
| REV-14b | R1-W4 | Major | Identificar o choque com um VAR de limiar ou de transição suave, ou estimar a LP recursiva por regime com controles contemporâneos interagidos | Há uma especificação alternativa reportada | reestimação | A |
| REV-15b | R1-W5 | Major | Usar surpresas de alta frequência em futuros de DI como instrumento externo (LP-IV) | Há uma LP-IV reportada | dados novos | A |
| REV-37 | R3-W7 | Minor | Comparar com o episódio de 2021–2023. Mencionar a heterogeneidade (endividados de risco, microdados do SCR) como passo seguinte | Uma frase ou parágrafo com a comparação e a referência ao Estudo Especial 80 | texto | R |
| REV-38 | DA (contra-argumento, M7-iii) | Major (M7) | Incluir uma tabela descritiva dos cinco episódios de platô com a trajetória da inflação de itens livres em 12 meses. Os números do DA não foram verificados nesta síntese | Há uma tabela com fonte e datas dos episódios | reestimação (dados do pacote) | A |
| REV-39 | DA (caminhos alternativos 5; partes interessadas) | — | Se a §5.2 for mantida em alguma forma, mencionar as alternativas de gestão da dívida e as partes interessadas ausentes | Uma menção explícita ou a justificativa de omissão | texto | R |

### 6.4 Reescrita × nova análise

| Natureza | Itens |
|---|---|
| **Só reescrita** (texto, sem reestimar) | REV-01, 03, 05, 07, 08, 09, 20, 23, 24, 28; should: REV-06, 10, 11, 17, 25, 30, 31, 36; consider: REV-37, 39. REV-04, 26 e 27 também, na opção mínima |
| **Reestimação com dados e código do pacote** | REV-02, 12, 13, 14, 16, 32, 34; should: REV-18, 19; consider: REV-14b, 38 |
| **Dados novos** (séries públicas fora da base ou fontes externas) | REV-15 (SGS 432), 22 (DBGG, DLSP, NFSP, RMD), 29 (SGS 29042), 33 (SGS 29036); should: REV-23b, 35 (SGS 29035); consider: REV-03b, 15b |
| **Cálculo analítico novo, sem dados novos** | REV-21; REV-04 e REV-27 nas opções mais custosas |

### 6.5 Lista de rastreabilidade (ordem de origem)

- [ ] REV-01 — `must_fix` — reenquadrar título, resumo e palavras-chave (EIC-W1; R2-W7; DA-M2)
- [ ] REV-02 — `must_fix` — contribuição e nulo informativo com IC/MDE; LP interagida (EIC-W2; R1-W1)
- [ ] REV-03 — `must_fix` — declarar que o canal da dívida pós-fixada não é testado (EIC-W3; R2-W8; DA-M9)
- [ ] REV-03b — `consider` — trazer o canal fiscal para a evidência (EIC-W3b)
- [ ] REV-04 — `must_fix` — tirar "fechado"; condensar ou calibrar a §2; dar fonte ao item 3 (EIC-W4; DA-M8, m1, m4)
- [ ] REV-05 — `must_fix` — reduzir a §5.2 e harmonizar o cenário (EIC-W5; R2-W6; R3-W5; DA-M7, m5)
- [ ] REV-06 — `should_fix` — reposicionar a literatura (EIC-W6; R2-W13)
- [ ] REV-07 — `must_fix` — anonimização (EIC-W7)
- [ ] REV-08 — `must_fix` — fontes e harmonização dos números da introdução (EIC-W8; R2; DA-m3)
- [ ] REV-09 — `must_fix` — reescrever a §5.1 (R2-W8; EIC-W9)
- [ ] REV-10 — `should_fix` — resumo ≤ 250 palavras (EIC-W10)
- [ ] REV-11 — `should_fix` — 1 DP como unidade principal (EIC-W11; R1-W8; R3-W7)
- [ ] REV-12 — `must_fix` — sensibilidade de β_mod^24 a p; Holm consistente (R1-W2; DA-M4)
- [ ] REV-13 — `must_fix` — inferência robusta, sup-t, episódios, testes confirmatórios (R1-W3, W12)
- [ ] REV-14 — `must_fix` — Selic por regime e normalização; placebo de h=0 como diagnóstico (R1-W4; DA-M6)
- [ ] REV-14b — `consider` — identificação dependente de estado (R1-W4)
- [ ] REV-15 — `must_fix` — alternativa de menor custo à Selic média (R1-W5; DA-M5)
- [ ] REV-15b — `consider` — HFI/LP-IV (R1-W5)
- [ ] REV-16 — `must_fix` — SVAR com sazonais como base (R1-W6)
- [ ] REV-17 — `should_fix` — equivalência em h=0 por construção (R1-W7)
- [ ] REV-18 — `should_fix` — grade de limiares e sup-Wald (R1-W9)
- [ ] REV-19 — `should_fix` — bootstrap com correção de viés (R1-W10)
- [ ] REV-20 — `must_fix` — inconsistências numéricas (R1-W11; DA-m8)
- [ ] REV-21 — `must_fix` — aritmética fiscal em termos reais, dois cenários (R2-W1; DA-M1)
- [ ] REV-22 — `must_fix` — tabela de insumos fiscais e bases coerentes (R2-W2)
- [ ] REV-23 — `must_fix` — 4% como limite superior condicional (R2-W3; DA-m7)
- [ ] REV-23b — `should_fix` — cenários de rolagem (R2-W3)
- [ ] REV-24 — `must_fix` — corrigir "sem elevar o valor presente" (R2-W4)
- [ ] REV-25 — `should_fix` — rótulo TFNP (R2-W5; DA-M8)
- [ ] REV-26 — `must_fix` — ciclos: níveis do primário e uso como evidência (R2-W6; EIC; DA-M7)
- [ ] REV-27 — `must_fix` — componentes da tese testados × não testados (R2-W9; DA-M2, m2)
- [ ] REV-28 — `must_fix` — enquadramento do γ̂ (R2-W10; R1-W9; EIC; DA-M3)
- [ ] REV-29 — `must_fix` — IC-Br em R$: rótulo e reestimação (R2-W11)
- [ ] REV-30 — `should_fix` — atribuição a Cochrane (R2-W12)
- [ ] REV-31 — `should_fix` — bibliografia e questões editoriais menores (EIC; R2)
- [ ] REV-32 — `must_fix` — documentação e safra de 29033/29034; robustez à MA(2) (R3-W1; R1)
- [ ] REV-33 — `must_fix` — decomposição taxa × estoque (R3-W2)
- [ ] REV-34 — `must_fix` — mesmo choque no serviço total; teste J − S; formulação (R3-W3; DA-m6)
- [ ] REV-35 — `should_fix` — η_pos e 29035 (R3-W4)
- [ ] REV-36 — `should_fix` — rótulo da Figura 2 (R3-W6)
- [ ] REV-37 — `consider` — magnitude e heterogeneidade das famílias (R3-W7)
- [ ] REV-38 — `consider` — tabela dos cinco episódios de platô (DA)
- [ ] REV-39 — `consider` — caminhos alternativos e partes interessadas (DA)

(Os IDs REV-06 e REV-10/11 ficam entre itens `must_fix` porque a ordem é a de origem. A numeração não é um ranking.)

**Carta de resposta.** Responder item por item (`templates/revision_response_template.md`), com marcação das alterações e uma tabela de correspondência de páginas. Um item recusado deve vir com justificativa. A recusa fica registrada como não resolvida e não é tratada como aceita.

**Prazo do periódico**: `NOT PROVIDED`.

---

## 7. Méritos reconhecidos

Todos os méritos abaixo foram registrados pelos próprios assentos. Nenhum foi acrescentado para suavizar a decisão.

- **Relato franco dos nulos e das fragilidades** (EIC-S1, R1-S2, R2-S1, DA "pontos fortes"). O artigo declara que H1 não tem apoio, descarta como artefato sazonal o resultado positivo da versão anterior e qualifica γ̂ pela causalidade reversa. Todos os assentos tratam isso como o principal ativo do manuscrito reposicionado.
- **Reprodutibilidade computacional exata** (R1-S1, EIC-S7, DA). Os três scripts de LP reproduzem os arquivos de `resultados/` byte a byte a partir do CSV, e o DA reproduziu os coeficientes-base de forma independente.
- **H2 robusto** (R1-S3, R3-S3). O efeito sobre J^fam resiste a p ∈ {2,…,12}, à inferência EWC, à LP recursiva, ao SVAR com sazonais, ao controle pelo estoque, à dummy de COVID e à amostra até 2019 (as checagens de R3 são exploratórias e não foram reproduzidas nesta síntese).
- **Bateria de robustez que inclui o resultado desfavorável** (EIC-S2, R1-S4). A especificação pelo juro real ex ante é reportada e incorporada à interpretação.
- **Hipóteses ligadas a coeficientes e testes** (EIC-S3, R1-S6). A implicação (iii), β_alto > β_mod testada por Wald, é a forma correta de separar dependência de estado de imprecisão. O artigo evita a falácia da "diferença de significâncias" (DA).
- **Separação entre evidência e proposta de política na Conclusão** (EIC-S4, R2-S2, R3-S4), incluindo a crítica de Lucas e o caráter marginal das surpresas.
- **Decomposição juros × serviço total** (EIC-S6, R3-S2). A série só de juros é reportada junto com a de serviço total.
- **Genealogia correta da tese** (R2-S3): Loyo (1999), Blanchard (2004) e Favero–Giavazzi (2004).
- **Teste direto do canal cambial por regime** (R2-S5), com a ressalva de D2 e REV-09 sobre a leitura dessa evidência como discriminante.
- **Tema relevante para a região** (EIC-S5).

---

*Os cinco relatórios completos ficam em `revisao_independente/relatorios/` como anexo deste documento.*
