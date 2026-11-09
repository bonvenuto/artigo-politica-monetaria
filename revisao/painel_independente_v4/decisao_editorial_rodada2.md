# Decisão Editorial e Roteiro de Revisão — 2ª rodada (re-revisão)

**Manuscrito**: "O Patamar dos Juros Altera a Transmissão da Política Monetária? Evidência de Projeções Locais Dependentes de Estado e do Comprometimento de Renda das Famílias no Brasil (2005–2026)"
**Data da decisão**: 9 de novembro de 2026
**Rodada**: 2ª rodada deste painel simulado (re-revisão da versão que respondeu ao Roteiro REV-01…REV-39)
**Papel**: `editorial_synthesizer`. Este documento consolida e arbitra. Não acrescenta críticas próprias: toda crítica abaixo remete a um ID de relatório (EIC2-n, R1b-n, R2b-n, R3b-n, DA2-n). As conferências feitas pelo sintetizador (Seção 1.4) servem só para arbitrar alegações em disputa.

`calibration_status: NOT_CALIBRATED`
`criteria_binding_unavailable`: não há periódico-alvo confirmado. Nenhum juízo abaixo afirma adequação a um periódico específico.

---

## 1. Proveniência e limites

### 1.1 Painel

| Assento | Papel | Relatório | Recomendação | Confiança (autodeclarada) |
|---|---|---|---|---|
| EIC | Journal-Fit Reviewer | `relatorios/eic_rodada2.md` | Minor Revision | 4 |
| R1 | Metodologia (SVAR/LP, inferência) | `relatorios/r1_metodologia_rodada2.md` | Minor Revision | 4 |
| R2 | Domínio (política monetária e fiscal, TFNP) | `relatorios/r2_dominio_rodada2.md` | Minor Revision | 4 |
| R3 | Perspectiva (finanças das famílias) | `relatorios/r3_perspectiva_rodada2.md` | Minor Revision (com reanálise localizada) | 4 |
| DA | Devil's Advocate | `relatorios/devils_advocate_rodada2.md` | não vota; nenhum achado CRÍTICO; 4 MAIOR, 4 MENOR | por achado |

Li os cinco relatórios por inteiro e a decisão da 1ª rodada (`rodada1/decisao_editorial.md`), cujo formato e régua sigo. A confiança declarada é só informação de escopo: não serviu como peso nem como critério de desempate.

### 1.2 Como os relatórios foram produzidos

- Os cinco assentos são **o mesmo modelo**, em contextos separados, cada um com pacote próprio. Nenhum teve acesso aos relatórios dos pares.
- **Não houve carta de resposta do autor.** Cada assento verificou o Roteiro da 1ª rodada diretamente no manuscrito, nos scripts e nas saídas.
- **Reanálises.** R1 reproduziu os seis arquivos de `resultados/` byte a byte, sem rede. R1 e o DA calibraram por conta própria a LP totalmente interagida sob a nula de linearidade: R1 obteve p ≈ 0,090–0,097 (wild/iid, B = 299) e o DA, p = 0,085 (B = 399). Os dois usaram o **mesmo DGP** do script do autor (`inferencia_regimes.py`, §D), de modo que não são medições independentes; a concordância confirma que a conta é reproduzível, não que esteja certa por dois caminhos. R3 fez reanálises exploratórias do bloco das famílias (defasagens próprias, fases trimestrais, SGS 432). R2 consultou fontes externas (API SGS 5793; RMD de set./2026 via imprensa).
- **Erro correlacionado.** Concordância entre assentos indica que papéis diferentes chegaram ao mesmo ponto (cobertura de papéis), e não votos independentes. Um viés do modelo pode se repetir em todos os assentos.

### 1.3 O que não foi executado

Não houve sprint contract, sidecars JSON (`revision-roadmap/1.0`), scripts de checagem automáticos (`check_re_review_synthesis.py` etc.), checkpoint cross-model nem verificação bibliográfica automática. As referências sugeridas por R2 e R3 seguem como estão nos relatórios. Não reexecutei os scripts do autor nem as reanálises dos assentos.

### 1.4 Conferências feitas pelo sintetizador (só para arbitrar)

Todas feitas sobre o pacote `manuscrito/`, sem acesso externo:
- **.tex**: l. 46 (resumo), 49 (palavras-chave), 73 e 75 (contribuições e resultados), 109–116 (Tabela 1), 149, 190–214 (§2.2 e Tabelas de insumos e cenários), 279 (§3.2, "reestimamos tudo"), 309 (testes confirmatórios), 432, 439, 468, 472, 483, 545–546, 575, 612, 627–631.
- **Resultados**: `aritmetica_fiscal.txt`, `inferencia_regimes.txt` (§A–H), `canal_familias.txt`.
- **Scripts**: chamadas a `meta_selic` (só em `estimacao_regime_juros_altos.py`, l. 136), rótulos de versão nos scripts e saídas, `qmask` em `canal_familias.py`, reamostragem iid em `inferencia_regimes.py` (l. 167).
- **Ensaio** (`ensaio_eu_acuso.pdf`, extraído com `pdftotext`): passagens das p. 6–11 citadas por R2b-1, R2b-3 e DA2-4.
- **Aritmética**: 82,87 × (12,63 − 7,5)/107,22 = 3,96; 82,87 × 6,44/107,22 = 4,98; termo dos indexados com x_IPCA = 23,59% × (9.382,95/13.402) = 16,5% do PIB; ω* = x(1+g)/[b(1+ī)] = 0,41 (x = 36,1) e 0,49 (x = 42,8); Holm dos p-valores de simetria de H2 (mínimo 0,057 × 6 = 0,342).

---

## 2. Decisão e justificativa

### Decisão: **Minor Revision**

| Assento | Recomendação | Confiança |
|---|---|---|
| EIC | Minor | 4 |
| R1 | Minor | 4 |
| R2 | Minor | 4 |
| R3 | Minor (com reanálise localizada; passaria a Major se a assimetria de H2 for mantida como afirmação sobre cortes) | 4 |
| DA | não vota; `da_critical_adjudications: []` | — |

Pela matriz (Minor/Minor/Minor/Minor, sem achado CRÍTICO do DA), a decisão é Minor Revision. As arbitragens abaixo não dão razão para afastar-se dela.

**Por que não Accept.** Restam problemas novos de severidade maior que tocam alegações de cabeçalho:
- **A única rejeição forte sobre H1 não está calibrada.** A LP totalmente interagida (Wald p = 0,001) não passou pelo bootstrap sob a nula que o artigo usa para rebaixar γ̂. Calibrada por R1 e pelo DA (mesmo DGP), fica em p ≈ 0,09 (R1b-1, DA2-2).
- **A descrição da grade de limiares é seletiva** (EIC2-2, R1b-3, DA2-2).
- **A §2.2 erra a aritmética e a leitura do ensaio.** Atribui à tese um ω ≈ 1 que o ensaio não sustenta (R2b-1, DA2-4), trata os títulos indexados como prefixados (R2b-2, DA2-4) e superestima o limite superior (R2b-3).
- **No bloco das famílias**, a "desalavancagem" e a "assimetria" dependem de escolhas frágeis, e a "taxa efetiva" pode refletir o método de estimação do BCB (R3b-1 a R3b-3, R1b-7, DA2-3, DA2-7).
- **O rótulo "nulo informativo" contradiz o próprio texto** (EIC2-1, DA2-1).
- **A anonimização foi preparada, mas não executada** (EIC2-5).

**Por que não Major.** Os bloqueantes B1–B3 da 1ª rodada estão resolvidos segundo os quatro assentos que pontuam. Nenhum item do Roteiro piorou. Nenhum problema novo derruba a conclusão central ("H1 inconclusiva; H2 positiva na taxa implícita"). R1, o DA e R2 afirmam explicitamente que as correções reforçam ou matizam essa conclusão, sem invertê-la.
- Todos os `must_fix` abaixo se resolvem com reescrita ou com reestimação usando código e dados do pacote. Os itens que pedem dados novos (RR2-12 em parte, RR2-32, RR2-13, RR2-26) são `should_fix` ou `consider`.
- R1 e R2 dizem não ver necessidade de nova rodada completa se os itens forem conferidos pelo editor.

**Condição registrada.** R3 declara que passaria a recomendar Major se a assimetria de H2 for mantida na §5.2 e na Conclusão como afirmação sobre cortes de juros (R3, "Recomendação"). O autor deve ler isso como condição desta decisão (RR2-29).

---

## 3. Status consolidado do Roteiro da 1ª rodada

Legenda: **R** = resolvido; **P** = parcial; **N** = não feito; **N (ac.)** = não feito, aceitável para `consider`. "Breve" indica que o assento verificou só existência e coerência. Quando os assentos discordam, a arbitragem está na observação.

| REV | Classe r1 | Status consolidado | Assentos | Observação |
|---|---|---|---|---|
| REV-01 | must | **R** | EIC R; R2 R; DA (M2) R | Resíduo: palavra-chave "dominância fiscal" (EIC2-6 → RR2-03) |
| REV-02 | must | **P** | EIC R; R1 P; DA (D1) — | **Arbitragem**: prevalece R1. A tabela `tab:nulo`, o MDE e a LP interagida existem (critério literal atendido), mas a LP interagida, apresentada no resumo como "significativa", não foi calibrada pela régua que o próprio artigo adota (conferido: §D de `inferencia_regimes.txt` só lista estatísticas da base). Falta também a banda simultânea da diferença. → RR2-01, RR2-17, RR2-21 |
| REV-03 | must | **R** | EIC R; R2 R; DA (M9) R | l. 149 conferida |
| REV-03b | consider | N (ac.) | EIC; R2 | Declarado como extensão |
| REV-04 | must | **R** | EIC R; R2 R; DA (M8, m1, m4) R | — |
| REV-05 | must | **R**, com problema novo | EIC R; R2 R; R3 R | A §5.2 ganhou a frase sobre assimetria em cortes (R3b-2 → RR2-29) |
| REV-06 | should | **P** (aceitável) | EIC R com ressalva; R2 P; R3 P | Lacunas não bloqueantes → RR2-06 (`consider`) |
| REV-07 | must | **P** | EIC P; R1 (R1b-8) e R2 (R2b-7) registram | Chave `\anonimotrue` existe, mas o PDF está com `\anonimofalse`; rótulos "VERSÃO 4", "versão 3" e "Base v3" no pacote (conferido) → RR2-36 |
| REV-08 | must | **R** | EIC R; R2 R (números conferidos contra RMD e SGS) | — |
| REV-09 | must | **R** | EIC R/P (subitem cosmético); R2 R | A Tabela de câmbio continuar na §5.1 é cosmético; não gera item |
| REV-10 | should | **R** | EIC R (249/228 palavras) | — |
| REV-11 | should | **P** (aceitável) | EIC P; R1 R/P; R3 P | Tabelas 5–6 em +1 p.p. com fator na legenda (aceito). Resíduo de R3 → RR2-35 |
| REV-12 | must | **R** | EIC R; R1 R; DA (M4) R | R1 recalculou Holm (0,073) e rodou lag augmentation (−1,97, p = 0,087) |
| REV-13 | must | **P** | EIC R (breve); R1 P | **Arbitragem**: prevalece R1 (inferência é o foco dele). O critério pedia EWC nas "Tabelas 4 e 5", e a Tabela 5 não tem; o N por regime só está em `resultados/` (conferido em §F) → RR2-23 |
| REV-14 | must | **R** | EIC R; R1 R; DA (M6) R | — |
| REV-14b | consider | N (ac.) | R1 | Limitação 1 |
| REV-15 | must | **P** | EIC R (breve); R1 P; R3 P; DA (M5) "resolvido como divulgação" | **Arbitragem**: prevalecem R1 e R3. O texto diz "reestimamos tudo com a meta Selic" (l. 279), mas `meta_selic` só é usada em `estimacao_regime_juros_altos.py` (conferido). LP linear e H2 não foram reestimadas → RR2-14 |
| REV-15b | consider | N (ac.) | R1 | — |
| REV-16 | must | **R** | EIC R; R1 R | — |
| REV-17 | should | **R** | EIC R; R1 R | — |
| REV-18 | should | **P** | EIC R; R1 P | **Arbitragem**: a grade e o sup-Wald existem e conferem. Mas a descrição no texto é seletiva (problema novo apontado por três assentos) e falta o indicador de estado não baseado na Selic → RR2-18, RR2-20, RR2-26 |
| REV-19 | should | **R** | EIC R; R1 R | — |
| REV-20 | must | **R** | EIC R; R1 R; DA (m8) R | — |
| REV-21 | must | **R** quanto ao critério; problema novo | EIC R; R2 "resolvido, com erro de execução"; DA (M1) "resolvido; gerou problema novo" | Cenários em termos reais existem. A execução e a leitura do ensaio geram RR2-08 a RR2-10 |
| REV-22 | must | **P** | EIC P; R2 P | A grade x × Δi está só em `resultados/` (conferido); base DPF aplicada à DBGG; linha "51,6% da DBGG" sem justificativa → RR2-12 |
| REV-23 | must | **P** | EIC R; R2 "resolvido no texto, número errado"; DA (m7) R | **Arbitragem**: prevalece R2 (número verificado na Seção 5) → RR2-10 |
| REV-23b | should | **P** | EIC P; R2 P (aceitável) | → RR2-13 (`consider`) |
| REV-24 | must | **R** | EIC R; R2 R | — |
| REV-25 | should | **R** | EIC R; R2 R | — |
| REV-26 | must | **R** | EIC R; R2 R (SGS 5793 conferida) | — |
| REV-27 | must | **R**, com ressalvas | EIC R; R2 R com ressalvas; DA (M2) R | Tabela 1 incompleta: linha de H2 e Curva de Phillips (R2b-5, DA2-3) → RR2-07 |
| REV-28 | must | **R** | EIC R; R1 R; R2 R; DA (M3) R | Resíduo: "γ̂ estável" (EIC2-2) → RR2-18 |
| REV-29 | must | **R** | EIC R; R1 R; R2 R | — |
| REV-30 | should | **P** | EIC P; R2 P | URLs dos posts → RR2-38 |
| REV-31 | should | **R** (quase) | EIC R; R2 R (faltam páginas) | → RR2-38 |
| REV-32 | must | **R** quanto ao critério | EIC R (breve); R1 R; R3 R com ressalvas | Ressalvas de R3 (método do numerador; nota de 28/12/2021; fase trimestral) → RR2-27, RR2-30, RR2-33 |
| REV-33 | must | **R** quanto ao critério; problema novo | EIC R (breve); R1 R; R3 R | Controles diferentes entre J e as demais séries (R3b-1) → RR2-28 |
| REV-34 | must | **R** quanto ao critério; problema novo | EIC R (breve); R1 R; R3 R | Mecanismos explicam um fato não estabelecido (R3b-4) → RR2-31 |
| REV-35 | should | **R** | EIC R (breve); R3 R | — |
| REV-36 | should | **R** | EIC R (breve); R3 R | — |
| REV-37 | consider | **R** | EIC R; R3 R | Falta a conta que liga a LP ao episódio (R3b-7) → RR2-35 |
| REV-38 | consider | **R** | EIC R; R1 R | A descrição da tabela no texto é seletiva (DA2-6) → RR2-24 |
| REV-39 | consider | **R** (por justificativa de omissão) | R3 R; R2 "não feito, aceitável" | **Arbitragem**: prevalece R3. O critério admitia "justificativa de omissão", e a §5.2 declara que os efeitos distributivos "são questões que este artigo não estuda" |

**Síntese.**
- **`must_fix` da 1ª rodada (25 itens, contados na tabela de 6.1 da decisão anterior):** 19 resolvidos, 5 deles com problema novo derivado (REV-05, 21, 27, 33, 34), e 6 parciais (REV-02, 07, 13, 15, 22, 23). O EIC fala em 26 itens; a diferença é de contagem e não muda nenhum status.
- **`should_fix` (12 itens):** 7 resolvidos (REV-10, 17, 19, 25, 35, 36 e, quase, 31) e 5 parciais (REV-06, 11, 18, 23b, 30).
- **`consider`:** REV-37, 38 e 39 resolvidos; REV-03b, 14b e 15b não feitos, o que é aceitável.

Nenhum item piorou: EIC, R1, R2, R3 e DA concordam nisso.

---

## 4. Consenso: problemas novos apontados por ≥ 2 assentos

**Regra de contagem.** Conto todos os assentos, incluindo o DA, e indico à parte quantos dos quatro que pontuam (EIC, R1, R2, R3) concordam. Lembrete (Seção 1.2): concordância é cobertura de papéis, não voto independente. A severidade é a de cada assento.

| CN | Problema | Assentos (severidade) | Que pontuam | RR2 |
|---|---|---|---|---|
| CN-1 | **"Tornamos o resultado nulo informativo"** (l. 73) contradiz a §4.5 (l. 439: "inconclusivo"; MDE de 0,42 por DP maior que o efeito moderado de −0,34). O que o artigo mostra é o limite do que os dados identificam | EIC2-1 (maior, de posicionamento); DA2-1 (MAIOR) | 1/4 (R1-S3 diverge na redação → D1) | RR2-01 |
| CN-2 | **Imprecisões do resumo e da Conclusão**: "em nenhum horizonte" é contradito na frase seguinte; "magnitude maior que o efeito moderado" só vale em h = 24; "não significativa sob bootstrap" (p = 0,073) é marginal; a redação do MDE inverte o conceito | EIC2-7 (menor); DA2-8 (MENOR); R1b-6 (menor, parte da redação) | 2/4 | RR2-02 |
| CN-3 | **LP totalmente interagida sem o bootstrap sob a nula.** O artigo usa a calibração para rebaixar γ̂ e o Wald-base, mas não a aplica à única rejeição forte (p = 0,001). Calibrada com o mesmo DGP, p ≈ 0,085–0,097 | R1b-1 (Maior); DA2-2 (MAIOR) | 1/4 | RR2-17 |
| CN-4 | **Grade de limiares descrita de forma seletiva.** O texto diz "positiva entre 9,5% e 13%", mas a diferença em h = 24 é positiva nos 11 limiares; no limiar de 14% ela vale +4,53 (p = 0,001) em h = 24 e +3,17 (p = 0,040) em h = 12; γ̂¹² vai a +0,13 e −0,56 nos limiares de 13,5% e 14%, o que desmente "γ̂¹² é estável" (l. 546) | EIC2-2 (menor); R1b-3 (menor); DA2-2 (MAIOR) | 2/4 | RR2-18 (e RR2-20 para o trimming) |
| CN-5 | **ω ≈ 1 atribuído à tese.** O ensaio diz que a inflação converge para "um nível mais baixo dado pela taxa de juros" (i − g real ≈ 5% com i = 7,5%) e que é inercial; o corte é sobretudo queda do juro real (ω ≈ 0). A "tensão" da Conclusão depende da leitura seletiva | R2b-1 (Maior); DA2-4 (MAIOR) | 1/4 | RR2-08 |
| CN-6 | **Títulos indexados ao IPCA tratados como prefixados** na Eq. (fiscal_scen). Isso superestima a piora em ω > 0 em cerca de 1/3 | R2b-2 (Maior); DA2-4, item 4 (MAIOR) | 1/4 | RR2-09 |
| CN-7 | **Tabela 1 marca "Sim" para H2** parafraseando "endividamento insustentável" como "carga de juros". Falta a linha da Curva de Phillips horizontal | R2b-5 (menor); DA2-3, item 2 (MAIOR) | 1/4 | RR2-07 |
| CN-8 | **H2 mede em parte a construção do indicador.** "Taxa efetiva" = J/E, taxa implícita estimada pelo BCB; um repasse de ≈ 0,8 em 12 meses ao estoque é alto demais para ser repreço; o resultado é "quase mecânico" | R3b-3 (maior); DA2-3, item 1 (MAIOR); EIC ("Adequação": "quase mecânico") | 2/4 | RR2-27 |
| CN-9 | **Assimetria de H2.** Em h = 0, surpresas dos dois sinais elevam J (b⁺ = +0,144; b⁻ = −0,171; p_sim < 0,001); a simetria só é rejeitada a 10%, com p_Holm = 0,34; a anedota de 2026 é confundida pela defasagem; a §5.2 e a Conclusão tratam surpresas negativas como cortes | R3b-2 (maior); R1b-7 (menor); DA2-7 (MENOR) | 2/4 | RR2-29 |
| CN-10 | **"Resultado mais robusto"** (resumo, l. 75, Conclusão) fixado em h = 12, sem dizer que o efeito é mais fraco na amostra trimestral reportada e que o pico robusto está em 12–18 meses | R1 (observação sem ID); DA2-3, item 3 (MAIOR); R3b-5 (menor, com leitura oposta → D2) | 2/4 | RR2-27, RR2-30 |
| CN-11 | **"Reestimamos tudo com a meta Selic"** é incorreto (l. 279): LP linear e H2 não foram reestimadas. R1 e R3 reestimaram H2: sobrevive (+0,270 por p.p., p = 0,012; ≈ 0,071 por DP; Holm 0,035) | R1b-2 (menor); R3b-6 (menor) | 2/4 | RR2-14 |
| CN-12 | **Anonimização não executada**: PDF com `\anonimofalse`, URL do GitHub, apêndice de versões; rótulos de versão no pacote | EIC2-5 (menor, bloqueante para duplo-cego); R1b-8 (menor); R2b-7 (menor) | 3/4 | RR2-36 |
| CN-13 | **Resíduos na §2.2**: os 2,3% "da versão anterior" sem dono; "4% a 5% do PIB" sem atribuição ao ensaio; ponto final ausente ("DBGG Terceiro") | EIC2-4 (menor); R2b-3 (Maior, parte da atribuição); R2b-7 (menor) | 2/4 | RR2-10 |
| CN-14 | **Grade de sensibilidade fiscal x × Δi fora do manuscrito** (resíduo de REV-22) | EIC2-8 (menor); R2b-7 (menor) | 2/4 | RR2-12 |
| CN-15 | **"Desalavancagem parcial"** na §4.7 e na Conclusão. R3 mostra que ela não sobrevive às defasagens próprias; DA e R2 usam a mesma queda de E como evidência contra a alegação literal do ensaio | R3b-1 (maior); DA2-3, item 2; R2b-5(b) | 2/4 | RR2-28 (direção arbitrada em D3) |

**Leitura de conjunto.** O consenso desta rodada é sobre **calibragem**, e não sobre desenho: aplicar a mesma régua inferencial a todas as estatísticas (CN-3, CN-4), dizer exatamente o que o nulo informa (CN-1, CN-2), corrigir a leitura do ensaio e a execução da aritmética fiscal (CN-5, CN-6, CN-13) e não deixar H2 sustentar mais do que a taxa implícita sustenta (CN-7 a CN-10, CN-15). Nenhum consenso aponta erro que inverta uma conclusão.

---

## 5. Divergências e arbitragens

### D1 — O nulo "tornou-se informativo"? (CN-1)
- *R1-S3*: "O nulo tornou-se informativo" (IC, MDE, LP interagida, "inconclusivo").
- *EIC2-1 e DA2-1*: o rótulo é falso pelo próprio critério do artigo.
- *Tipo*: redação (o fato não está em disputa).
- *Resolução*: prevalecem EIC e DA quanto ao rótulo; o mérito apontado por R1 fica registrado como "nulo **quantificado**" (Seção 8).
- *Fundamento*: conferi as l. 73 ("tornamos o resultado nulo informativo") e 439 ("O desenho não detectaria [...] O nulo de H₁ é inconclusivo"). R1 descreve o que o artigo faz (caracterizar o poder), e não afirma que o nulo discrimine as hipóteses. A formulação de EIC2-1 ("delimitamos o que esses dados podem identificar") acomoda as três leituras.

### D2 — H2 é robusto ou frágil? (CN-8, CN-10)
- *R1 e R3*: o efeito de J é robusto a EWC, NW h+3, p ∈ {2,…,12}, controle pelo estoque, corte em 2023:12 e SGS 432. A taxa implícita é robusta mesmo com defasagens próprias (R3b-1: +6,4, p < 0,001).
- *DA2-3*: o efeito é mecânico, pequeno e frágil na amostra trimestral (+0,19, p = 0,43 em h = 12).
- *Tipo*: avaliação da evidência.
- *Resolução*: H2 é **estatisticamente** o resultado mais robusto do artigo, mas o que ele documenta é o repasse da Selic à taxa implícita J/E, isto é, o elo inicial do canal convencional, e em parte talvez o método de estimação do BCB (R3b-3). O rótulo "mais robusto" pode ficar, desde que qualificado nesses termos (RR2-27).
- *Fundamento*:
  - **DA2-3(1)**, mecânico: corroborado por R3b-3, por outra via (o repasse de ≈ 0,8 ao estoque é implausível como repreço). Validado.
  - **DA2-3(3)**, fragilidade trimestral: **rejeitado como estabelecido**. A amostra reportada usa os meses 3/6/9/12 (conferido em `qmask`, l. 64). R3b-5 mostra que as outras duas fases dão +0,55 (p = 0,09) e +0,77 (p = 0,004) em h = 12, e todas as fases são significativas em h = 18. A fraqueza em h = 12 é, portanto, em boa parte dependente da fase escolhida. Procede apenas que o resumo não deve fixar o resultado em h = 12 (observação de R1) → RR2-30.
  - **DA2-3(4)**, magnitude pequena: o número é exato (0,07 p.p. por DP). Mas R3b-7 mostra que, escalado para o ciclo de 2021–23, o efeito é economicamente coerente (+1,7 a +2,2 p.p. previstos contra +2,6 p.p. observados). A correlação em nível de 0,09 não é teste. Parcialmente validado: a magnitude deve ser apresentada com as duas leituras (RR2-35).

### D3 — A queda do endividamento é evidência contra o ensaio? (CN-7, CN-15)
- *DA2-3(2) e R2b-5(b)*: a Tabela 11 mostra queda de E (≈ −1 p.p.), ou seja, desalavancagem, o contrário de "endividamento insustentável".
- *R3b-1*: com as defasagens próprias, a queda de E desaparece (−0,17, p = 0,76; 100 ln E: −0,3, p = 0,84).
- *Tipo*: direção.
- *Resolução*: prevalece R3. A linha da Tabela 1 deve registrar "endividamento: testado, **sem efeito detectável**", e não "desalavancagem contrária à tese". A frase "com desalavancagem parcial" sai da §4.7 e da Conclusão.
- *Fundamento*: R3 é o assento de famílias e fez a reestimação. Já no texto atual a queda não é significativa após Holm (conferido em `canal_familias.txt`: E com p_Holm entre 0,249 e 0,308). Um efeito não significativo não pode sustentar a leitura de R3 nem a do DA. Procede o ponto comum aos três assentos: a Tabela 1 não pode marcar "Sim" para uma alegação sobre endividamento que não foi confirmada.

### D4 — Como mapear o ensaio em ω (CN-5)
- *R2b-1*: apresentar duas leituras: ω → 1 no horizonte em que a proposição neo-fisheriana valesse; ω ≈ 0 no primeiro ano, coerente com i − g ≈ 5% e com inflação inercial. A tensão real é que o alívio sem pressão inflacionária exige um canal de demanda inoperante (Curva de Phillips horizontal).
- *DA2-4*: remover a equivalência "tese = ω ≈ 1", mapear a regra π → i − g para ω (que dá ω entre −0,12 e +0,14) e estender a grade a ω < 0.
- *Tipo*: remédio (as duas posições concordam no diagnóstico).
- *Resolução*: o diagnóstico procede. Combinar os remédios: remover a atribuição de ω ≈ 1 à tese, apresentar a leitura ω ≈ 0 como a coerente com o próprio ensaio (sem impedir que se discuta ω → 1 como horizonte neo-fisheriano) e reescrever a frase de tensão nos termos de R2b-1. A extensão da grade para ω < 0 fica como `should_fix` (RR2-11), porque só o DA a pede e ela não muda a conclusão.
- *Fundamento (conferido no ensaio)*:
  - p. 8: "A inflação inicia imediatamente sua convergência para um nível mais baixo **dado pela taxa de juros**".
  - p. 9: "No longo prazo a inflação converge para a diferença entre a taxa básica de juros e a taxa de crescimento real da economia"; "No curto prazo, a relação [...] pode ser inversa".
  - p. 8: "a inflação é inercial – tende a ficar onde está".
  - p. 6: "a Curva de Phillips tornou-se praticamente horizontal".
  - p. 10: crescimento real potencial de 2,5%.
  
  O ponto de equilíbrio ω* = 0,41 / 0,49 calculado pelo DA confere com os insumos da Tabela de cenários. Prefiro a formulação de R2b-1 para a Conclusão por se apoiar numa premissa textual do ensaio (Phillips horizontal). A do DA ("o que está em disputa é se essa queda desancora as expectativas") é compatível, e o autor pode usar as duas.

### D5 — "Limite superior" de 4–5% do PIB contra 3,96% (R2b-3)
- *Alegação*: a linha "todo o estoque refinanciado" aplica o corte da Selic (−6,44 p.p.) ao custo médio do estoque (12,63%).
- *Conferência*: −4,98 = 82,87 × (−6,44)/107,22 (confere com `aritmetica_fiscal.txt`). Com Δī = 7,5 − 12,63 = −5,13, o resultado é 82,87 × (−5,13)/107,22 = **−3,96**. O ensaio diz "de quase 13% para 7,5% [...] cerca de 4% do PIB ao ano" (p. 11, conferido).
- *Resolução*: **procede**. O "limite superior" do manuscrito é mais generoso que o do próprio ensaio. As colunas ω = 0,5 e ω = 1 dessa linha herdam o erro. A legenda diz "no primeiro ano", mas a última linha é um regime permanente: isso também procede (conferido na legenda da `tab:cenarios_fiscais`). A severidade "Maior" de R2 é mantida pelo peso da alegação, mas a correção é trivial. → RR2-10.

### D6 — Números corrigidos de ω com indexados (R2b-2; DA2-4, item 4)
- *R2b-2*: com x_IPCA = 23,59% da DPF (≈ 16,5% do PIB, RMD de set./2026), ω = 0,5 passa de +0,22/+0,44 para −0,03/−0,05 (36,1%, gradual/imediato) e ω = 1 de +1,53/+3,06 para +1,03/+2,07.
- *DA2-4(4)*: com participação **suposta** de 25%, +1,53 → cerca de +1,0.
- *Conferência*: o termo x_IPCA·ω·Δī/(1+g) vale −0,248 (ω = 0,5, gradual), −0,496 (ω = 1, gradual, ou ω = 0,5, imediato) e −0,992 (ω = 1, imediato). As correções de R2 para x = 36,1% conferem. Para x = 42,8%, obtenho −0,23 e +0,83 contra os "≈ −0,25 / ≈ +0,81" de R2: diferença imaterial de arredondamento.
- *Limite*: a participação de 23,59% vem do RMD consultado por R2 fora do pacote. O manuscrito só diz "parcela prefixada e indexada a preços, cerca de metade da DPF" (l. 214), e a Tabela de insumos não traz a participação dos indexados. Não pude conferi-la.
- *Resolução*: **procede**. O autor deve incluir a participação dos indexados na Tabela de insumos, com fonte, e refazer a tabela. Prevalece o número de R2 (fonte documental) sobre o ilustrativo do DA. → RR2-09.

### D7 — O DA atribui ao autor uma escolha seletiva do teste (DA2-2)
- *DA2-2*: "Na prática, o autor escolheu qual teste submeter ao procedimento mais exigente", e o resumo dá "tratamento retórico diferente" a dois resultados com o mesmo p de bootstrap.
- *Conferência*: o resumo (l. 46) diz que a especificação interagida "produz diferença significativa, de sinal favorável à hipótese". Ou seja, o texto **não** usou a ausência de calibração para favorecer o nulo. Apresentou como significativo, a favor de H1, o resultado não calibrado. A assimetria é de procedimento, não de direção retórica contra a tese.
- *Resolução*: o fato procede (a interagida não foi calibrada; R1b-1 confirma). A imputação de intenção é **rejeitada**: não é verificável e o sentido do viés é o oposto do sugerido. O remédio é o mesmo (RR2-17).

### D8 — Severidade da assimetria de H2 (CN-9)
- R3b-2 (maior) × R1b-7 (menor) × DA2-7 (MENOR).
- *Resolução*: `must_fix`. São três assentos, o p_Holm de 0,34 confere (mínimo 0,057 × 6) e R3 condiciona sua recomendação a esse item. As correções são de texto, mais uma reestimação barata (decomposição s/|s|, normalização pela Selic).

### D9 — Status divergente de itens do Roteiro
Arbitrado na Seção 3: REV-02, 13, 15, 18, 23 e 39. A regra foi dar prevalência ao assento cujo foco cobre o item e cuja verificação é mais profunda (o EIC verificou itens de R1/R3 só "brevemente", por declaração própria).

---

## 6. Adjudicação dos achados do Devil's Advocate

`da_critical_adjudications: []`. O DA não registrou achados CRÍTICOS e afirma que nenhum dos problemas derruba a conclusão central. Nenhum assento que pontua discorda.

| ID | Achado (resumo) | Corroboração | Adjudicação | Item |
|---|---|---|---|---|
| **DA2-1** (MAIOR) | "Nulo informativo" é falso; os limites unilaterais e o padrão de sinal da diferença (positivo em 26 de 28 especificações em h = 24; inverso em h = 12) não são reportados | EIC2-1 | **Parcialmente validado.** O rótulo é validado (l. 73 × l. 439, conferido). Os limites unilaterais por DP ([−0,04; +0,54] em h = 24; [−0,44; +0,11] em h = 12) conferem com `tab:nulo` × 0,156. A contagem de sinal confere nos pontos que verifiquei (11/11 na grade; p = 2 e p = 12 negativos, p = 4 e p = 9 positivos). **Mas** o valor informativo do padrão de sinal é rebaixado pelo próprio DA (DA2-2: sinal consistente na grade ocorre em ≈ 21% das réplicas sob a nula) e pela correlação entre especificações. A exigência de reportá-lo procede apenas com essa calibração. Ler a estimativa pontual como "perda de 50% a 110% do efeito, da ordem prevista por H1" não é sustentado por um intervalo que inclui zero | RR2-01; RR2-22; RR2-25 |
| **DA2-2** (MAIOR) | Bootstrap sob a nula aplicado seletivamente (não à interagida nem a H2); grade descrita seletivamente | R1b-1, R1b-3, EIC2-2 | **Validado** quanto aos fatos (§D só calibra a base; l. 472 × §G conferidos). A imputação de intenção é **rejeitada** (D7). O pedido de bootstrap para H2 é aceito na forma "aplicar ou justificar" | RR2-17; RR2-18 |
| **DA2-3** (MAIOR) | H2 mecânico, pequeno, frágil no trimestral e redefinido em relação ao ensaio | R3b-3 (item 1); R2b-5(b) (item 2); R1 obs. (item 3) | **Parcialmente validado.** (1) Validado com R3b-3. (2) Validado quanto à Tabela 1 ("Sim" para uma paráfrase), **rejeitado** quanto à direção "desalavancagem contrária à tese" (D3). (3) **Rejeitado como estabelecido**: depende da fase (R3b-5); procede só a recomendação de não fixar o resumo em h = 12 (D2). (4) Parcial: exato como número, mas R3b-7 mostra coerência econômica (D2) | RR2-07; RR2-27; RR2-28; RR2-30 |
| **DA2-4** (MAIOR) | ω ≈ 1 atribuído à tese sem base; ω < 0 omitido; indexados como prefixados; falso dilema | R2b-1; R2b-2 | **Validado.** Passagens do ensaio conferidas (D4); ω* = 0,41/0,49 conferido; indexados conferidos (D6). A qualificação "espantalho" é retórica do DA e não entra no roteiro; o remédio é reescrever a frase de tensão (D4) | RR2-08; RR2-09; RR2-11 |
| DA2-5 (MENOR) | Caminhos bifurcados: p = 6 é a única escolha em que C2 é significativo pelos dois critérios; testes "confirmatórios" declarados após exploração | — | **Validado parcialmente.** O texto já declara (l. 309) que os testes foram declarados "depois de uma análise exploratória". O rótulo é impreciso, mas a informação está lá | RR2-16 (`consider`) |
| DA2-6 (MENOR) | Tabela de episódios: a inflação caiu em quatro platôs, não dois; e subiu nos 12 meses seguintes ao fim dos quatro completos | — | **Validado** (conferido em §F: 4,12→5,94; 5,61→8,11; 1,48→2,76; 4,06→5,20; queda durante o platô em 4 de 5). O texto (l. 483) descreve só dois | RR2-24 |
| DA2-7 (MENOR) | Assimetria a 10%, anomalia em h = 0, anedota confundida | R3b-2; R1b-7 | **Validado** (D8) | RR2-29 |
| DA2-8 (MENOR) | "Em nenhum horizonte" contradito no próprio resumo | EIC2-7 | **Validado** (l. 46 conferida) | RR2-02 |

O contra-argumento global do DA ("relatório cuidadoso de que os dados não respondem à pergunta do título"; "nota metodológica") converge com EIC2-1 e com a avaliação de suficiência da contribuição do EIC. Não exige resposta item por item além de RR2-01. A escolha entre reposicionar como nota metodológica ou manter o formato de artigo fica com o autor.

---

## 7. Roteiro de Revisão da 2ª rodada

**Convenções**
- Os itens estão **por tema, na ordem em que os temas aparecem no manuscrito** (resumo/introdução → Tabela 1 e §2.2 → §3 → §4.5–4.6 → §4.7 → pacote). A ordem não indica prioridade além da classe.
- `Classe`: **must_fix** (condição para aceite); **should_fix** (esperado; uma recusa deve ser justificada); **consider** (opcional).
- `Custo`: texto; reestimação (código e dados do pacote); dados novos.
- As severidades de origem estão na Seção 4 e nos relatórios.

### 7.1 Tabela de itens

| ID | Origem | Classe | Localização | O que fazer | Critério de aceitação verificável | Custo |
|---|---|---|---|---|---|---|
| **RR2-01** | EIC2-1; DA2-1 (rótulo); (D1) | **must_fix** | Introdução, contribuições (l. 73) e resultados (l. 75); §4.5 (título do parágrafo/seção "O nulo de H1 é informativo?"); Conclusão (l. 627) | Reescrever a 1ª contribuição como delimitação do que os dados identificam (poder quantificado; dependência de p, da medida de juros, do limiar e da especificação; nem a tese nem a sua negação têm apoio). Na Conclusão, uma frase explícita: a evidência mensal agregada não arbitra a controvérsia. Opcional (EIC2-1): rebaixar a 3ª contribuição a "observação analítica" | A expressão "nulo informativo" (e variantes) não aparece no .tex, salvo negada. A contribuição 1 menciona o MDE e a falta de poder. A Conclusão contém uma frase sobre o que a evidência não arbitra | texto |
| **RR2-02** | DA2-8; EIC2-7; R1b-6 (redação do MDE) | **must_fix** | Resumo PT/EN (l. 46, 59); Introdução (l. 75); Conclusão (l. 627) | (a) Condicionar "não encontramos diferença [...] em nenhum horizonte" à especificação-base e ao sup-Wald sob a nula. (b) "Magnitude maior que o efeito moderado" → "em 24 meses". (c) γ̂: "não significativa a 5% sob bootstrap (p = 0,073)". (d) Reescrever o MDE corretamente (diferenças menores que ≈ 0,4–0,5 p.p. por DP são detectadas com probabilidade inferior a 80%). (e) Ajustar a frase sobre a interagida ao resultado de RR2-17 | Nenhuma frase incondicional "em nenhum horizonte" convive com a menção a uma diferença significativa. O MDE está definido corretamente. A frase sobre a interagida traz o p calibrado. Resumo ≤ 250 palavras | texto |
| RR2-03 | EIC2-6 | should_fix | Palavras-chave PT/EN (l. 49, 62) | Trocar "dominância fiscal" por "interação monetária-fiscal" ou "regime de juros", ou deixar claro na §1.1 que o tema é só motivação | A palavra-chave não promete um teste que o texto declara não fazer | texto |
| RR2-04 | R2b-6 | should_fix | §1, 1º parágrafo ("Uma tradição crítica sustenta...") | Citar Barth–Ramey e Ravenna–Walsh para o canal de custos. Descrever Loyo, Blanchard e Favero–Giavazzi como literatura de interação fiscal-monetária, não como "tradição crítica" | Cada canal citado remete a uma obra que o trata | texto |
| RR2-05 | R2b-4 | should_fix | §1.1, "Interação monetária e fiscal" | Trocar `cochrane2011determinacy` por Cochrane (2001, *Econometrica* 69(1)) ou manter só Sims (2011) e Cochrane (2023) para "maturidade da dívida determina o efeito de curto prazo" | A afirmação sobre maturidade não é atribuída a Cochrane (2011, JPE) | texto |
| RR2-06 | R2 (REV-06 residual); R3 (REV-06 residual) | consider | §1.1 | Considerar Sims (1994), Woodford (1995), Minella e Souza-Sobrinho (2013), Ayres et al. (2021), Garín–Lester–Sims (2018); literatura do canal de caixa (Flodén et al.; Di Maggio et al.) e Drehmann–Juselius–Korinek | Menção ou justificativa de omissão | texto |
| **RR2-07** | R2b-5; DA2-3(2); R2b-1 (linha de Phillips); (D3) | **must_fix** | Tabela 1 (`tab:componentes`, l. 109–116) | (a) Desdobrar a linha de H2 em "carga de juros das famílias: Sim (repasse à taxa implícita)" e "endividamento insustentável (ensaio, p. 5): testado, sem efeito detectável". (b) Acrescentar a linha "Curva de Phillips horizontal / recessão não reduz a inflação" (ensaio, p. 6 e 9), com status "Não identificado" | A Tabela 1 tem linhas separadas para carga de juros e endividamento, com a citação literal do ensaio para a segunda, e uma linha para a Curva de Phillips. Nenhuma linha marca "Sim" para uma paráfrase da alegação do ensaio | texto |
| **RR2-08** | R2b-1; DA2-4 (1), (2), (5); (D4) | **must_fix** | §2.2, 1ª conclusão (l. 214: "corresponde a ω próximo de 1"); Introdução, 3ª contribuição (l. 73); Conclusão (l. 631); §5.2 se aplicável | Remover a equivalência "tese = ω ≈ 1". Apresentar a leitura coerente com o ensaio (inflação de longo prazo = i − g real ≈ 5% com i = 7,5%; inflação inercial ⇒ ω ≈ 0 no primeiro ano), podendo discutir ω → 1 como horizonte neo-fisheriano. Informar o ponto de equilíbrio ω* (≈ 0,41–0,49). Reescrever a frase de "tensão" da Conclusão: o alívio e a ausência de pressão inflacionária exigem, juntos, um canal de demanda inoperante, hipótese que o artigo não testa | Nenhuma frase atribui ao ensaio ω ≈ 1 sem citação literal que o diga. O texto cita a regra de longo prazo do ensaio (p. 9) e informa ω*. A Conclusão não afirma "tensão com a tese" nos termos atuais | texto (cálculo simples) |
| **RR2-09** | R2b-2; DA2-4(4); (D6) | **must_fix** | Eq. (`fiscal_scen`); Tabela de cenários (`tab:cenarios_fiscais`); Tabela de insumos; `aritmetica_fiscal.py` (função `db`) | Decompor b em parcela Selic (x), indexada ao IPCA (x_IPCA, cujo custo nominal acompanha π), prefixada e cambial. Acrescentar o termo dos indexados e refazer a tabela. Incluir na Tabela de insumos a participação dos indexados com fonte (RMD) | A equação tem um termo para os indexados. A Tabela de insumos traz a participação com fonte e data. Com x = 36,1% e corte gradual, os valores para ω = 0,5 e ω = 1 diferem dos atuais na direção apontada por R2b-2 (≈ −0,03 e ≈ +1,03, ou o que resultar da participação documentada). Script e tabela conferem | reestimação (cálculo) |
| **RR2-10** | R2b-3; EIC2-4; R2b-7; (D5) | **must_fix** | Tabela de cenários, última linha e legenda; §2.2, 2ª e 3ª conclusões (l. 214); `aritmetica_fiscal.py` (`db(dbgg, dbgg, dI, w)`) | (a) Usar Δī = 7,5 − ī (custo médio) no regime permanente e reportar "cerca de 4% do PIB". (b) Atribuir esse número a Lara Resende (2026, p. 11) e mostrar que ele corresponde à linha "todo o estoque, ω = 0". (c) Separar a linha de regime permanente da legenda "primeiro ano" (ou ajustar a legenda). (d) Suprimir os 2,3% "da versão 3" (ou levá-los ao apêndice de versões, que sai na versão anônima). (e) Corrigir a pontuação "DBGG Terceiro" | A última linha com ω = 0 vale ≈ −3,96 (ou ≈ −4,3 com a DPMFi, declarado). O texto atribui os ≈ 4% ao ensaio. A legenda não chama de "primeiro ano" o regime permanente. "2,3%" não aparece no corpo. A pontuação está corrigida | texto + recálculo |
| RR2-11 | DA2-4(3) | should_fix | Tabela de cenários | Estender a grade de ω a valores negativos (previsão convencional: o corte eleva a inflação), dizendo que o custo de desancoragem e de prêmio não é modelado | Há ao menos uma coluna com ω < 0 e uma frase sobre o que a equação omite | cálculo |
| RR2-12 | EIC2-8; R2b-7; R2 (REV-22 residual) | should_fix | §2.2; Tabela de cenários | (a) Incluir a grade x × Δi (já em `resultados/`) como painel ou nota. (b) Reportar ao lado do termo bola-de-neve a versão em NFSP/DLSP (taxa implícita de 14,8%). (c) Justificar a linha "51,6% da DBGG" ou trocá-la pela exposição DPF flutuante + compromissadas, declarando a fonte | A grade aparece no texto. As duas bases do termo bola-de-neve são reportadas. A linha de 42,8% tem justificativa econômica explícita | texto (+ dado público para compromissadas) |
| RR2-13 | EIC (REV-23b); R2 (REV-23b) | consider | §2.2 | Simular a rolagem com o cronograma de vencimentos e cenários de prêmio a termo | Tabela de cenários com fonte do cronograma | dados novos |
| **RR2-14** | R1b-2; R3b-6; (REV-15) | **must_fix** | §3.2, 2º parágrafo (l. 279); Tabela 11 ou §4.7, item 3 | Reestimar a LP linear e H2 com o choque da SGS 432 e reportar (R1 e R3 indicam que H2 sobrevive com magnitude menor); ou trocar "reestimamos tudo" por "reestimamos as LPs dependentes de estado". Preferência dos dois assentos: reportar H2 | A frase do §3.2 corresponde ao que os scripts fazem. Se reportado, H2 com a SGS 432 aparece com coeficiente, p-valor e conversão por DP | reestimação |
| RR2-15 | R1b-8 | should_fix | §3.2 ("p < 10⁻¹¹" do F das sazonais) | Dizer qual é o teste (regressão só em dummies ou equação do VAR) e fazer um script gerá-lo | O número do texto é reproduzido por um script do pacote | reestimação |
| RR2-16 | DA2-5 | consider | §3.4, "Testes confirmatórios" (l. 309) | Trocar "confirmatórios" por "principais (pré-especificados nesta versão, sem pré-registro)" | Rótulo ajustado | texto |
| **RR2-17** | R1b-1; DA2-2; (D7) | **must_fix** | §4.5, "Especificação totalmente interagida" (l. 468) e "Bootstrap sob a nula" (l. 472); `tab:nulo`, Painel B; `inferencia_regimes.py` §D; resumo; Conclusão | Incluir os Wald da LP interagida (h = 12 e 24) no laço do bootstrap sob a nula, reportar p_boot e o quantil de 95% e reescrever as frases do resumo e da Conclusão com o p calibrado. Para H2 (teste C4), aplicar o mesmo bootstrap ou justificar no texto por que não | O Painel B da `tab:nulo` traz p_boot e o quantil de 95% da interagida. O resumo e a Conclusão não usam "significativa" para a interagida sem o p calibrado. Há bootstrap de C4 ou uma justificativa explícita | reestimação |
| **RR2-18** | EIC2-2; R1b-3; DA2-2 | **must_fix** | §4.5, parágrafo da grade (l. 472); §4.6, item 3 (l. 546); Conclusão ("resiste aos controles adicionais", l. 627) | Descrever a grade inteira: diferença em h = 24 positiva nos 11 limiares; limiar de 14% com +4,53 (p = 0,001) em h = 24 e +3,17 (p = 0,040) em h = 12, com 31 meses de platô (22 na amostra de h = 24, episódios de 2006–07 e 2016–17); γ̂¹² que desaparece acima de 13%. Corrigir "γ̂¹² é estável" para "estável em p e no Painel A, mas desaparece para limiares acima de 13% e com o juro real ex ante" | O parágrafo menciona o limiar de 14% e o número de meses. A frase "γ̂¹² é estável" está qualificada. A Conclusão não diz que γ̂ "resiste" sem essa ressalva | texto |
| RR2-19 | R1b-4 | should_fix | §3.4, item 3; `inferencia_regimes.py` §D | Reportar uma variante wild ou por blocos de resíduos para γ¹², para os Wald confirmatórios e para a interagida. Informar a fração de réplicas com Selic simulada negativa (ou descartá-las como sensibilidade) | Os p-valores das duas variantes estão no texto ou em nota | reestimação |
| RR2-20 | R1b-3 | should_fix | §4.5; Figura 6; sup-Wald | Restringir a grade aos quantis [0,15; 0,85] (trimming usual) ou reportar as duas versões, refazendo o sup-Wald bootstrap | Há sup-Wald com trimming de 15% reportado | reestimação |
| RR2-21 | R1b-6; R1 (REV-02 residual) | should_fix | `tab:nulo`; §4.5, "Poder e intervalo da diferença" | Incluir o MDE com EP EWC (2,70 em h = 12; 3,32 em h = 24; 0,52 por DP). Considerar uma banda simultânea para a *diferença* | A `tab:nulo` tem uma linha MDE EWC | texto (números já em `resultados/`) |
| RR2-22 | DA2-1 | should_fix | §4.5 | Reportar os limites unilaterais por DP em h = 12 e h = 24 e dizer que a direção da estimativa pontual se inverte entre os horizontes. Informar o padrão de sinal ao longo das especificações **com** a calibração sob a nula (frequência de sinal consistente sob a nula), sem lê-lo como evidência independente | O texto informa os limites e a inversão de sinal, e qualifica o padrão de sinal pela sua frequência sob a nula | texto |
| RR2-23 | R1b-5; R1 (REV-13 residual) | should_fix | Tabela 5 (`tab:robustez`); Tabela 4; §4.6 | Acrescentar o p EWC para β_mod^24 e para o Wald na Tabela 5. Incluir N_alto/N_mod por h na Tabela 4. Retirar ou qualificar "2 de 22 Wald rejeitam, o que se espera por acaso" (os testes são fortemente correlacionados) | A Tabela 5 tem coluna EWC. A Tabela 4 tem N por regime. O argumento "por acaso" está qualificado ou ausente | reestimação |
| RR2-24 | DA2-6 | should_fix | §4.5, "Episódios" (l. 483) | Descrever a tabela inteira: a inflação caiu durante quatro dos cinco platôs e, nos quatro episódios completos, subiu nos 12 meses após o fim. Comentar com a ressalva de endogeneidade | O parágrafo cobre os cinco episódios e o padrão pós-platô | texto |
| RR2-25 | DA2-1; DA2-5 | consider | §4.5 ou apêndice | Curva de especificações da diferença em h = 12 e h = 24 com as escolhas já exploradas (p, limiar, medida de juros e de inflação, controles) | Figura ou tabela da curva | reestimação |
| RR2-26 | R1 (REV-18 residual) | consider | §4.5 | Indicador de estado que não dependa da Selic | Especificação reportada | dados novos ou reestimação |
| **RR2-27** | R3b-3; DA2-3 (1), (4); R1 (observação sobre H2); EIC ("quase mecânico"); (D2) | **must_fix** | Resumo (l. 46); Introdução (l. 75); §3.1 (l. 229); §4.7, item 1 (l. 575); Conclusão (l. 629) | (a) Trocar "pela alta da taxa efetiva" por "pela alta da taxa implícita (juros/estoque), que combina repreço, composição e o método de estimação do BCB". (b) Documentar com fonte do BCB como se estimam juros e amortização no numerador, ou declarar explicitamente que o método não é público. (c) Qualificar "o resultado mais robusto": robusto estatisticamente, documenta o repasse convencional da Selic à taxa implícita e não é evidência a favor da tese. Dizer que o pico robusto está em 12–18 meses | O resumo, a §4.7 e a Conclusão usam "taxa implícita". A §3.1 traz a fonte do método ou a declaração de que ele é desconhecido. "Mais robusto" vem acompanhado da qualificação | texto |
| **RR2-28** | R3b-1; EIC2-3; DA2-3(2); (D3) | **must_fix** | Tabela 11 (`tab:servico`); §4.7, itens 1 e 2 (l. 575); Conclusão (l. 629); `canal_familias.py` (`CTRL`) | (a) Padronizar a Tabela 11 com as defasagens da variável dependente em todas as linhas (ou reportar as duas versões). (b) Retirar "com desalavancagem parcial" da §4.7 e da Conclusão, ou qualificá-la como não robusta. (c) Corrigir "p_Holm < 0,001 em todos os horizontes" para "p_Holm ≤ 0,007" | A Tabela 11 informa os controles de cada linha e são iguais (ou há duas versões). "Desalavancagem" não aparece como resultado sem qualificação. O p_Holm da taxa implícita confere com `canal_familias.txt` | reestimação |
| **RR2-29** | R3b-2; R1b-7; DA2-7; (D8) | **must_fix** | §4.7, item 4; §5.2 (l. 612: "não são simétricos"); Conclusão (l. 629: "Surpresas negativas não reduzem o comprometimento") | Reportar p_Holm da simetria (≈ 0,34) e o h = 0 da especificação assimétrica. Incluir a decomposição s/|s| (ou |choque| como controle). Normalizar pela resposta da Selic a s⁺ e s⁻. Rebaixar a assimetria a resultado exploratório. Retirar da §5.2 e da Conclusão as afirmações sobre cortes, ou reescrevê-las como "não há evidência de que surpresas baixistas reduzam rapidamente J; a assimetria não é robusta". Retirar o dado de fev.–ago./2026 como evidência de assimetria ou apresentá-lo como coerente com a defasagem | A §5.2 e a Conclusão não afirmam assimetria em cortes. A §4.7 informa p_Holm, h = 0 e o termo em |s|. O episódio de 2026 não é usado como evidência de assimetria | reestimação + texto |
| RR2-30 | R3b-5; DA2-3(3); R1 (observação); (D2) | should_fix | §4.7, item 3; `canal_familias.py` (`qmask`) | Reportar as três fases da amostra trimestral (ou a média), ou agregar o choque por trimestre em vez de descartar dois terços | Há resultados para as três fases ou uma versão agregada | reestimação |
| RR2-31 | R3b-4; R3b-1(3) | should_fix | §4.7, item 2 | Apresentar os mecanismos (Price, alongamento, concessões) como hipóteses compatíveis com uma resposta de A que não se mede com precisão. Reportar o MDE da resposta de S e da diferença J − S (≈ 1,2 e 0,86 p.p. em h = 12, segundo R3) | O texto não afirma que "o serviço total responde menos" como fato. O MDE de S e de A aparece | texto + recálculo |
| RR2-32 | R3b-3(2) | should_fix | §4.7 | Comparar a resposta de J/E com a das taxas médias de juros às pessoas físicas e do Indicador de Custo do Crédito (SGS; códigos a confirmar pelo autor), separando concessões e estoque | Há uma comparação reportada ou uma justificativa de omissão | dados novos (públicos) |
| RR2-33 | R3b-6 | should_fix | §3.1; Tabela 4 (`tab:series`); `referencias.bib` | Citar a nota de imprensa do BCB de 28/12/2021 sobre a substituição das séries 19879–19882. Dizer na Tabela 4 qual transformação cabe a 29035 e a 29037 | Nota citada; linha da Tabela 4 inequívoca | texto |
| RR2-34 | R3b-8 | should_fix | Limitação 6 | Uma frase: o denominador de 29033 (RNDBF restrita) exclui as rendas de propriedade; o indicador mede a carga bruta dos devedores e nada diz da redistribuição líquida | Frase presente | texto |
| RR2-35 | R3b-7; R3 (REV-11, REV-37 residuais); (D2) | consider | §4.7, último parágrafo | Reportar a resposta de J por p.p. de Selic na trajetória e a comparação aproximada com o ciclo de 2021–23, com ressalva | Conta reportada | texto |
| **RR2-36** | EIC2-5; R1b-8; R2b-7; (REV-07) | **must_fix** | `\anonimofalse` (l. 23); PDF p. 1; apêndice "Mudanças em relação às versões anteriores" (l. 650); cabeçalhos "VERSÃO 4" em `resultados/`; "Número da versão 3" em `aritmetica_fiscal.py`/`.txt`; "Base v3" e "Mudanças em relação à versão 3" em `estimacao_svar_lara_resende.py` | Compilar a submissão com `\anonimotrue`. Retirar os rótulos de versão do pacote de replicação (ou não anexá-lo até o aceite). Levar o apêndice de mudanças para a carta de resposta | O PDF de submissão não contém o nome, o URL do GitHub nem o apêndice de versões. Uma busca por "VERSÃO", "versão 3" e "v3" no pacote anexado não retorna nada | texto |
| RR2-37 | R1b-8 | should_fix | `data/safra_dados.txt`; `coleta_series_complementares.py` | Registrar a data de extração no momento do download ou incluir um hash do arquivo de `base_macro_bcb.csv` | A safra é gravada pelo script, não por texto fixo | código |
| RR2-38 | R2b-7; R2 (REV-30, REV-31 residuais); EIC (REV-30) | should_fix | `referencias.bib` | URLs completos dos dois posts de Cochrane (2026) e do RMD; páginas de Blanchard (2005), Favero–Giavazzi (2005) e Minella (2003); conferir as páginas de `arida2005credit` | Entradas completas | texto |

### 7.2 Contagem

| Classe | N | Itens |
|---|---|---|
| must_fix | 13 | RR2-01, 02, 07, 08, 09, 10, 14, 17, 18, 27, 28, 29, 36 |
| should_fix | 19 | RR2-03, 04, 05, 11, 12, 15, 19, 20, 21, 22, 23, 24, 30, 31, 32, 33, 34, 37, 38 |
| consider | 6 | RR2-06, 13, 16, 25, 26, 35 |

### 7.3 Natureza do trabalho

| Natureza | Itens |
|---|---|
| Só reescrita | must: RR2-01, 02, 07, 08, 18, 27, 36; should: 03, 04, 05, 22, 24, 33, 34, 38; consider: 06, 16, 35 |
| Recálculo ou reestimação com código e dados do pacote | must: RR2-09, 10, 14, 17, 28, 29; should: 11, 15, 19, 20, 21, 23, 30, 31, 37; consider: 25 |
| Dados novos (públicos) | should: RR2-12 (compromissadas, em parte), 32; consider: 13, 26 |

### 7.4 Lista de rastreabilidade

- [ ] RR2-01 — `must_fix` — reescrever a contribuição 1 e o rótulo "nulo informativo" (EIC2-1; DA2-1)
- [ ] RR2-02 — `must_fix` — precisão do resumo e da Conclusão; redação do MDE (DA2-8; EIC2-7; R1b-6)
- [ ] RR2-03 — `should_fix` — palavra-chave "dominância fiscal" (EIC2-6)
- [ ] RR2-04 — `should_fix` — atribuição do 1º parágrafo (R2b-6)
- [ ] RR2-05 — `should_fix` — citação de Cochrane (2011) (R2b-4)
- [ ] RR2-06 — `consider` — literatura residual (R2; R3)
- [ ] RR2-07 — `must_fix` — Tabela 1: desdobrar H2 e incluir a Curva de Phillips (R2b-5; DA2-3; R2b-1)
- [ ] RR2-08 — `must_fix` — mapeamento do ensaio em ω e frase de tensão (R2b-1; DA2-4)
- [ ] RR2-09 — `must_fix` — indexados ao IPCA na Eq. fiscal (R2b-2; DA2-4)
- [ ] RR2-10 — `must_fix` — limite superior ≈ 4%, atribuição, legenda, resíduos (R2b-3; EIC2-4; R2b-7)
- [ ] RR2-11 — `should_fix` — ω < 0 na grade (DA2-4)
- [ ] RR2-12 — `should_fix` — grade x × Δi, base NFSP, linha de 51,6% (EIC2-8; R2b-7)
- [ ] RR2-13 — `consider` — cenários de rolagem (REV-23b)
- [ ] RR2-14 — `must_fix` — "reestimamos tudo" com a SGS 432 (R1b-2; R3b-6)
- [ ] RR2-15 — `should_fix` — F das sazonais reproduzível (R1b-8)
- [ ] RR2-16 — `consider` — rótulo "confirmatórios" (DA2-5)
- [ ] RR2-17 — `must_fix` — bootstrap sob a nula da LP interagida (R1b-1; DA2-2)
- [ ] RR2-18 — `must_fix` — grade de limiares completa e γ̂ "estável" (EIC2-2; R1b-3; DA2-2)
- [ ] RR2-19 — `should_fix` — bootstrap wild/blocos; Selic negativa (R1b-4)
- [ ] RR2-20 — `should_fix` — trimming de 15% no sup-Wald (R1b-3)
- [ ] RR2-21 — `should_fix` — MDE EWC; banda da diferença (R1b-6; R1)
- [ ] RR2-22 — `should_fix` — limites unilaterais e inversão de sinal (DA2-1)
- [ ] RR2-23 — `should_fix` — EWC na Tabela 5; N por regime; "por acaso" (R1b-5)
- [ ] RR2-24 — `should_fix` — descrição completa dos episódios (DA2-6)
- [ ] RR2-25 — `consider` — curva de especificações (DA2-1; DA2-5)
- [ ] RR2-26 — `consider` — estado não baseado na Selic (R1)
- [ ] RR2-27 — `must_fix` — "taxa implícita", método do numerador, "mais robusto" qualificado (R3b-3; DA2-3; R1)
- [ ] RR2-28 — `must_fix` — controles da Tabela 11; desalavancagem; Holm (R3b-1; EIC2-3; DA2-3)
- [ ] RR2-29 — `must_fix` — assimetria de H2 e afirmações sobre cortes (R3b-2; R1b-7; DA2-7)
- [ ] RR2-30 — `should_fix` — fases trimestrais (R3b-5; DA2-3)
- [ ] RR2-31 — `should_fix` — mecanismos como hipóteses; MDE de S e A (R3b-4; R3b-1)
- [ ] RR2-32 — `should_fix` — J/E contra taxas médias do SGS (R3b-3)
- [ ] RR2-33 — `should_fix` — nota de 28/12/2021; Tabela 4 (R3b-6)
- [ ] RR2-34 — `should_fix` — Limitação 6 (R3b-8)
- [ ] RR2-35 — `consider` — magnitude por p.p. de Selic; ciclo 2021–23 (R3b-7)
- [ ] RR2-36 — `must_fix` — anonimização executada (EIC2-5; R1b-8; R2b-7)
- [ ] RR2-37 — `should_fix` — registro da safra (R1b-8)
- [ ] RR2-38 — `should_fix` — bibliografia residual (R2b-7; REV-30/31)

**Carta de resposta.** Responder item por item (RR2-01…38), com indicação de página e linha da alteração. Um item recusado deve vir com justificativa e fica registrado como não resolvido. Não houve carta nesta rodada; sua ausência obrigou cada assento a reconstruir o status do Roteiro, e ela é esperada na próxima submissão.

**Verificação prevista.** R1 e R2 declaram que os itens do seu domínio podem ser conferidos pelo editor sem nova rodada completa. R3 condiciona sua recomendação a RR2-29. Sugere-se conferência editorial dos `must_fix`, com consulta pontual a R1 (RR2-17, RR2-18), R2 (RR2-08 a RR2-10) e R3 (RR2-27 a RR2-29).

**Prazo do periódico**: `NOT PROVIDED`.

---

## 8. Méritos reconhecidos

Todos os méritos foram registrados pelos próprios assentos. Nenhum foi acrescentado para suavizar a decisão.

- **Reposicionamento completo e honesto** (EIC "Pontos fortes" 1; R2 1; DA "Resumo"). O título virou pergunta, o resumo abre pelo nulo e termina com "O canal da dívida pública pós-fixada não é testado". O enquadramento confirmatório que o EIC havia condicionado ao Reject não voltou.
- **Tabela 1 (componentes × testado/não testado)** (EIC 2; R2 1). É a solução adequada para um artigo motivado por um ensaio de opinião. As citações literais do ensaio conferem (EIC; conferido também nesta síntese para as passagens usadas em D4).
- **Reprodutibilidade exemplar** (R1 1; R3 1; EIC 6). Os seis arquivos de `resultados/` são reproduzidos byte a byte, sem rede, inclusive os bootstraps de semente fixa. O código é modular e a ordem de execução está documentada.
- **Resposta séria à crítica de inferência** (R1 2; EIC 3). EWC (reimplementado de forma independente por R1), banda sup-t, bootstrap recursivo sob a nula com reestimação do VAR, do choque e do estado, sup-Wald na grade e bootstrap de Kilian.
- **Nulo quantificado** (R1 3; EIC 3). IC da diferença, MDE, LP interagida e a frase "inconclusivo, e não uma rejeição"; o texto evita a falácia da diferença de significâncias (D1 sobre o rótulo).
- **Rebaixamento honesto do que não resistiu** (R1 4; DA "Status"). β_mod^24 virou "sugestivo, não robusto"; γ̂ virou associação de nível; o placebo de h = 0 virou diagnóstico; a troca do IC-Br e o papel das sazonais estão documentados.
- **Aritmética fiscal em termos reais, com insumos documentados** (EIC 4; R2 2 e 3). Insumos com código SGS ou RMD e data, conferidos por R2. A mensagem de que o alívio na razão exige queda do juro real é, nas palavras de R2, "a contribuição conceitual mais útil do artigo para o debate brasileiro", desde que o mapeamento para o ensaio seja corrigido (RR2-08).
- **Tratamento correto da *duration*** e **ciclos com números corretos** rebaixados a ilustração (R2 4 e 5).
- **H2 bem fundamentado no núcleo** (R1 5; R3 3). O mesmo choque para J, A, S, 29035 e E; a identidade J + A = S verificada no código; a resposta de J resiste a EWC, NW h+3, corte em 2023:12, controle pelo estoque e, nas checagens de R1 e R3, à SGS 432.
- **Proporcionalidade** (EIC 5; R3 4). O bloco teórico foi reduzido ao seu papel, a §5.2 virou um parágrafo e as Limitações são específicas. A §5.2 deixou de afirmar efeitos distributivos sem dados.
- **Honestidade sobre o nulo do serviço total** ("ausência de evidência, e não evidência de ausência") e menção à heterogeneidade (EE 80) (R3 5).
- **Divulgação dos caminhos de especificação** (DA2-5): todas as escolhas, inclusive as desfavoráveis, estão no texto ou em `resultados/`, o que permitiu as reanálises desta rodada.

---

*Os cinco relatórios da 2ª rodada ficam em `relatorios/` como anexo deste documento.*
