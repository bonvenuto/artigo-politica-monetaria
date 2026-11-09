# Relatório de Revisão: Metodologia (Revisor 1)

## Informações do manuscrito
- **Título**: Patamar de Juros, Dívida Pós-Fixada e Comprometimento de Renda das Famílias: Formalização Analítica e Evidência de Projeções Locais Dependentes de Estado para o Brasil (2005–2026)
- **Data da revisão**: 2026-11-09
- **Rodada**: painel simulado, rodada única deste assento
- **Vínculo com critérios do periódico**: `criteria_binding_unavailable`. Não há periódico-alvo confirmado. Os julgamentos abaixo seguem padrões gerais de econometria de séries temporais macro, e não as normas de um periódico específico.

## Identidade do revisor
Sou econometrista de séries temporais macro, com especialidade em SVAR e Projeções Locais (linha Plagborg-Møller–Wolf e Montiel Olea–Plagborg-Møller). Tenho trabalhos sobre LPs dependentes de estado e sobre inferência simultânea em múltiplos horizontes. **Ponto cego declarado:** não avalio a plausibilidade institucional dos canais (Bloco II, LC 179/2021 e a proposta de política).

## Foco da revisão
O foco tem três partes. (1) A identificação: Cholesky mensal, choque gerado e normalização de +1 p.p. (2) As LPs de estado: limiar endógeno, indicador construído com a própria Selic e poder dos testes de Wald. (3) A inferência: HAC com janela h+1, Holm comparado com bandas sup-t, VAR em níveis, escolha de p e tratamento da sazonalidade.

---

## Recomendação geral
**Major Revision**

## Confiança
**4.** O tema está no centro da minha especialidade. Reduzi um ponto porque não pude conferir os dados contra o SGS e o Olinda: a revisão é offline e só tive o CSV do pacote.

A confiança apenas declara incerteza e escopo. Ela não altera severidades.

## Status de calibração
`NOT_CALIBRATED`

---

## O que verifiquei executando código e o que é julgamento

Copiei o pacote para `r1_replica/` e rodei lá. Nada foi executado no diretório do pacote.

**Reprodução (verificado por execução)**
- `estimacao_regime_juros_altos.py`, `robustez_servico_divida.py` e `estimacao_local_projections.py` reproduzem os três arquivos de `resultados/` **byte a byte** (comparei com `diff`).
- As Tabelas 2 a 6 e a Tabela A conferem com os arquivos de resultado.
- O script `estimacao_svar_lara_resende.py` baixa dados da internet e não foi executado. Reestimei o VAR(6) a partir do CSV, e as IRFs da Tabela 2 conferem.

**Testes adicionais (verificado por execução)**
- Os scripts são `r1_checks.py`, `r1_checks2.py`, `r1_checks3.py` e `r1_checks4.py`.
- As saídas estão em `r1_checks_output.txt`, `r1_checks2_output.txt` e `r1_checks3_output.txt`, no mesmo diretório.
- O resultado de `r1_checks4.py` (teste F clássico de previsibilidade do choque, citado em S5) não foi salvo em arquivo; ele saiu apenas no console.
- Os testes cobrem: seleção de defasagens, efeito mínimo detectável (MDE), resposta da Selic por regime, placebo em h=0, sensibilidade a p, inferência EWC, bootstrap por blocos com banda sup-t, LP recursiva, bootstrap do SVAR, SVAR com sazonais, previsibilidade do choque e LP totalmente interagida.

**O que é julgamento**
- Severidades, interpretação econômica dos testes e recomendações.
- O bootstrap por blocos mantém o choque fixo e não reestima o VAR em cada réplica. Por isso ele é indicativo, e não uma alternativa definitiva ao HAC.

---

## Julgamentos por critério

| Dimensão / critério | Fonte do critério | Julgamento | Âncoras | Justificativa | Incerteza / limite | Pesa na decisão? |
|---|---|---|---|---|---|---|
| Rigor metodológico: identificação | Cartão do revisor (1); Plagborg-Møller & Wolf (2021) | PARTLY_MEETS | `table: Tabela 6, h=0, p(β_alto=β_mod)=0,031`; `text: §4.5 "a Selic subiu em apenas"` | O Cholesky mensal sobre a Selic média é transparente, mas a invariância do choque entre regimes não foi verificada (W4, W5) | Sem datas do Copom no pacote, não pude separar o efeito de carregamento da média mensal | sim: o choque sustenta H1 e H1' |
| Rigor metodológico: LPs de estado | Cartão (2); Ramey & Zubairy (2018) | PARTLY_MEETS | `table: Tabela 4, coluna Wald`; `table: Tabela 4, h=24, β_mod −1,982 (0,009)` | Teste de diferença sem poder relatado; resultado de h=24 frágil à escolha de p e à restrição de defasagens comuns entre regimes (W1, W2) | — | sim |
| Rigor metodológico: inferência | Cartão (3); Montiel Olea & Plagborg-Møller (2019); Lazarus et al. (2018) | PARTLY_MEETS | `text: §4.4 "janela de truncamento"` | Erros-padrão HAC com janela h+1 e poucos episódios; Holm sem banda simultânea (W3) | Bootstrap indicativo (choque fixo) | sim |
| Suficiência da evidência | quality_rubrics (geral) | PARTLY_MEETS | W1–W3 | H2 é robusto; β_mod^24 não é; γ^h é robusto em ponto, frágil em inferência | — | sim |
| Coerência argumentativa | quality_rubrics (geral) | MEETS | `text: §4.5 item 3` | O texto já separa associação de nível e choque identificado e reconhece resultados nulos | Há afirmações pontuais exageradas (W2, W7) | não, isoladamente |
| Reporte estatístico | statistical_reporting_standards | PARTLY_MEETS | `absence: §4.5 e Tabela 4 — expected IC ou MDE para β_alto−β_mod; checked §4.5, §4.6, §5.3, Tabelas 4–5` | Há efeitos em p.p. e reescala para 1 DP; faltam ICs da diferença e análise de poder | — | sim (ligado a W1) |
| Reprodutibilidade | Etapa 6 do protocolo | EXCEEDS | `dataset: scripts/ e resultados/ — reprodução byte a byte` | Reprodução exata e offline das LPs | O SVAR exige download | não |
| Originalidade, literatura, impacto | — | NOT_ASSESSED | — | Fora do escopo deste assento | — | — |

Não totalizei nem ponderei estes julgamentos.

---

## Avaliação resumida

O artigo estima um SVAR recursivo mensal (2005–2026, T=258) e LPs lineares, dependentes de estado e assimétricas. O objetivo é testar se a eficácia desinflacionária da Selic depende de um "platô" de juros altos (H1), se a permanência no platô se associa a inflação mais alta (H1') e se choques na Selic elevam o comprometimento de renda das famílias com juros (H2).

Do ponto de vista metodológico, a versão atual é honesta e reprodutível:
- reconhece que o resultado positivo no platô da versão anterior era artefato sazonal;
- reporta p-valores ajustados por Holm;
- reescala para 1 DP;
- trata γ^h como associação.

Minhas verificações confirmam que H2 é robusto: ele resiste à escolha de p entre 2 e 12, à inferência EWC, à LP recursiva e ao SVAR com dummies sazonais.

As conclusões sobre H1, porém, dependem de três fragilidades que o texto não quantifica:
- O teste de Wald entre regimes quase não tem poder. O MDE a 80% é de ≈2,8 p.p. em h=12, maior que o próprio efeito estimado no regime moderado.
- O efeito desinflacionário de 24 meses no regime moderado só é significativo com p=6 ou p=9. Com p=2, 4 ou 12 ele desaparece.
- A inferência HAC com janela h+1, apoiada em cerca de quatro episódios de platô utilizáveis, é otimista. Com bootstrap por blocos, nem γ^12 nem β_mod^24 são significativos.

Há ainda indícios de que o choque, identificado num VAR linear, não é invariante entre regimes: a resposta de impacto da PTAX difere entre eles, e o caminho da Selic também.

Nenhum desses problemas é fatal sozinho. Juntos, porém, exigem reanálise antes que as afirmações sobre H1 possam ser mantidas mesmo na forma cautelosa atual. Daí a recomendação de Major Revision.

---

## Pontos fortes

### S1: Reprodutibilidade computacional exata
Os três scripts de LP reproduzem byte a byte os arquivos de `resultados/` a partir do CSV, sem acesso à rede. As Tabelas 2 a 6 e a Tabela A conferem com essas saídas. Isso é raro e permite auditar cada número.
**Evidence Anchor**: `dataset: scripts/estimacao_regime_juros_altos.py, robustez_servico_divida.py, estimacao_local_projections.py — saídas idênticas a resultados/*.txt`

### S2: Reporte transparente de resultados nulos e frágeis
O texto informa que o β_alto positivo da versão anterior "desaparece com o controle sazonal". Também reporta Holm, a contagem de surpresas negativas em que a Selic de fato caiu (38 de 59) e a escala de 1 DP. E declara que γ^h não distingue a hipótese de Lara Resende da causalidade reversa. Isso reduz o risco de reporte seletivo.
**Evidence Anchor**: `text: §4.5, item 2 "esse resultado desaparece com o controle sazonal e não deve ser interpretado como evidência a favor"`

### S3: H2 robusto às verificações independentes
Verifiquei por execução que o efeito de +0,46 p.p. em h=12 sobre J^fam:
- vale com p ∈ {2, 4, 6, 9, 12}: entre +0,40 e +0,49, com p ≤ 0,005;
- resiste à inferência EWC de Lazarus, Lewis, Stock e Watson (2018): p = 0,007 em h=12 e p = 0,0009 em h=18;
- se mantém quando a Selic entra como regressor, com controles contemporâneos (o choque gerado não altera a inferência);
- aparece também no SVAR com dummies sazonais: +0,393 [0,146] em h=12.

O contraste com o serviço total (Apêndice A) também é informativo.
**Evidence Anchor**: `table: Tabela 3, coluna LP juros, h=12 +0,4594 (0,144) [0,001]`

### S4: Bateria de robustez bem desenhada, e γ^h resiste a controles adicionais
A especificação 8 (choque de um VAR com sazonais) e a especificação 5 (regime definido pelo juro real ex ante) são as perguntas certas. Testei se γ^h é apenas o efeito das defasagens 7 a 12 omitidas, já que a MM12 da Selic usa 12 defasagens e as LPs controlam só 6. Não é: γ^12 vale +1,80 (p=0,002) com 12 defasagens, +1,53 (p=0,013) com a inflação acumulada em 12 meses defasada e +1,52 (p=0,018) com a MM12 linear da Selic. Em h=18 o resultado perde significância nesses casos.
**Evidence Anchor**: `table: Tabela 5, linhas γ^h, especificações 1–8`

### S5: O choque não é previsível com informação defasada
Verifiquei por execução:
- o Ljung-Box do choque tem p entre 0,35 e 0,95 nas defasagens 6, 12 e 24;
- o teste F de que o choque responde às defasagens 7 a 12 de todo o sistema dá p = 0,90;
- a expectativa Focus em t−1 não prevê o choque (p = 0,60).

Assim, a omissão de expectativas não aparece como previsibilidade do choque.
**Evidence Anchor**: `dataset: r1_replica/r1_checks3_output.txt (Ljung-Box, Focus t−1) e r1_checks4.py (F clássico, só console) — previsibilidade do choque`

### S6: Formulação testável de H1
A implicação (iii) de H1, β_alto > β_mod, é a forma correta de separar a dependência de estado de "imprecisão em um regime". O artigo a aplica de forma honesta.
**Evidence Anchor**: `text: §1, H1 "A implicação (iii) é a que distingue $H_1$ de uma transmissão homogênea com estimativas imprecisas"`

---

## Pontos fracos

### W1: O teste de diferença entre regimes não tem poder relatado, e a conclusão sobre H1 depende de restringir as defasagens a serem comuns entre regimes

**Problema**: §4.5 e a Conclusão concluem que H1, "na forma em que distingue os regimes, não encontra apoio nos dados", a partir de p-valores de Wald entre 0,23 e 0,90. Não há IC para β_alto − β_mod nem efeito mínimo detectável.

Calculei os dois a partir da especificação-base (verificado por execução):

| h | Erro-padrão da diferença | MDE a 80% | IC 95% da diferença |
|---|---|---|---|
| 12 | 1,00 | 2,81 p.p. por choque de 1 p.p. (0,45 p.p. por 1 DP) | [−3,05; +0,89] |
| 24 | 0,90 | 2,52 p.p. | [−0,72; +2,81] |

Em h=24, o MDE supera o próprio |β_mod^24| = 1,98.

A especificação também restringe os coeficientes das defasagens a serem iguais nos dois regimes; só o choque e o intercepto interagem com o estado. Na versão totalmente interagida (Ramey & Zubairy, 2018), o resultado muda em h=24 (verificado por execução): β_alto = +1,76 (p=0,029), β_mod = −2,27 (p=0,005) e Wald p = 0,001, que favorece H1. Essa versão tem 98 regressores para N=228, e o HAC tende a rejeitar demais nessas condições. Não a apresento como evidência a favor de H1, e sim como prova de que o resultado nulo depende da especificação.

**Evidence Anchor**: `text: §4.5, item 2 "A implicação (iii), que distingue $H_1$ de uma transmissão homogênea estimada com imprecisão, não encontra apoio nos dados"`

**Por que importa**: com esse poder, a falta de rejeição não informa. O leitor pode tomar "não encontra apoio" como evidência de transmissão homogênea. Na verdade, os dados não conseguem distinguir H1 nem de homogeneidade nem do seu oposto.

**Sugestão**:
- Reportar, para cada h, a diferença β_alto − β_mod com IC 95% (e uma banda simultânea) e o MDE.
- Trocar "não encontra apoio" por "os dados são inconclusivos; diferenças menores que ≈2,5 p.p. por 1 p.p. não seriam detectáveis".
- Reportar a versão totalmente interagida, ou a de transição suave de Tenreyro–Thwaites com controles interagidos, e discutir a divergência.

**Severidade**: Major
**Confiança**: 5. Especialidade central: LPs dependentes de estado.

### W2: O efeito desinflacionário de 24 meses no regime moderado depende da escolha de p = 6

**Problema**: O resumo e a Conclusão (item 2) apresentam β_mod^24 = −1,98 (p=0,009) como achado, e a Conclusão o chama de "resultado estável entre especificações". Reestimei VAR e LP com o mesmo p, mantendo os demais elementos da especificação-base (verificado por execução):

| p | β_mod^24 | p-valor |
|---|---|---|
| 2 (escolhido por BIC/HQIC) | −1,23 | 0,105 |
| 4 | −1,71 | 0,150 |
| 6 | −1,98 | 0,009 |
| 9 | −1,66 | 0,029 |
| 12 | −0,49 | 0,662 |

Com p=12, a ordem se inverte: β_alto^24 = −2,14 (p=0,034). Esse resultado se soma ao que o próprio artigo já mostra: Holm p=0,061, queda à metade com a dummy de COVID e falta de significância com o IPCA cheio.

Em contraste, γ^12 (entre +1,51 e +1,81, p ≤ 0,007) e J^fam são estáveis em p. A escolha de p=6 em §4.1 se apoia na "dinâmica semestral", e não nos critérios de informação.

**Evidence Anchor**: `text: §6, item 2 "resultado estável entre especificações, mas reduzido à metade com controle para a pandemia"`

**Por que importa**: a implicação (i) de H1 é dada como "sustentada, mas com evidência moderada". Ela depende de uma escolha de p que nenhum critério de informação seleciona. Esse é o único efeito desinflacionário significativo das LPs de estado.

**Sugestão**:
- Incluir na Tabela 5 uma linha de sensibilidade a p ∈ {2, 4, 6, 9, 12}.
- Rebaixar a implicação (i) a "sugestiva e não robusta" no resumo e na Conclusão.
- Remover "estável entre especificações".
- Considerar LP com lag augmentation (Montiel Olea & Plagborg-Møller, 2021), que reduz a dependência de p.

**Severidade**: Major
**Confiança**: 5. Especialidade central; verificado por execução.

### W3: Inferência HAC com janela h+1 em variáveis acumuladas sobrepostas, com poucos episódios de platô

**Problema**: As LPs usam a soma da inflação de t a t+h e erros-padrão Newey-West com janela h+1. O indicador de platô produz **cinco** episódios:

| Episódio | Duração |
|---|---|
| 2006-03 a 2009-10 | 44 meses |
| 2011-09 a 2012-04 | 8 meses |
| 2015-04 a 2017-10 | 31 meses |
| 2022-11 a 2024-09 | 23 meses |
| 2025-05 a 2026-08 | 16 meses |

O último episódio entra com, no máximo, 4 observações em h=12 e nenhuma em h=24 (verificado por execução). Na prática, a comparação entre regimes repousa em cerca de quatro episódios.

Com regressor de estado persistente e dependente acumulado, o Bartlett com janela h+1 tende a subestimar a variância. Comparei três abordagens (verificado por execução):

| Estatística | NW (h+1) | EWC (ν≈15) | Bootstrap por blocos (L=24, B=999) |
|---|---|---|---|
| γ^12 | p = 0,003 | p = 0,013 | t = 1,95 |
| γ^18 | p = 0,037 | p = 0,070 | — |
| β_mod^24 | p = 0,009 | p = 0,024 | t = −1,61 |

- O EWC segue Lazarus, Lewis, Stock e Watson (2018).
- O bootstrap por blocos reamostra pares e mantém o choque fixo. Seus erros-padrão são 1,5 a 1,8 vezes maiores que os NW. Com bloco L=12 os resultados são parecidos (t = 1,87 e −1,49).
- Na banda sup-t do bootstrap, nenhum horizonte de γ^h, β_mod^h ou β_alto^h é significativo.

O texto menciona sup-t só como "alternativa menos conservadora", sem implementá-la. E Holm é feito dentro de cada coeficiente, embora a análise inclua três coeficientes, sete horizontes, oito especificações e a versão assimétrica.

**Evidence Anchor**: `text: §4.4 "erros-padrão robustos à heterocedasticidade e autocorrelação (HAC / Newey-West, janela de truncamento $h + 1$)"`

**Por que importa**: o "resultado mais estável do artigo" (γ^12, Holm p=0,019) e o único efeito desinflacionário de estado (β_mod^24) estão no limiar da significância com inferência robusta à dependência. A afirmação de §5.3, de que a amostra contém "quatro grandes ciclos de aperto no platô alto", também não confere com o indicador.

**Sugestão**:
- Adotar inferência robusta como padrão: EWC ou fixed-b com valores críticos t_ν, ou LP com lag augmentation e erros-padrão EHW.
- Reportar bandas sup-t (Montiel Olea & Plagborg-Møller, 2019) para γ^h e β^h na Figura 5.
- Fazer um bootstrap que reestime o VAR e o choque em cada réplica.
- Informar o número de episódios e de observações por regime e horizonte.

**Severidade**: Major
**Confiança**: 4. Especialidade central; o bootstrap é indicativo, pois o choque fica fixo.

### W4: O choque é identificado num VAR linear, mas usado como se fosse válido dentro de cada regime; o placebo de impacto e a trajetória da Selic indicam o contrário

**Problema**:

*(a) Placebo de impacto.* No Cholesky, a PTAX, ordenada antes da Selic, tem resposta nula em h=0 por construção. No agregado da amostra isso vale exatamente. Dentro de cada regime, deveria valer aproximadamente se a identificação for invariante. A Tabela 6 mostra β_alto = −5,62 e β_mod = +2,64 em h=0, com p(β_alto = β_mod) = 0,031. O texto lê esse resultado como "estimativa pontual de apreciação no platô". Mas uma resposta de impacto diferente de zero, numa variável que a identificação proíbe de reagir, é sinal de violação do esquema de identificação, e não um fato econômico. O teste conjunto que fiz para a PTAX em h=0 dá p = 0,038 sem sazonais e p = 0,078 com sazonais. Para inflação, IBC e ICBr, os p-valores ficam entre 0,26 e 0,75.

*(b) A política não segue o mesmo caminho nos dois regimes.* A LP da própria Selic por regime mostra (verificado por execução):

| | Platô alto | Regime moderado |
|---|---|---|
| Selic em h=0 | ≈1,0 | ≈1,0 |
| Selic em h=12 | +1,49 (EP 1,36) | +2,51 (EP 0,64) |
| Selic em h=24 | +1,06 | −1,25 |
| Soma de 0 a 12 | 25,7 p.p.-mês | 31,8 p.p.-mês |

Logo, comparar β_alto^h com β_mod^h mistura a eficácia do choque com intensidades e persistências de aperto diferentes.

**Evidence Anchor**: `table: Tabela 6, h=0 — β_alto −5,624 (0,096), β_mod +2,643 (0,111), p(β_alto=β_mod)=0,031`

**Por que importa**: H1 é uma afirmação sobre a eficácia por unidade de política em cada regime. Se a função de reação e a persistência do aperto mudam entre regimes, o choque de um VAR linear não é o mesmo objeto nos dois regimes. A diferença de eficácia (ou a ausência dela) fica sem interpretação clara.

**Sugestão**:
- Reportar a resposta da Selic por regime, como "primeiro estágio".
- Normalizar as respostas de inflação pela resposta acumulada da Selic em cada regime: razão de integrais, ou LP-IV com a Selic acumulada instrumentada pelo choque.
- Identificar o choque com um VAR que permita coeficientes dependentes do estado (VAR com limiar ou com transição suave), ou estimar a LP recursiva por regime com os controles contemporâneos interagidos.
- Tratar o placebo de h=0 como diagnóstico, e não como resultado econômico.

**Severidade**: Major
**Confiança**: 4. Especialidade central. O placebo é marginal, e a diferença de trajetória da Selic é imprecisa no platô.

### W5: Cholesky mensal sobre a Selic média do mês: o "choque" se distancia de uma surpresa de política

**Problema**: A Selic usada é a SGS 4189, uma média mensal anualizada. As reuniões do Copom caem em datas variadas dentro do mês. Por isso, uma decisão tomada no meio do mês t aparece em parte em t e em parte em t+1, e a ordenação recursiva mensal confunde a resposta da política com esse efeito de carregamento.

Os próprios números do artigo sinalizam o problema:
- das 63 surpresas positivas no platô, a Selic subiu em apenas 13;
- a correlação entre o choque e a variação mensal da Selic é de 0,44, com R² de 0,19 (verificado por execução).

O efeito-informação é citado (Nakamura & Steinsson, 2018), mas não é tratado na identificação.

**Evidence Anchor**: `text: §4.5, especificação assimétrica (segundo item da lista de especificações) "entre os $63$ meses de surpresa positiva, a Selic subiu em apenas $13$"`

**Por que importa**: o choque é um desvio de uma regra linear estimada sobre médias mensais. Ele não é uma decisão inesperada do Copom. Isso afeta a leitura de β^h como "efeito de um aperto", sobretudo na especificação assimétrica.

**Sugestão** (das opções de menor para maior custo):
- Reestimar com a meta Selic de fim de período (SGS 432) ou com a Selic do último dia útil.
- Usar uma amostra por reunião do Copom.
- Idealmente, usar surpresas de alta frequência em futuros de DI como instrumento externo (LP-IV), ao menos como robustez para as LPs lineares e para H2.

O artigo trata HFI como extensão futura. Considero que ao menos uma das alternativas de menor custo deveria entrar nesta revisão.

**Severidade**: Major
**Confiança**: 4. Especialidade central. A magnitude do efeito de carregamento não pôde ser medida sem as datas do Copom.

### W6: O SVAR-base não tem dummies sazonais, embora o resumo diga que a especificação-base as tem; a dinâmica de inflação da Tabela 2 muda quando elas entram

**Problema**: O resumo afirma que a especificação-base tem dummies sazonais. Isso vale para as LPs de estado, mas não para o SVAR (Tabela 2, Figuras 2 e 3) nem para a LP linear (Tabela 3). O resíduo da equação de inflação do VAR(6) tem autocorrelação de +0,13 na defasagem 12 (Ljung-Box p = 0,021), que desaparece com as dummies (p = 0,25).

Reestimei o SVAR com sazonais exógenas (verificado por execução):

| Inflação | SVAR-base (Tabela 2) | SVAR com sazonais |
|---|---|---|
| h=6 | +0,188 [0,093], significativo | +0,088 [0,082], não significativo |
| h=12 | −0,134 [0,060], significativo | −0,056 [0,049], não significativo |
| h=18 e h=24 | ≈ −0,10 | ≈ −0,10 (inalterado) |

O "price puzzle" significativo em h=6 e a reversão significativa em h=12, discutidos em §4.2, item 3, são em boa parte sazonais. J^fam e a FEVD de J^fam não se alteram de modo relevante (participação da Selic de 14,9%, 17,0% e 15,9%). Mesmo com dummies, o teste Portmanteau multivariado rejeita a ausência de autocorrelação nos resíduos (p < 0,001 em 12 e 24 defasagens).

**Evidence Anchor**: `text: Resumo "com dummies sazonais na especificação-base"`

**Por que importa**: a narrativa do SVAR sobre a inflação, incluindo o "pico de +0,357 em h=5" e a reversão significativa a partir do 12º mês, depende de uma especificação que o próprio artigo já considera inadequada para a inflação sem ajuste sazonal. As conclusões principais não dependem dela, mas a Tabela 2 e a §4.2 sim.

**Sugestão**:
- Tornar padrão o SVAR com dummies sazonais (como na especificação 8) e reapresentar a Tabela 2 e as Figuras 2 e 3.
- Manter a versão sem dummies como robustez.
- Reportar testes de autocorrelação residual e discutir a autocorrelação que sobra (por exemplo, em J^fam, cuja ADF escolhe 16 defasagens).

**Severidade**: Major
**Confiança**: 5. Verificado por execução.

### W7: A "equivalência" LP–SVAR em h=0 é mecânica, e "forte aderência" exagera

**Problema**: A LP linear usa como regressor o resíduo ortogonalizado do próprio VAR, com as mesmas defasagens como controles. Pelo teorema de Frisch-Waugh-Lovell, o coeficiente em h=0 coincide com o impacto do Cholesky dentro da amostra, por construção. Isso não confirma nada. A inflação em h=0 tem coeficiente exatamente 0, com EP 0,087 e p = 1,000, e esse p-valor ainda entra na família de Holm.

Fora de h=0, os dois métodos divergem bastante:

| | SVAR | LP |
|---|---|---|
| Inflação, h=9 | +0,05 | −0,22 |
| Inflação, h=24 | −0,10 | −0,33 |
| J^fam, h=18 | +0,29 | +0,59 |

Verifiquei por execução que a LP recursiva (Selic_t como regressor, mais controles contemporâneos das variáveis ordenadas antes) dá os mesmos pontos e erros-padrão a até ±8% de distância. Portanto, o problema do regressor gerado não é material aqui.

**Evidence Anchor**: `text: §4.4 "confirmam a equivalência algébrica em $h = 0$ \citep{plagborg2021local} e a forte aderência entre os dois métodos"`

**Por que importa**: o texto apresenta como robustez algo que é identidade, e minimiza divergências que são informativas: em amostra finita, as LPs têm menos viés e mais variância que o VAR.

**Sugestão**:
- Escrever a LP na forma recursiva de Plagborg-Møller e Wolf.
- Dizer explicitamente que a igualdade em h=0 vale por construção.
- Excluir da família de Holm os horizontes nulos por construção.
- Trocar "forte aderência" por uma descrição das divergências.

**Severidade**: Minor
**Confiança**: 5. Especialidade central.

### W8: A normalização para +1 p.p. extrapola, sobretudo na especificação assimétrica

**Problema**: O artigo já reconhece que +1 p.p. corresponde a cerca de 6 DP do choque. No platô, o DP do choque é 0,144, e as partes ± separadas têm desvio ainda menor, o que leva os coeficientes β^{+} e β^{−} para cerca de 7 DP ou mais. Além disso, no SVAR um choque de +1 p.p. desencadeia um ciclo de aproximadamente +3 p.p. A Conclusão também lista "−1,98 p.p. por choque de 1 p.p." antes do valor por 1 DP.

**Evidence Anchor**: `text: §4.5, especificação 2 "corresponde a cerca de seis desvios-padrão e está fora do intervalo observado"`

**Por que importa**: o leitor tende a ler "+1 p.p." como uma alta de 100 pb do Copom, um evento muito maior que qualquer choque da amostra.

**Sugestão**:
- Usar 1 DP como unidade principal nas Tabelas 4 a 6 e no resumo, ou normalizar pela resposta acumulada da Selic (ver W4).
- Manter +1 p.p. apenas na comparação com o SVAR.

**Severidade**: Minor
**Confiança**: 5.

### W9: O limiar na mediana não é testado formalmente, e o indicador é construído com a própria variável de política

**Problema**:
- O limiar de 11,27% é a mediana da MM12 da Selic. Não há teste de não linearidade com limiar estimado (sup-Wald de Hansen, 2000) nem uma figura de γ^h e β^h ao longo de uma grade de limiares.
- O γ^h cresce à medida que o limiar cai: em h=18, vale +2,55 com limiar de 10%, contra +1,44 na base. Isso sugere que γ^h capta em boa parte o fato de os períodos com Selic acima de 10% serem os de inflação alta.
- A perda de significância com o regime definido pelo juro real ex ante (especificação 5) é coerente com essa leitura. O artigo a reconhece, mas segue chamando γ^h de "resultado mais estável".

**Evidence Anchor**: `table: Tabela 5, especificação 6, γ^18 = +2,547 (<0,001) e especificação 5, γ^12 = +0,934 (0,140)`

**Por que importa**: quando o indicador de estado é função da variável de política, a "permanência no platô" e o estado da inflação se confundem.

**Sugestão**:
- Apresentar γ^h e β^h ao longo de uma grade de limiares (por exemplo, de 9% a 14%) com bandas.
- Fazer um teste sup-Wald com p-valores por bootstrap.
- Acrescentar um indicador de estado que não dependa da Selic: por exemplo, o hiato de inflação defasado. Assim γ^h pode ser comparado com ele.

**Severidade**: Minor. O artigo já qualifica γ^h como associação.
**Confiança**: 4.

### W10: VAR em níveis com raiz quase unitária: viés de amostra finita e bandas assintóticas no limite

**Problema**: O maior módulo das raízes do VAR(6) fica muito perto de 1: a menor raiz do polinômio inverso tem módulo 1,0006. Comparei as bandas assintóticas com um bootstrap residual recursivo (B=499), que reestima P55 em cada réplica (verificado por execução):
- Os erros-padrão do bootstrap são parecidos com os assintóticos. Logo, dividir por P55 sem propagar sua incerteza não é material.
- Os pontos estimados têm viés de amostra finita: em J^fam, h=12, o ponto é 0,382 e a média do bootstrap é 0,307; em h=24, 0,111 contra 0,029.
- Os intervalos percentis da inflação em h=18 e h=24 tocam zero (limites superiores de +0,001), embora a Tabela 2 os marque em negrito.

**Evidence Anchor**: `table: Tabela 2, linha IPCA Itens Livres, h=18 −0,1020 [0,047] e h=24 −0,0956 [0,044] em negrito`

**Por que importa**: o argumento de Sims, Stock e Watson (1990) garante consistência dos coeficientes, mas não a validade de bandas assintóticas em horizontes longos com raiz quase unitária.

**Sugestão**:
- Usar bootstrap com correção de viés (Kilian, 1998), ou LP com lag augmentation, para as bandas do SVAR.
- Retirar o negrito das respostas que ficam no limite.

**Severidade**: Minor
**Confiança**: 4.

### W11: Pequenas inconsistências numéricas e textuais

**Problema**:
1. §4.2, item 3: o texto diz "+0,357 p.p. em h=5", mas a reestimação dá +0,344.
2. §4.4: "os p-valores ajustados permanecem abaixo de 0,01", e a lista inclui 0,010.
3. §5.3, item 3: "quatro grandes ciclos", contra cinco episódios no indicador (ver W3).
4. A FEVD rotulada "h=12" corresponde à previsão de 12 passos, ou seja, a IRF até h=11. Isso é apenas convenção, mas deve ser dito.

**Evidence Anchor**: `text: §4.2, item 3 "atingindo pico de $+0{,}357$ p.p. em $h = 5$"`

**Por que importa**: só afeta a precisão dos números.

**Sugestão**: corrigir os números e declarar a convenção de horizonte da FEVD.

**Severidade**: Minor
**Confiança**: 5. Verificado por execução.

### W12: Histórico de especificações e ajuste por múltiplos testes limitado

**Problema**: A especificação-base mudou entre versões depois que se viram os resultados (sem dummies na v2, com dummies na v3). O texto informa isso, o que é mérito. Mas o número total de estimativas é grande: três coeficientes, sete horizontes, oito especificações, a versão assimétrica e a PTAX por regime. E a correção cobre apenas horizontes dentro de cada coeficiente da base.

**Evidence Anchor**: `text: §4.4 "controla a probabilidade de ao menos uma rejeição falsa na família"`

**Por que importa**: a taxa de erro em toda a análise é maior do que a família de Holm sugere.

**Sugestão**:
- Declarar quais testes são confirmatórios (por exemplo, γ^12 e o Wald da diferença em h=12 e h=24) e quais são exploratórios.
- Para os confirmatórios, reportar bandas simultâneas.

**Severidade**: Minor
**Confiança**: 4.

---

## Comentários detalhados

### Questões de pesquisa e hipóteses
H1, H1' e H2 estão bem formuladas. A distinção entre as implicações (i), (ii) e (iii) é a forma correta de colocar a pergunta. H2 é declarada "quase mecânica", e seu conteúdo está na magnitude e na transmissão, o que é apropriado. Falta dizer qual teste de H1 é confirmatório (W12).

### Desenho da pesquisa
O desenho combina SVAR recursivo mensal com LPs de estado, uma combinação padrão e adequada para explorar o tema. Os pontos críticos são três: o choque, identificado num modelo linear, é usado de forma condicional ao estado (W4); a Selic média mensal no Cholesky (W5); e a restrição de defasagens comuns entre regimes (W1).

### Amostra
Os dados mensais vão de 2005-03 a 2026-08. Para o platô, isso dá cerca de quatro episódios utilizáveis (W3). Em h=24, a amostra efetiva é N=228, com 105 observações no platô, para cerca de 50 regressores. O tamanho efetivo para comparar regimes é pequeno, e o texto precisa refletir isso no tom das conclusões.

### Coleta de dados
As séries vêm do SGS e do Olinda, e os códigos são informados. Não pude conferir o CSV contra a fonte. Recomendo informar a data de extração (vintage) e se o IBC-Br e o comprometimento de renda são revisados.

### Métodos de análise
- O VAR em níveis com p=6 tem escolha pouco justificada (W2, W10).
- O HAC com janela h+1 é otimista (W3).
- Não há bootstrap nem bandas simultâneas.
- A sazonalidade é tratada só nas LPs (W6).
- O problema do regressor gerado não é material, e eu verifiquei isso (W7).

### Apresentação dos resultados
Os resultados nulos são reportados por completo, o que é mérito. Faltam:
- IC e MDE da diferença entre regimes (W1);
- a resposta da Selic por regime (W4);
- a sensibilidade a p (W2).

A Figura 5 deveria mostrar a diferença β_alto − β_mod com banda sup-t.

### Reprodutibilidade
É excelente para as LPs (S1). O SVAR depende de download. Sugiro um modo offline que leia o CSV.

### Falácias metodológicas detectadas
- **Endogeneidade do estado:** o indicador é função da variável de política (W9). O texto a reconhece em parte.
- **Ausência de evidência tratada como evidência de ausência:** é o caso do Wald sem poder (W1).
- **Caminho de especificações bifurcado:** troca da especificação-base e escolha de p (W2, W12).
- **Causalidade reversa em γ^h:** declarada pelos autores.

Não detectei p-hacking deliberado. O texto rebaixa resultados que a revisão enfraqueceu.

### Suporte das conclusões pelos dados
- **Conclusão 1 (H2):** sustentada.
- **Conclusão 2 (H1):** "β_mod^24 estável" não é sustentada (W2), e "H1 não encontra apoio" deveria ser "inconclusivo" (W1).
- **Conclusão 3 (H1'):** o ponto estimado é sustentado, mas a significância depende da inferência (W3). A ressalva sobre a interpretação é adequada.

---

## Perguntas aos autores
1. Qual é o IC 95% de β_alto^h − β_mod^h em h=12 e h=24, e qual efeito mínimo o teste detectaria com 80% de poder? A conclusão sobre H1 se mantém quando lida como "inconclusiva"?
2. Como fica a resposta da Selic, nível e acumulada, em cada regime? Normalizando a resposta da inflação pela Selic acumulada em cada regime, a comparação entre regimes muda?
3. Por que p=6, quando BIC e HQIC escolhem p=2 e o AIC escolhe p=5? Como β_mod^24 se comporta com p ∈ {2, 4, 9, 12} e com lag augmentation?
4. Os resultados de H2 e de γ^h se mantêm com a meta Selic de fim de mês (SGS 432) ou com surpresas de futuros de DI em torno das reuniões do Copom?

---

## Questões menores (abaixo do limiar de achado)

### Linguagem e notação
- Em §4.5, a especificação assimétrica é chamada de "item 2", o que se confunde com o item 2 da §4.5 dos resultados. Numerar as equações da especificação assimétrica.
- Eq. (13): explicitar que os controles Y_{t−k} não interagem com o estado.

### Tabelas e figuras
- Tabela 2: a linha da PTAX não tem erros-padrão. Incluí-los ou dizer por que faltam.
- Tabela 3: incluir uma coluna com IC para a inflação também, não só para J^fam.
- Figura 5: incluir um painel com a diferença entre regimes e bandas simultâneas.

### Formatação
- Tabela 5: a nota "em negrito, p<0,05" deveria dizer que o p-valor é pontual, sem Holm.
