# Relatório de Re-revisão — Revisor 3 (Perspectiva: finanças das famílias, crédito e transmissão via balanço das famílias)

- **Manuscrito**: "O Patamar dos Juros Altera a Transmissão da Política Monetária? Evidência de Projeções Locais Dependentes de Estado e do Comprometimento de Renda das Famílias no Brasil (2005–2026)"
- **Rodada**: 2ª (re-revisão). Uso a mesma régua do meu relatório da 1ª rodada (W1–W7).
- **Escopo**: H2, §2.3, §3.1 (construção das séries), §4.7 e Tabela 11 (no .tex, `tab:servico`), as passagens sobre famílias no resumo, na §5.2, nas Limitações e na Conclusão, e as implicações distributivas.
- **Ponto cego declarado**: não avalio a identificação do choque nem H1/H1′, salvo quando afetam H2.
- **Material usado**: somente o pacote `r3/`. Não há carta de resposta do autor, então verifiquei cada item diretamente no .tex, no PDF, nos scripts e nas saídas.

---

## Resumo

A revisão respondeu ao essencial do que pedi na 1ª rodada:
- **Construção das séries**: a §3.1 agora documenta como as séries são feitas (estimativa do BCB, renda MM3, Denton-Cholette, retropolação, revisões) e informa a safra (9/11/2026).
- **Decomposição**: a Tabela 11 decompõe o comprometimento em $J$, $A$, $S$, a série sem habitacional (29035), $E$ e $\ln(J/E)$, todos com o mesmo choque-base.
- **Redação**: "não se transmite" virou "não se detecta", e a §5.2 deixou de fazer afirmações distributivas sem dados.
- **Reprodutibilidade**: reexecutei `canal_familias.py` numa cópia em `replica/` e a saída é **idêntica byte a byte** a `resultados/canal_familias.txt`.

O núcleo de H2 (a taxa efetiva implícita sobe após uma surpresa positiva) ficou mais robusto do que o artigo mostra. Ele resiste às defasagens próprias e ao choque identificado pela meta Selic (SGS 432), que o artigo não reporta para H2.

Três novos resultados da §4.7, porém, dependem de escolhas frágeis:
1. **Desalavancagem**: a "desalavancagem parcial" desaparece quando se controla pelas defasagens próprias do endividamento.
2. **Serviço total**: a "ausência de efeito no serviço total" vem de um desenho em que só $J$ tem as próprias defasagens como controle.
3. **Assimetria**: a assimetria tem $p_{Holm}=0{,}34$ em todos os horizontes e mistura um efeito de magnitude do choque, que aparece já em $h=0$, com primeiros estágios assimétricos da Selic. Mesmo assim, ela é levada à §5.2 e à Conclusão como afirmação sobre cortes de juros.

Além disso, o repasse implícito da Selic à taxa média do estoque (cerca de 0,8 em 12 meses) é implausivelmente alto para uma carteira majoritariamente prefixada. Isso reabre a pergunta, não respondida, sobre como o BCB estima o numerador.

São problemas de reanálise localizada e de calibragem do texto, não de fundamento. **Recomendação: Minor Revision (com reanálise), confiança 4.**

---

## Verificação do roteiro

| ID | Status | Evidência |
|---|---|---|
| **REV-32** (construção de 29033/29034, safra, MA(2), h=0) | **Resolvido**, com ressalvas (ver R3b-5 e R3b-6) | A §3.1 descreve a estimativa do BCB, a RNDBF restrita em MM3, Denton-Cholette, a retropolação pré-2012, a substituição das 19879–19882 e as revisões de 2024–2026, e cita `bcb2021nt55`. Conferi a NT 55: MM3 (nota 25), PME antes de 2012 (nota 14), "revisões substanciais". A safra está em `data/safra_dados.txt` e na Tabela 4. A §4.7, item 3, traz NW $h+3$, EWC, a amostra trimestral não sobreposta e o corte em 2023:12, e discute $h=0$. **Ressalvas**: (i) o método do **numerador** (taxa do estoque ou das concessões, prazo, anuidade) continua sem documentação, e a NT 55 trata só da renda; (ii) a substituição das 19879–19882 não tem fonte, porque a nota de imprensa de 28/12/2021 não é citada; (iii) o resultado trimestral depende do mês de amostragem (R3b-5). |
| **REV-33** (decomposição J, A, S, E, J/E; controle pelo estoque) | **Resolvido** quanto ao critério. A interpretação tem problema novo (R3b-1) | A Tabela 11 reúne as cinco séries e $\ln(J/E)$ com o mesmo choque. H2 com seis defasagens de 29037: +0,41 ($p=0{,}021$) em $h=12$. Reproduzido. |
| **REV-34** (mesmo choque; amortização; teste J−S; "não se detecta"; mecanismos) | **Resolvido** quanto ao critério. Problema novo de especificação (R3b-1) e de interpretação (R3b-4) | O mesmo choque é usado para todas as séries. Como $J+A=S$ vale exatamente nos dados (erro 0,000; conferi em ago/2026: 10,92 + 18,07 = 28,99), o teste $J-S$ equivale à resposta de $-A$, e a legenda e o texto dizem isso corretamente. A expressão "não se transmite" não aparece mais no PDF. Os três mecanismos (Price, alongamento e portabilidade, concessões) são citados. |
| **REV-35** (descrição de $\eta_{pos}$; 29035) | **Resolvido** | A §2.3 separa estoque repactuado de concessões (fluxo), cita a TR no imobiliário e os tetos (cheque especial a 8% a.m. desde 2020; rotativo limitado a 100% do principal desde 2024). A série 29035 está na Tabela 11. A extensão por modalidade (taxas e saldos) não foi feita, mas ela era sugestão, não critério. |
| **REV-36** (título "Fragilidade" na Figura 2) | **Resolvido** | O painel (b) se chama "Comprometimento de renda com juros (SGS 29033)". `grep -i fragilidade` não encontra nada nos scripts nem no .tex. |
| **REV-37** (episódio 2021–2023; heterogeneidade) | **Resolvido** | O último parágrafo da §4.7 compara com 2021–2023 (J de 7,1% para 9,7%; Selic de 1,9% para 13,65%; números conferidos na saída) e cita o EE 80. Falta uma conta que ligue a LP ao episódio (R3b-7). |
| **REV-39** (alternativas e partes interessadas, se a §5.2 for mantida) | **Resolvido** (por justificativa de omissão) | A §5.2 declara que os efeitos distributivos sobre devedores, detentores de pós-fixados e fundos de previdência "são questões que este artigo não estuda". |
| **REV-05** (minha parte: "expressivamente"; poupadores e fundos) | **Resolvido**, mas a §5.2 ganhou uma afirmação nova sem base suficiente (R3b-2) | "expressivamente" não aparece mais, e a afirmação sobre poupadores e fundos DI foi retirada. A nova frase "Os efeitos de um corte sobre as famílias também não são simétricos aos de uma alta" passa da evidência. |
| **REV-11** (J por DP e por p.p. de Selic acumulada) | **Parcial** | Os efeitos por DP estão no resumo, na Tabela 6 (coluna "LP por 1 DP"), na §4.7 e na Conclusão (0,07 p.p. em 12 meses). Não há conversão por p.p. de Selic acumulada (R3b-7). |
| **REV-06** (literatura de finanças das famílias) | **Parcial** | Há um parágrafo de uma frase (Drehmann et al. 2015, Cloyne et al. 2020, Auclert 2019). Não discute a literatura do canal de caixa (Flodén et al.; Di Maggio et al.) nem Drehmann, Juselius e Korinek sobre a defasagem entre crédito novo e serviço, que é justamente o arcabouço dos mecanismos citados na §4.7. |
| **REV-15** (alternativa SGS 432 "para as LPs lineares, de estado e H2") | **Parcial** para H2 | A §3.2 diz que "reestimamos tudo" com a SGS 432, mas não há resultado de H2 com esse choque em `resultados/` nem no texto. Reestimei: $J$ em $h=12$ = +0,27 ($p=0{,}012$; Holm 0,035); $h=18$ = +0,40 (Holm 0,001); $\ln(J/E)$ em $h=12$ = +5,4 ($p<0{,}001$). **H2 sobrevive**, mas com magnitude cerca de 35% menor, e isso deve ser reportado. |
| **REV-13** (lista de testes confirmatórios) | **Resolvido** para H2 | (C4) = $J$ em $h=12$, NW 0,006, EWC 0,015, Holm 0,012. |
| **REV-10** (resumo ≤ 250 palavras) | Fora do meu foco | Não conferi a contagem. |

---

## Problemas novos

### R3b-1 — Os controles diferem entre $J$ e as demais séries da Tabela 11, e a "desalavancagem" e a "ausência no serviço total" dependem disso
**Severidade: maior.**
**Localização**: Tabela 11; §4.7, itens 1 e 2; Conclusão, 2º parágrafo ("com desalavancagem parcial"); `canal_familias.py` (`X0` usa só `lag_controls(v)`).

**Evidência**: $J$ está no VAR, então a LP de $J$ controla pelas próprias seis defasagens. $A$, $S$, 29035, $E$ e $\ln(J/E)$ não estão no VAR, e suas LPs **não** incluem as próprias defasagens, apesar de serem séries em nível muito persistentes. A comparação entre $J$ e $S$ fica, portanto, entre especificações diferentes. Acrescentei seis defasagens da própria variável dependente:

| Série | Especificação do artigo ($h=12$) | Com defasagens próprias ($h=12$) | Outros horizontes, com defasagens próprias |
|---|---|---|---|
| $S$ (29034) | +0,31 (ep 0,43; $p=0{,}46$) | +0,40 ($p=0{,}32$) | $h=3$: +0,38 ($p=0{,}039$); $h=18$: +0,86 ($p=0{,}029$); Holm mínimo 0,18 |
| 29035 | +0,39 ($p=0{,}37$) | +0,51 ($p=0{,}20$) | $h=3$: $p=0{,}013$; $h=18$: $p=0{,}011$ |
| $E$ (29037) | −1,00 ($p=0{,}11$) | −0,17 ($p=0{,}76$) | $100\ln E$: −0,3 ($p=0{,}84$) em $h=12$ |
| $100\ln(J/E)$ | +8,2 | +6,4 ($p<0{,}001$) | Robusto |

**Consequências**:
- A queda do endividamento, base da frase "parcialmente compensado por desalavancagem", **não sobrevive** ao controle pelas próprias defasagens. Já no texto atual ela não é significativa após Holm, e mesmo assim entra na Conclusão como resultado.
- No serviço total, as respostas de $S$ e de 29035 se aproximam das de $J$ e passam a ser significativas a 5% (NW) em $h=3$ e $h=18$. Continuam não significativas após Holm.
- A conclusão "não se detecta" sobrevive formalmente, mas é frágil. Os erros-padrão "três vezes maiores" de $S$ refletem em parte a omissão da dinâmica própria.
- O resultado sobre a taxa efetiva é o único robusto, e é ele que deve ancorar H2.

**Correção**:
1. Padronizar a Tabela 11 com as defasagens da variável dependente em todas as linhas (ou reportar as duas versões).
2. Retirar "com desalavancagem parcial" da Conclusão e do item 1 da §4.7, ou qualificar como não robusto.
3. Reportar o efeito mínimo detectável da resposta de $S$ e da diferença $J-S$. Pelas minhas contas, em $h=12$ o MDE com 80% de poder é de cerca de 1,2 p.p. para $S$ e 0,86 p.p. para $A$, várias vezes a resposta de $J$. É o mesmo tratamento que o artigo dá ao nulo de H1.

### R3b-2 — A assimetria de H2 não é robusta e é usada como afirmação sobre cortes de juros
**Severidade: maior.**
**Localização**: §4.7, item 4; §5.2 ("Os efeitos de um corte sobre as famílias também não são simétricos aos de uma alta: surpresas negativas não reduziram $J^{fam}$"); Conclusão ("Surpresas negativas não reduzem o comprometimento").

**Evidência**:
1. **Holm**: os p-valores de simetria (0,33; 0,14; 0,057; 0,085; 0,095; 0,065 em $h=3,\dots,24$) dão **$p_{Holm}=0{,}343$ em todos os horizontes**. O texto aplica Holm a todos os coeficientes de cabeçalho, mas não a esta família.
2. **Efeito em $h=0$**: na saída do próprio artigo, em $h=0$, $b^+=+0{,}144$ ($p=0{,}003$) e $b^-=-0{,}171$ ($p=0{,}001$), com simetria rejeitada a $p=0{,}000$. Surpresas **de qualquer sinal** elevam $J$ no impacto, horizonte em que, segundo o próprio texto, não há repreço (média móvel e repreço gradual). Reescrevendo como $a\,s + b\,|s|$: em $h=0$, $b=+0{,}157$ ($p<0{,}001$). Em $h=9$–$24$, $b\approx a$ ($p$ entre 0,06 e 0,10). Ou seja, a "assimetria" é em boa parte um efeito da *magnitude* da surpresa sobre $J$. Esse efeito não aparece na Selic ($|s|$: $p=0{,}76$ em $h=12$) nem na taxa implícita $\ln(J/E)$ ($p=0{,}88$). Isso sugere confusão com períodos turbulentos de surpresas grandes, e não um mecanismo de repreço.
3. **Primeiros estágios diferentes**: depois de $s^+$, a Selic fica cerca de 2,5 p.p. acima até $h=18$. Depois de $s^-$, a resposta é de +1,59 ($p=0{,}37$) em $h=12$ e muda de sinal em $h=18$ (−1,11). A comparação de $J$ não normaliza pela trajetória da Selic, a mesma objeção de REV-14 para a inflação.
4. **Surpresas não são cortes**: a §3.3 lembra corretamente que $\text{Shock}^-$ não é um corte. A §5.2 trata as duas coisas como equivalentes.
5. **Episódio de 2026**: o dado descritivo (Selic de 14,90 para 13,94 e $J$ de 10,58 para 10,92 entre fev. e ago. de 2026) é coerente com uma resposta **simétrica e defasada**. A LP linear tem pico em $h=18$, e a Selic subiu ao longo de 2025. Ele não discrimina a hipótese de assimetria.

**Correção**:
- Reportar $p_{Holm}$ da simetria e a decomposição $s$/$|s|$.
- Normalizar pela resposta da Selic a $s^+$ e a $s^-$.
- Rebaixar a assimetria a resultado exploratório.
- Retirar da §5.2 e da Conclusão as afirmações sobre cortes, ou reescrevê-las como "não há evidência de que surpresas baixistas reduzam rapidamente $J$; a assimetria não é robusta".
- Retirar o dado de 2026 como evidência de assimetria ou apresentá-lo como coerente com a defasagem.

### R3b-3 — O repasse implícito à taxa média do estoque é alto demais para ser repreço; falta o método do numerador
**Severidade: maior** (afeta a interpretação "pela alta da taxa efetiva" no resumo).
**Localização**: Resumo; §4.7, item 1; §3.1.

**Evidência**:
- Com o choque de 1 p.p., $J/E$ (média de 21,3%) sobe **+1,62 p.p.** em $h=12$, enquanto a Selic está +2,04 p.p. acima no mesmo horizonte (LP). O repasse ao custo médio do **estoque** seria de cerca de 0,8 em 12 meses.
- Isso é difícil de conciliar com a própria §2.3: o consignado, os veículos e o imobiliário são majoritariamente prefixados ou atrelados à TR, e o rotativo e o cheque especial têm repasse fraco e tetos regulatórios.
- Repasse dessa ordem sugere uma de duas coisas. (a) O BCB estima os juros do numerador com taxas correntes (de concessão), e não com as taxas contratadas do estoque. Nesse caso, H2 mede em parte a fórmula do indicador. (b) Há mudança de composição, com recuo de linhas baratas e permanência de linhas caras, que $J/E$ não separa de repreço.
- Há ainda um componente de denominador: $J$ usa renda em MM3, e $E$ usa a renda acumulada em 12 meses. Logo, $J/E$ inclui a razão $Y_{12m}/(12\,Y_{3m})$, que se move com o crescimento da renda.
- A pergunta 3 do meu relatório anterior, sobre como o BCB estima juros e amortização, segue sem resposta.

**Correção**:
1. Documentar, com fonte do BCB (DSTAT/metadados SGS), como se estimam juros e amortização.
2. Comparar a resposta de $J/E$ com a das taxas médias de juros e do Indicador de Custo do Crédito das pessoas físicas no SGS (códigos a verificar pelo autor), separando concessões e estoque.
3. Trocar "pela alta da taxa efetiva" por "pela alta da taxa implícita (juros/estoque), que combina repreço, composição e o método de estimação do BCB", até que (1) e (2) sejam feitos.

### R3b-4 — Os mecanismos explicam uma diferença entre $J$ e $S$ que os dados não estabelecem
**Severidade: menor.**
**Localização**: §4.7, item 2.

**Evidência**: a resposta de $A$, que é exatamente $S-J$, nunca é significativa, e as estimativas pontuais de $S$ têm magnitude parecida com as de $J$. Os dados não mostram que "o serviço total responde menos". Os três mecanismos (Price, alongamento, concessões) aparecem como explicação de um fato não estabelecido, e nenhum deles é testado: concessões e prazos médios não são estimados.

**Correção**: apresentá-los como hipóteses compatíveis com uma resposta de $A$ que não se consegue medir com precisão. Se possível, estimar a resposta das concessões às pessoas físicas e do prazo médio das carteiras (séries públicas do SGS).

### R3b-5 — O teste trimestral não sobreposto depende do mês de amostragem e é reportado na fase menos favorável
**Severidade: menor.**
**Localização**: §4.7, item 3 ("+0,19, $p=0{,}43$"); `canal_familias.py` (`qmask` = meses 3, 6, 9, 12).

**Evidência**: com o mesmo desenho, mudar a fase altera o resultado de $h=12$ de forma substancial:

| Fase (meses) | $h=12$ | $h=18$ |
|---|---|---|
| mar/jun/set/dez (a reportada) | +0,19 ($p=0{,}43$) | +0,82 ($p=0{,}008$) |
| jan/abr/jul/out | +0,55 ($p=0{,}09$) | +0,64 ($p=0{,}018$) |
| fev/mai/ago/nov | +0,77 ($p=0{,}004$) | +0,84 ($p<0{,}001$) |

**Leitura**: a robustez à MA(2) é melhor do que o texto sugere, mas o teste trimestral tem pouco poder e varia muito com a fase. Para o teste confirmatório C4, isso importa.

**Correção**: reportar as três fases ou a média delas, ou agregar o choque por trimestre (soma dos três choques mensais) em vez de descartar dois terços deles.

### R3b-6 — H2 com o choque da SGS 432 não é reportado; documentação residual
**Severidade: menor.**
**Localização**: §3.2 ("reestimamos tudo com a meta Selic"); §3.1; `referencias.bib`.

**Evidência e correção**:
- H2 com a SGS 432: +0,27 em $h=12$ (Holm 0,035), cerca de 35% abaixo da base. Incluir essa linha na Tabela 11 ou no item 3 da §4.7. Ela reforça o rótulo "mais robusto".
- Citar a nota de imprensa do BCB de 28/12/2021 para a substituição das séries 19879–19882, já que a NT 55 só trata do denominador.
- Na Tabela 4, a linha "29035; 29037 — nível, ln" não diz qual transformação cabe a qual série. Corrigir.

### R3b-7 — Falta traduzir a magnitude para ciclos reais
**Severidade: menor** (resíduo de REV-11).
**Localização**: §4.7, último parágrafo; Tabela 6.

**Evidência**: o artigo dá a resposta por DP (0,07 p.p.), mas não por p.p. de Selic na trajetória: $J_h/\text{Selic}_h$ ≈ 0,12 em $h=6$ e 0,21 em $h=12$. Também não confronta a LP com o ciclo de 2021–2023. Uma conta simples ajuda o leitor de política: o choque de 1 p.p. gera uma trajetória com pico de cerca de 3 p.p. e eleva $J$ em 0,43–0,57 p.p.; escalado para +11,75 p.p., isso dá cerca de +1,7 a +2,2 p.p., contra +2,6 p.p. observados. A comparação fora da amostra de choques é aproximada (não linearidade, crítica de Lucas), mas mostra que a magnitude é economicamente coerente.

**Correção**: reportar a resposta por p.p. de Selic na trajetória e essa comparação, com a ressalva de que ela é aproximada.

### R3b-8 — A implicação distributiva continua de um lado só
**Severidade: menor.**
**Localização**: §1.1 (parágrafo "Finanças das famílias"); Limitação 6.

**Evidência**: a §5.2 agora se abstém corretamente. Mas o artigo cita Auclert (2019) sem lembrar que o denominador de 29033 (RNDBF restrita) exclui as rendas de propriedade. O indicador mede apenas a carga bruta dos devedores e nada diz sobre a redistribuição líquida entre devedores e credores.

**Correção**: uma frase na Limitação 6 basta.

---

## Pontos fortes

1. **Reprodutibilidade exemplar no bloco das famílias**: o script roda e reproduz a saída byte a byte, e a identidade $J+A=S$ é verificada no código.
2. **Resposta séria ao roteiro**: todos os critérios de aceite de REV-32 a REV-37 foram cumpridos no sentido literal, com documentação correta da NT 55 (conferida), safra, mesmo choque, série 29035, "não se detecta" e Figura 2 corrigida.
3. **O resultado central de H2 é sólido**: a resposta de $J$ resiste a EWC, NW $h+3$, ao corte em 2023:12, ao controle pelo estoque e, nas minhas checagens, à SGS 432 (Holm 0,035). A taxa implícita sobe de forma robusta, inclusive com as defasagens próprias.
4. **Proporcionalidade na §5.2**: o artigo deixou de afirmar efeitos distributivos sem dados e trata H2 como evidência sobre surpresas marginais.
5. **Honestidade sobre o nulo do serviço total** ("ausência de evidência, e não evidência de ausência") e menção explícita à heterogeneidade (EE 80).

---

## Recomendação

- [ ] Accept
- [x] **Minor Revision** (com reanálise localizada no bloco das famílias)
- [ ] Major Revision
- [ ] Reject

**Confiança: 4.** A área é central para mim. O método exato do numerador do BCB continua não confirmado nas fontes públicas.

**Justificativa**: os pontos Major da 1ª rodada (W1, W2, W3, W5) foram resolvidos. Os problemas novos maiores (R3b-1 a R3b-3) não derrubam H2. Eles exigem padronizar os controles da Tabela 11, rebaixar a desalavancagem e a assimetria a resultados exploratórios ou não robustos, retirar da §5.2 e da Conclusão a afirmação sobre cortes, e qualificar "taxa efetiva". São tarefas de poucos dias, com dados e código já no pacote. Se o autor mantiver a assimetria como afirmação sobre cortes na §5.2 e na Conclusão sem as correções de R3b-2, eu passaria a recomendar Major.

**Checagens do revisor**: scripts em `replica/scripts/r3_checks.py` e `replica/scripts/r3_checks2.py`. São exploratórios e não constam do manuscrito.
