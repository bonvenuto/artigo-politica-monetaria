# Resposta ao Roteiro de Revisão da 2ª rodada

Esta carta responde, item por item, ao roteiro de `decisao_editorial_rodada2.md` (RR2-01 a RR2-38). As referências a seções e tabelas seguem a numeração do manuscrito revisado.

Legenda: **feito**; **parcial** (com justificativa); **não feito** (com justificativa).

## Itens `must_fix`

| ID | Status | O que mudou | Onde |
|---|---|---|---|
| RR2-01 | feito | A contribuição 1 deixou de dizer "tornamos o nulo informativo". Agora ela delimita o que dados mensais agregados conseguem identificar, citando MDE, limites unilaterais e a dependência de p, da medida de juros, do limiar e da especificação. O título da §4.5 passou a ser "O que os dados identificam sobre H1". A Conclusão diz que "a evidência mensal agregada não arbitra a controvérsia". A aritmética fiscal virou "observação analítica". | §1, §4.5, §6 |
| RR2-02 | feito | Resumo PT/EN, introdução e Conclusão: o nulo está condicionado à especificação-base e ao sup-Wald calibrado. O MDE foi redefinido como "detectadas com probabilidade inferior a 80%", e a frase fala do efeito "em 24 meses". γ̂ aparece com "não significativa a 5% sob bootstrap (p = 0,093)". A interagida aparece com o p calibrado. O resumo PT tem 248 palavras. | resumos, §1, §6 |
| RR2-07 | feito | A Tabela 1 tem linhas separadas para "carga de juros" (Sim: repasse à taxa implícita) e para "endividamento insustentável", com citação literal do ensaio (p. 5) e o status "testado, sem efeito detectável". Foi incluída a linha da Curva de Phillips horizontal (ensaio, p. 5–6 e 9), com o status "não identificado". | Tabela 1 |
| RR2-08 | feito | Foi retirada a equivalência "tese = ω ≈ 1". A §2.2 cita a regra do ensaio (p. 9: a inflação "é inercial" e, no longo prazo, converge para i − g, cerca de 5% com i = 7,5%), que corresponde a ω ≈ 0 no primeiro ano, e informa ω* ≈ 0,51–0,61. A frase de "tensão" foi substituída por: alívio fiscal e ausência de pressão inflacionária exigem, juntos, um canal de demanda pouco operante, que o artigo não testa. | §2.2, §6 |
| RR2-09 | feito | A Eq. (fiscal_scen) ganhou o termo dos indexados ao IPCA, x_IPCA·Δg/(1+g). A participação vem do RMD de set./2026: 23,59% da DPF (16,5% do PIB). A Tabela de insumos traz indexados, prefixados e cambiais. Com x = 36,1% e corte gradual, ω = 0,5 dá −0,03 e ω = 1 dá +1,03, como R2b-2 havia indicado. | Eq. (fiscal_scen), Tabelas 2–3, `aritmetica_fiscal.py` |
| RR2-10 | feito | O Painel B da Tabela 3 (regime permanente) usa Δī = 7,5 − ī e dá −3,97 p.p. com o custo da DPF e −4,27 com o da DPMFi. O texto atribui os "cerca de 4% do PIB" ao ensaio (p. 11) e mostra que eles correspondem ao Painel B com ω = 0. A legenda separa o primeiro ano do regime permanente. "2,3%" foi suprimido do corpo e a pontuação "DBGG Terceiro" foi corrigida. | Tabela 3, §2.2 |
| RR2-14 | feito | A frase "reestimamos tudo" foi substituída pela lista do que usa a SGS 432: as LPs de estado, a LP linear da inflação e H2. H2 com a meta Selic dá +0,27 por 1 p.p. (p = 0,012; Holm 0,035; +0,071 por DP), na §4.7, item 3. A LP linear da inflação dá −0,14 em h = 24 (p = 0,012; Holm 0,071), na §4.6. | §3.2, §4.6, §4.7 |
| RR2-17 | feito | Os Wald da LP interagida (h = 12 e 24) passaram a integrar o bootstrap recursivo sob a nula (B = 999). Em h = 24, p_boot = 0,107 (iid) e 0,104 (wild), com quantil de 95% de 16,1 contra a estatística observada de 10,35. O Painel B da Tabela 8 traz p_boot e o quantil. Resumo, introdução e Conclusão usam o p calibrado. Para C4 (H2) o bootstrap sob a nula linear não se aplica, porque essa nula não implica efeito nulo de J; o arquivo de resultados registra a justificativa e uma calibração do tamanho do teste HAC. | §4.5, Tabela 8, `inferencia_regimes.py` §D |
| RR2-18 | feito | A grade está descrita por inteiro. Em h = 24, a diferença é positiva nos 11 limiares e significativa em 4. No limiar de 14% (31 meses; 22 em h = 24): +4,53 (p = 0,001) em h = 24 e +3,17 (p = 0,040) em h = 12. γ̂¹² cai a +0,95 a 13% e desaparece acima disso. "γ̂¹² é estável" virou "estável em p e no Painel A, exceto juro real ex ante e limiares acima de 13%". A Conclusão traz a mesma ressalva. | §4.5, §4.6 item 3, §6 |
| RR2-27 | feito | O texto usa "taxa implícita" no resumo, na §4.7 e na Conclusão. A §3.1 declara que a documentação pública não descreve o método do numerador. A §4.7 discute o repasse implícito alto e as explicações possíveis (taxas correntes no numerador; composição), que os dados não distinguem. "Mais robusto" foi qualificado: o resultado é estatisticamente robusto, documenta o repasse convencional da Selic e não é evidência sobre a tese. O pico robusto está em 12–18 meses. | resumo, §3.1, §4.7, §6 |
| RR2-28 | feito | Todas as linhas da Tabela 11 incluem seis defasagens da própria variável dependente; a versão antiga está em `resultados/canal_familias.txt`. O endividamento deixa de responder (−0,17 em h = 12, p = 0,76), e "desalavancagem" foi retirada como resultado. O p_Holm de J/E agora é ≤ 0,003 (NW) e ≤ 0,024 (EWC), conferido com o arquivo de resultados. | Tabela 11, §4.7 itens 1–2, §6 |
| RR2-29 | feito | A assimetria foi rebaixada a resultado exploratório, com p_Holm = 0,34 e h = 0 reportados (b⁺ = +0,14, b⁻ = −0,17). A decomposição em s e \|s\| foi incluída: o termo \|s\| vale +0,16 em h = 0 (p < 0,001) e não é significativo depois. A resposta da Selic difere por sinal (+2,5 contra +1,6 p.p. em 12 meses). A §5.2 e a Conclusão não afirmam assimetria em cortes, e o episódio de fev.–ago./2026 saiu como evidência. | §4.7 item 4, §5.2, §6 |
| RR2-36 | feito | `artigo_anonimo.tex` compila a versão de submissão (`artigo_anonimo.pdf`), sem nome, URL nem o apêndice de versões; a busca por "Bonvenuto", "github" e "Mudanças em relação" no PDF não retorna nada. Os rótulos de versão ("VERSÃO 4", "v3", "versão 3", "Número da versão 3") saíram de scripts e resultados. A versão com nome e filiação continua sendo o arquivo principal, por decisão do autor. O apêndice de mudanças permanece só nessa versão. | preâmbulo, `artigo_anonimo.tex`, `scripts/`, `resultados/` |

## Itens `should_fix`

| ID | Status | Observação |
|---|---|---|
| RR2-03 | feito | "Dominância fiscal" foi trocada por "interação monetária-fiscal" nas palavras-chave PT/EN. |
| RR2-04 | feito | O 1º parágrafo cita Barth–Ramey e Ravenna–Walsh para o canal de custos e descreve Loyo, Blanchard e Favero–Giavazzi como literatura de interação monetária-fiscal. |
| RR2-05 | feito | A citação de Cochrane (2011, JPE) foi trocada por Cochrane (2001, *Econometrica* 69(1), 69–116). |
| RR2-11 | feito | A grade inclui ω = −0,5, com a ressalva de que custos de desancoragem e de prêmio não são modelados. |
| RR2-12 | feito | (a) A grade x × Δi é citada no texto e está no arquivo de resultados. (b) O termo bola-de-neve também aparece na base NFSP/DLSP (taxa implícita de 14,8%; 4,6 p.p.). (c) A linha "51,6% da DBGG" foi justificada como limite superior que inclui as compromissadas. |
| RR2-15 | feito | O texto identifica as duas regressões do teste F: só dummies, F(11,246) = 8,08, p < 10⁻¹¹; equação do VAR, F(11,204) = 4,12, p < 10⁻⁴. `estimacao_svar_lara_resende.py` imprime ambas. |
| RR2-19 | feito | O bootstrap tem variante wild (Rademacher) para γ¹², os Wald e a interagida, com p-valores praticamente iguais. A Selic simulada fica negativa em 4,1–4,4% das réplicas; descartá-las não altera os p. |
| RR2-20 | feito | O sup-Wald também é reportado com trimming de 15%, que exclui o limiar de 14%: em h = 24, a estatística cai de 11,4 para 4,9 (p = 0,458). |
| RR2-21 | feito | A Tabela 8 traz o MDE com EP EWC (2,70 e 3,32; 0,42 e 0,52 por DP). Não foi construída uma banda simultânea para a diferença. |
| RR2-22 | feito | O texto reporta os limites unilaterais por DP em h = 12 e 24 e a inversão de sinal entre esses horizontes. Também reporta a frequência sob a nula: mesmo sinal nos 11 limiares em 25% das réplicas; dif12 < 0 e dif24 > 0 em 16%. |
| RR2-23 | feito | A Tabela 10 traz p EWC para β_mod^24 e para os Wald, e as Tabelas 7 e 10 trazem o N por regime. O argumento "por acaso" foi substituído pela observação de que os testes são correlacionados. |
| RR2-24 | feito | O texto descreve todos os episódios: queda da inflação durante quatro platôs e repique nos 12 meses após o fim dos quatro completos, com a ressalva de endogeneidade. |
| RR2-30 | feito | A amostra trimestral é reportada nas três fases (h = 12: +0,55, +0,77 e +0,19) e com o choque agregado por trimestre (+0,42 a +0,49; p ≤ 0,009). |
| RR2-31 | feito | Os mecanismos aparecem como hipóteses. O MDE de S (1,13) e de J − S (0,76) em h = 12 é reportado. |
| RR2-32 | não feito | A comparação com as taxas médias de juros às pessoas físicas e o ICC exige novas séries do SGS e uma decisão sobre os códigos. O texto declara que os dados não distinguem repreço de composição. |
| RR2-33 | feito | A nota do BCB de 28/12/2021 (`bcb2021notacredito`) é citada. A Tabela 4 traz a transformação de 29035 (nível) e de 29037 (nível e ln). |
| RR2-34 | feito | A Limitação 6 diz que a RNDBF restrita exclui as rendas de propriedade e que o indicador mede carga bruta, não redistribuição líquida. |
| RR2-37 | parcial | `coleta_series_complementares.py` grava a data de extração no momento do download e o SHA-256 dos CSVs. `data/safra_dados.txt` só muda de formato quando o script for executado de novo; não baixamos os dados outra vez para não alterar a amostra. |
| RR2-38 | parcial | Foram acrescentadas as páginas de Blanchard (49–80), Favero–Giavazzi (85–108) e Minella (605–635), e as de Arida et al. foram corrigidas para 265–294 (Crossref). Não foram obtidos os URLs individuais dos posts de Cochrane nem o URL oficial do RMD. |

## Itens `consider`

| ID | Status | Observação |
|---|---|---|
| RR2-06 | não feito | A literatura adicional não foi incorporada nesta rodada. |
| RR2-13 | não feito | Não foi feita a simulação de rolagem com o cronograma de vencimentos; o ritmo de rolagem está informado. |
| RR2-16 | feito | "Confirmatórios" virou "principais (pré-especificados nesta versão, sem pré-registro)". |
| RR2-25 | parcial | A grade de limiares e o padrão de sinal sob a nula cobrem parte da curva de especificações; não há figura dedicada. |
| RR2-26 | não feito | Não foi construído indicador de estado independente da Selic; o item consta nas limitações. |
| RR2-35 | feito | A resposta de J por p.p. de Selic (≈ 0,2 em h = 12) e a comparação aproximada com o ciclo de 2021–23 (+2,3 a +2,5 previstos contra +2,6 observados) estão na §4.7. |

## Números que mudaram nesta rodada

- **Bootstrap sob a nula:** B passou de 399 para 999. Os p-valores ficaram assim:
  - γ̂¹²: 0,073 → 0,093;
  - Wald da base em h = 12 e h = 24: 0,368 e 0,236 → 0,380 e 0,268;
  - sup-Wald (h = 12 e h = 24): 0,335 e 0,128;
  - quantil de 95% de \|t_γ\|: 3,44.
- **LP interagida:** em h = 24, o p calibrado é 0,107. O p assintótico de 0,001 deixa de ser lido como significativo.
- **Famílias:**
  - J/E em 12 meses: +6,4%, e não +8,2%, depois que os controles foram padronizados;
  - endividamento: não significativo;
  - p_Holm de J/E: ≤ 0,003, e não "< 0,001".
- **Fiscal, com o termo dos indexados:**
  - ω = 1, corte gradual: +1,53 → +1,03;
  - ω = 0,5: +0,22 → −0,03;
  - regime permanente com ω = 0: −4,98 → −3,97, e com ω = 1: +0,20.

## Correções após a conferência editorial e a conferência numérica

A conferência editorial (`conferencia_editorial.md`) apontou três `must_fix` parciais, um problema bloqueante (B1) e afirmações desta carta que não correspondiam ao manuscrito. A conferência numérica (`conferencia_numerica.md`) apontou uma divergência de números e descrições imprecisas. Tudo foi corrigido no manuscrito.

**Correções desta carta.**
- Na primeira versão, RR2-02 e RR2-17 diziam que o resumo, a introdução e a Conclusão usavam o p calibrado da especificação interagida, o que **não era verdade**. Agora usam: p = 0,107 (0,11 no resumo).
- RR2-12(a) dizia que a grade x × Δi era "citada no texto", mas o texto só remetia ao arquivo. A §2.2 agora traz os valores dos extremos da grade.
- RR2-29: a primeira versão omitia a normalização pela Selic média, agora reportada.

**Itens corrigidos no manuscrito:**

| Item | Correção |
|---|---|
| B1 (C4/H2) | A §4.7 reporta a calibração do tamanho do teste: o NW rejeita a resposta verdadeira em 21% das réplicas a 5%; o valor crítico calibrado de \|t\| é 3,06, contra t = 2,76; p ≈ 0,08. A §3.4 explica por que C4 não usa o bootstrap sob a nula. "Estatisticamente mais robusto" passou a "o mais robusto entre especificações, marginal em 12 meses com valor crítico calibrado", no resumo, na introdução, na §4.7 e na Conclusão. A magnitude é dada para 12 a 18 meses (0,07 a 0,09 p.p. por DP). |
| RR2-01 | A contribuição 1 menciona a falta de poder (cinco episódios de platô). |
| RR2-02 / RR2-17 | Resumo, introdução e Conclusão trazem o p calibrado da especificação interagida. |
| M1 | O IC da diferença entre as razões normalizadas foi corrigido para [−0,38; +0,07] em 12 meses e [−1,75; +1,06] em 24 meses. |
| M2 | O −0,14 da LP com a meta Selic é a inflação mensal em t + 24, e não a acumulada. |
| M3 | Assimetria: o texto agora usa a Selic média (+2,21 e +2,23), reporta J normalizada (+0,41 e −0,01) e descreve o termo \|s\| como "marginal de 9 a 24 meses". |
| M4 | Na Tabela 1, a linha "carga de juros" passou a "formulação deste artigo, a partir do ensaio (p. 5)". |
| M6 | A grade x × Δi aparece no texto da §2.2. |
| M8 | `s_firm` sai em texto romano. |
| M10 | A Limitação 6 justifica a omissão da comparação com as taxas médias e o ICC (RR2-32). |
| Numéricos | "5,7%" do ensaio citado com página (p. 4) e reconciliado com os 5,4 p.p. "Cerca de 5%" vem do crescimento real de 2,5% que o ensaio adota (p. 11). "6,4%" e "14,8%" passaram a pontos logarítmicos. A descrição da SGS 4189 foi uniformizada. |

**Não feito:**
- **M5:** o nome do autor e os marcadores REV-/RR2- continuam nos comentários dos scripts. Se o pacote de replicação for anexado à submissão anônima, eles devem ser retirados antes. O PDF anônimo não contém nenhum dos dois.
- **M9:** os URLs individuais dos posts de Cochrane e o URL oficial do RMD continuam sem confirmação.
