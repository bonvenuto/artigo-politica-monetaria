# Relatório de Re-revisão (2ª rodada): Revisor 2, Domínio

**Manuscrito:** "O Patamar dos Juros Altera a Transmissão da Política Monetária? Evidência de Projeções Locais Dependentes de Estado e do Comprometimento de Renda das Famílias no Brasil (2005–2026)"
**Data:** 9 de novembro de 2026
**Papel:** Revisor 2 (política monetária e fiscal, TFNP, neo-fisherianismo, economia brasileira). Uso a mesma régua da 1ª rodada (`rodada1/r2_dominio.md`).
**Material verificado:** `.tex`, PDF, `referencias.bib`, `scripts/aritmetica_fiscal.py`, `resultados/aritmetica_fiscal.txt`, `data/base_complementar_bcb.csv` e o ensaio `ensaio_eu_acuso.pdf`, lido na íntegra. Não há carta de resposta, então conferi cada item diretamente. Fontes externas: API do SGS (série 5793) e busca na web (RMD de setembro de 2026, referências).

---

## Resumo

A revisão é substancial e, no meu domínio, quase toda na direção certa. O título, o resumo e as palavras-chave agora se organizam em torno da pergunta e do resultado nulo. O canal da dívida pós-fixada está declarado como não testado. O "modelo fechado" virou arcabouço motivador. O canal de expectativas foi renomeado como solvência e prêmio de risco. A §5.1 deixou de atribuir ao ensaio a exclusão do canal cambial e declara que o desenho não discrimina as teorias. A §5.2 foi reduzida ao que a evidência não informa. Os ciclos de 2011–12 e 2016–18 aparecem com os níveis corretos do primário, que conferi no SGS 5793. A afirmação de que a *duration* zero "elimina" o efeito de valor presente desapareceu. A aritmética fiscal passou a ser feita em termos reais, com tabela de insumos documentada e cenários de repasse ω.

Restam quatro problemas no meu domínio. Um é novo e de interpretação. Os outros são de cálculo ou de citação.
1. **Leitura do ensaio no mapeamento para ω (R2b-1, maior).** O texto equipara a tese de Lara Resende a "ω próximo de 1". O próprio ensaio dá outra leitura: a inflação de longo prazo é i − g real, que com i = 7,5% dá cerca de 5%, acima dos 4,2% atuais. Pela lógica do ensaio, portanto, o corte é sobretudo uma queda do juro real (ω ≈ 0), não uma queda fisheriana da inflação. A "tensão" anunciada na §2.2 e na Conclusão depende dessa leitura seletiva.
2. **Indexação das NTN-B (R2b-2, maior).** Na Eq. (fiscal_scen), toda a dívida que não é Selic é tratada como prefixada. Os títulos indexados ao IPCA (23,6% da DPF) têm custo nominal que cai junto com a inflação. Isso superestima a piora em ω > 0. Com ω = 0,5, os cenários passam de "+0,22 / +0,02" para cerca de "−0,03 / −0,25".
3. **Limite superior "4% a 5% do PIB" (R2b-3, maior).** O número aplica o corte da Selic (−6,44 p.p.) a todo o estoque, cujo custo médio é 12,63%. A conta correta (12,63% → 7,5%) dá cerca de 4,0% do PIB, que, aliás, é o número do próprio ensaio.
4. **Citação de Cochrane (2011) (R2b-4, menor).** O texto cita Cochrane (2011, JPE, sobre regras de Taylor) como fonte de que a maturidade da dívida determina o efeito de curto prazo. Essa não é a referência certa.

Recomendação: **Minor Revision**, com confiança 4.

---

## Verificação do roteiro (itens de domínio)

| ID | Status | Evidência |
|---|---|---|
| REV-01 (título, resumo, palavras-chave) | **Resolvido** | O título é uma pergunta e não tem mais "Dívida Pós-Fixada". A 1ª frase de resultado do resumo é o nulo de H1 ("Não encontramos diferença..."). As palavras-chave (PT e EN) não trazem nome de pessoa. O resumo termina com "O canal da dívida pública pós-fixada não é testado". |
| REV-03 (canal da dívida não testado) | **Resolvido** | §2.1: "nenhuma especificação estimada inclui a composição da dívida, o resultado nominal ou o prêmio soberano. O canal da dívida pós-fixada, portanto, **não é testado**". Repetido no resumo, na Tabela 1, na Limitação 4 e na Conclusão. A frase "sintetiza a dependência de estado testada" foi removida. |
| REV-04 (fechado; condensar; item 3) | **Resolvido** | "fechado" não aparece mais. A §2 se declara não resolvida ("é preciso *supor* que θ e ρ′ crescem com o patamar"). O item 3 (r* = g + ρ(b*), atribuído a ABL) foi removido, e ABL aparece na literatura com a evidência contrária de Gonçalves et al. (2007). |
| REV-05 (§5.2 enxuta, Δi único) | **Resolvido** | A §5.2 tem um parágrafo, não contém "expressivamente" nem detalhes do CFMN, e trata os efeitos distributivos como "questões que este artigo não estuda". O Δi é único: 13,94% → 7,5% (6,44 p.p.) na §2.2 e na §5.2. A Conclusão não defende a redução. |
| REV-06 (literatura) | **Parcial** | Foram incluídos Sargent–Wallace (1981), Leeper (1991), Woodford (2001), Tanner–Ramos (2003), Minella (2003), Gonçalves–Holland–Spacov (2007), Drehmann et al., Cloyne et al. e Auclert. Os blogs só aparecem como relato do ensaio. Continuam faltando Sims (1994) e Woodford (1995), canônicos da TFNP (Woodford 2001 é aceitável); Minella e Souza-Sobrinho (2013), que é diretamente relevante para H2 porque aponta o canal de juros das famílias; Ayres et al. (2021); e Garín–Lester–Sims (2018). Nada disso é bloqueante. |
| REV-08 (números da introdução com fonte) | **Resolvido** | Os números foram para a Tabela de insumos fiscais, com código SGS ou RMD e data. A discrepância 5,7% × 5,05% é explicada (diferencial antes da divisão por 1+g, custo de junho). Conferi DBGG 82,87, DLSP 69,27, juros 8,86 (= 9,48 − 0,62), primário 0,62, Selic 13,94, custo da DPF 12,63, DPMFi 13,03, prazo 4,10 e vencimentos em 12 meses de 19,95% contra o script e o RMD. Todos batem. |
| REV-09 (§5.1) | **Resolvido** | O título passou a ser "O que os resultados dizem sobre os canais". O texto reconhece que "o ensaio de 2026 também adota o canal cambial" e lista os critérios que separariam as teorias (primário × nível do juro, prêmio soberano, dívida cambial). Há a frase "**O desenho deste artigo não discrimina entre essas teorias.**" A Tabela 6 continua na §5 (detalhe). |
| REV-21 (aritmética em termos reais) | **Resolvido, com erro de execução** | Há a Eq. (fiscal_scen) e a Tabela de cenários ω ∈ {0; 0,5; 1}. Os 2,3% aparecem só como número incorreto da versão anterior. A decomposição, porém, trata as NTN-B como prefixadas (R2b-2). |
| REV-22 (insumos, bases, Selic × custo médio, gradualismo, grade) | **Parcial** | O que foi feito: tabela de insumos; distinção entre Selic e custo médio (o corte parte de 13,94%); corte gradual (Δī₁ = −3,22); grade x × Δi no `resultados/aritmetica_fiscal.txt` (não no texto). O que falta: (i) o termo bola-de-neve ainda aplica o custo da DPF à DBGG (12,63% × 82,87 ≈ 10,5% do PIB contra 8,86% de juros NFSP observados), e as NFSP líquidas, que estão na tabela, não são usadas em fluxo nenhum; (ii) a linha "51,6% da DBGG" não tem justificativa econômica. A exposição relevante na DBGG é a DPF flutuante mais as compromissadas (cerca de 7–8% do PIB, número a confirmar), o que dá ≈ 44% do PIB. A proximidade com 42,8% é coincidência e deve ser explicitada; (iii) a grade de sensibilidade não aparece no artigo. |
| REV-23 (4% como limite superior condicional) | **Resolvido no texto, número errado** | "é um *limite superior*: supõe inflação rígida, prêmio a termo nulo e convergência de toda a curva para 7,5%, e a rolagem levaria anos". O valor de −4,98 está superestimado (R2b-3). |
| REV-23b (cronograma de rolagem e prêmio a termo) | **Parcial** | Há só menção qualitativa (20% vencem em 12 meses, prazo médio de 4,1 anos). Não há simulação com cronograma nem cenários de prêmio. Aceitável como `should_fix`, dado o rótulo de limite superior. |
| REV-24 (*duration*/valor presente) | **Resolvido** | Não há mais "sem elevar o valor presente" no resumo PT/EN. A §2.2 diz que "o corte valoriza a parcela prefixada e indexada a preços, cerca de metade da DPF. A dívida curta reduz o canal de repique da TFNP; não o elimina". Isso confere com o RMD (21,1% + 23,6% + 3,7% ≈ 48%). |
| REV-25 (rótulo TFNP) | **Resolvido** | "Esse canal é de solvência e de prêmio de risco; não é a equação de valoração da TFNP". |
| REV-26 (ciclos) | **Resolvido** | §5.2: superávit de 3,5% → 2,1% do PIB (ago/2011–out/2012) e déficits entre 1,4% e 2,9% (2016–18), com a EC 95. Conferi no SGS 5793: −3,53 em ago/2011, −2,07 em out/2012 e déficit entre 1,42 e 2,87 de out/2016 a mar/2018. Está correto. O texto declara "serve apenas como ilustração" e "não sustentam conclusão". |
| REV-27 (componentes × hipóteses) | **Resolvido, com ressalvas de fidelidade** | A Tabela 1 existe. H1 é declarada "não uma previsão explícita" do ensaio. O canal de custos é atribuído a Barth–Ramey e Ravenna–Walsh, não ao ensaio. O componente neo-fisheriano está marcado como "Não". As ressalvas estão em R2b-5. |
| REV-28 (γ̂ como Fisher) | **Resolvido** | H1′ "não discrimina entre teorias". A especificação pelo juro real *ex ante* é destacada como "a mais próxima da tese". "Mais estável" e a contagem de votos foram removidos. |
| REV-29 (IC-Br) | **Resolvido** | A base usa a SGS 29042 (US$) e a 27574 aparece como "em R$" na robustez (especificação 10, correlação dos choques de 0,993). A FEVD reporta as duas versões. Isso confirma o meu diagnóstico da 1ª rodada. |
| REV-30 (Cochrane 2026) | **Parcial** | A atribuição está corrigida: "o ensaio relata ainda que posts recentes... defendem reduzir os juros encurtando a maturidade", e nenhuma tese sobre a Selic é atribuída a Cochrane. O `.bib` declara honestamente "citados conforme Lara Resende (2026)". Ainda não há os URLs completos dos dois posts, só o domínio. |
| REV-31 (higiene do `.bib`) | **Resolvido (quase)** | Não há entradas órfãs (as 45 chaves são citadas). Pastore, Serrano e resende2014 saíram. Blanchard e Favero–Giavazzi estão nas versões publicadas (MIT Press, 2005). `lopes1979causas` (TD PUC-Rio n.º 6, 1979) confere com o PDF da PUC-Rio. Uribe e García-Schmidt–Woodford estão descritos corretamente. `\date` está fixa. Faltam as páginas de Blanchard (2005), Favero–Giavazzi (2005) e Minella (2003). |
| REV-03b (`consider`) | Não feito | Aceitável. Está declarado como limitação. |
| REV-39 (`consider`) | Não feito | A §5.2 não menciona alternativas de gestão da dívida (alongar ou encurtar). É aceitável com a §5.2 enxuta. |

---

## Verificação de referências

| Entrada | Verificação | Situação |
|---|---|---|
| sargent1981some, leeper1991equilibria, woodford2001fiscal, sims2011stepping, uribe2022neo, garciaschmidt2019low, mcleay2020optimal, tenreyro2016pushing, ramey2018government, plagborg2021local, nakamura2018high, barth2001cost, ravenna2006financial, cloyne2020monetary, auclert2019monetary, lazarus2018har, montielolea2019/2021, kilian1998small, jorda2005estimation, tanner2003fiscal, goncalves2007can, cespedes2008monetary, holm1979simple, lavoie1995, hein2007, drehmann2015how | Volume, número e páginas conferidos de memória ou com fonte | Corretas |
| **cochrane2011determinacy** | A entrada (JPE 119(3), 565–615) está correta, mas é **citada para a afirmação errada** | Ver R2b-4 |
| cochrane2026reasons | Só o domínio; fonte secundária declarada | URL incompleto (REV-30) |
| lopes1979causas | TD n.º 6, PUC-Rio, out./1979 (o ensaio diz "1980") | Correta |
| blanchard2005fiscal, favero2005inflation | Volume MIT Press 2005, correto | Faltam páginas |
| minella2003monetary | RBE 57(3) | Faltam páginas (605–635) |
| arida2005credit | Capítulo do mesmo volume; páginas 265–293 não verificadas | A confirmar |
| loyo1999tight | Manuscrito da KSG/Harvard, 1999 | Aceitável (texto não publicado) |
| resende2017/2020/2022 | Portfolio-Penguin; títulos conferem | Corretas |
| tesouro2026rmd | RMD de set./2026. Conferi participação flutuante de 51,60%, índices de preços 23,59%, prefixados 21,14%, custo de 12,63% e prazo de 4,10 anos | Correta. Falta URL |
| bcb2021nt55, bcb2020ee80 | Fora do meu domínio, não verifiquei | — |

**Ausentes relevantes:** Cochrane (2001), "Long-term debt and optimal policy in the fiscal theory of the price level", *Econometrica* 69(1), 69–116, que é a referência certa para maturidade × efeito de curto prazo; Sims (1994); Woodford (1995); Minella e Souza-Sobrinho (2013).

---

## Problemas novos

### R2b-1. O mapeamento "tese do ensaio = ω próximo de 1" é uma leitura seletiva do ensaio. **Maior**
- **Localização:** §2.2, 1ª conclusão ("corresponde a ω próximo de 1, cenário em que a razão piora no primeiro ano"); Conclusão, 3º parágrafo ("em tensão com a tese de que a dívida curta permitiria reduzir juros e inflação ao mesmo tempo"); §5.2.
- **Evidência:** A frase citada ("a inflação inicia imediatamente sua convergência para um nível mais baixo dado pela taxa de juros", p. 8 do ensaio) diz que não há repique, isto é, ω não negativo. Ela não diz que a inflação cai um para um no primeiro ano. O ensaio também afirma: (a) "No longo prazo a inflação converge para a diferença entre a taxa básica de juros e a taxa de crescimento real" (p. 9); (b) a redução da dívida "restabelece a credibilidade fiscal..., condição para que a inflação venha a convergir" (p. 11), o que descreve convergência posterior e condicionada; (c) "No curto prazo, a relação... pode ser inversa" (p. 9). Com i = 7,5% e crescimento real de 2,5% (números do próprio ensaio, p. 11), a inflação de "longo prazo" do ensaio é de cerca de **5%**, acima do IPCA de 4,22% da Tabela de insumos. Na lógica interna do ensaio, portanto, a transição 13,94% → 7,5% é uma **queda do juro real** (de cerca de 9,3% *ex post* para algo próximo de g), com inflação inercial ou estável, ou seja, ω ≈ 0. A redução da inflação para 3% só viria depois, com a eliminação do *spread* de 2 p.p. A tensão real é outra. O alívio do ensaio exige ω ≈ 0, e ω ≈ 0 com queda de cerca de 6 p.p. do juro real só é não inflacionário se o canal de demanda for desprezível (curva de Phillips horizontal, que o ensaio afirma na p. 6). É exatamente esse o componente que a literatura (McLeay–Tenreyro, citado pelo próprio artigo) diz não poder ser inferido de formas reduzidas.
- **Correção:** Apresentar as duas leituras: (i) ω → 1 no horizonte em que a proposição neo-fisheriana valesse, o que anula o alívio na razão; (ii) ω ≈ 0 no primeiro ano, a leitura coerente com i − g = 5% e com inflação inercial, em que o alívio existe mas depende de κ·σ ≈ 0. Reescrever a frase da Conclusão de acordo: o alívio fiscal e a ausência de pressão inflacionária exigem juntos um canal de demanda inoperante, hipótese que este artigo não testa. Incluir na Tabela 1 a linha "Curva de Phillips horizontal / recessão não reduz a inflação" (ensaio, p. 6 e p. 9), com o status "Não identificado; a resposta do IBC-Br e a FEVD não informam κ (McLeay–Tenreyro)".

### R2b-2. A Eq. (fiscal_scen) trata os títulos indexados ao IPCA como prefixados. **Maior**
- **Localização:** Eq. (fiscal_scen), Tabela de cenários, texto ("com ω = 1..., o custo real da parcela atrelada à Selic não muda, e o da parcela prefixada sobe"), `aritmetica_fiscal.py`, função `db`.
- **Evidência:** O segundo termo penaliza todo o estoque b pela queda de g_nom. Mas as NTN-B (23,59% da DPF, ≈ 16,5% do PIB) têm custo nominal IPCA + cupom, que cai junto com a inflação. Só os prefixados (21,1%) e a dívida cambial ficam com custo real maior. Recalculei com os insumos do próprio script, somando o termo +x_IPCA·Δπ/(1+g):

| x | Corte | ω = 0 | ω = 0,5 (manuscrito → corrigido) | ω = 1 (manuscrito → corrigido) |
|---|---|---|---|---|
| 36,1% PIB | gradual | −1,08 | +0,22 → **−0,03** | +1,53 → **+1,03** |
| 36,1% PIB | imediato | −2,17 | +0,44 → **−0,05** | +3,06 → **+2,07** |
| 42,8% PIB | gradual | −1,28 | +0,02 → **≈ −0,25** | +1,33 → **≈ +0,81** |

- O sinal em ω = 1 se mantém, e a conclusão qualitativa de que o alívio diminui com ω também. Mas o "ponto de equilíbrio" se desloca de ω ≈ 0,5 para ω acima de 0,5, e as magnitudes de ω = 1 caem cerca de 1/3.
- **Correção:** Decompor b em Selic (x), IPCA (x_IPCA, que acompanha π com defasagem de um a dois meses), prefixada e cambial, e refazer a tabela. A frase "o da parcela prefixada sobe" está correta, mas a tabela não a implementa.

### R2b-3. O "limite superior" de 4–5% do PIB está superestimado em cerca de 1 p.p. **Maior** (correção trivial)
- **Localização:** Tabela de cenários, linha "Todo o estoque refinanciado ao novo patamar" (−4,98); §2.2 ("economia de cerca de 4% a 5% do PIB"); `aritmetica_fiscal.py` (`db(dbgg, dbgg, dI, w)` com dI = 7,5 − 13,94).
- **Evidência:** Refinanciar todo o estoque a 7,5% reduz o **custo médio** de 12,63% para 7,5% (−5,13 p.p.), não a Selic de 13,94% (−6,44 p.p.). A conta é 82,87 × (−5,13)/107,22 = **−3,96 p.p.** do PIB. Mesmo com o custo da DPMFi (13,03%), dá −4,27. O próprio ensaio fala em "quase 13% para 7,5%... cerca de 4% do PIB" (p. 11). Logo, o "limite superior" do manuscrito é mais generoso que o próprio ensaio. As linhas de ω = 0,5 e ω = 1 dessa linha herdam o erro (e, com R2b-2, também a indexação).
- **Correção:** Usar Δī = 7,5 − ī e reportar "cerca de 4% do PIB". Além disso, a legenda da Tabela diz "no primeiro ano", mas a última linha é um regime permanente após anos de rolagem. É preciso separar ou ajustar a legenda.

### R2b-4. Cochrane (2011) citado para maturidade da dívida. **Menor**
- **Localização:** §1.1, "Interação monetária e fiscal": "\citet{sims2011stepping} e \citet{cochrane2011determinacy, cochrane2023fiscal} mostram que, sob a TFNP, a maturidade da dívida determina a magnitude do efeito de curto prazo".
- **Evidência:** "Determinacy and identification with Taylor rules" (JPE 2011) trata da identificação de regras de Taylor no modelo novo-keynesiano, não da maturidade da dívida.
- **Correção:** Trocar por Cochrane (2001, *Econometrica* 69(1), 69–116) ou manter apenas Sims (2011) e Cochrane (2023, caps. sobre dívida de longo prazo).

### R2b-5. A Tabela 1 está incompleta em dois componentes do ensaio. **Menor**
- **Localização:** Tabela `tab:componentes`.
- **Evidência:** (a) Falta a proposição central do ensaio de que "a Curva de Phillips tornou-se praticamente horizontal" e de que "recessão e capacidade ociosa não reduzem a inflação" (p. 6 e p. 9). É a premissa que sustenta o alívio em ω ≈ 0 (ver R2b-1). (b) A linha "Juros altos elevam a carga de juros das famílias" parafraseia o ensaio, que fala em "endividamento insustentável das famílias e das empresas" (p. 5). O artigo testa a carga de juros (H2, confirmada), mas a sua própria Tabela 9 mostra que o **endividamento cai** (cerca de −1 p.p. da renda, n.s.) após o aperto. A tabela marca "Sim" sem registrar que a afirmação literal do ensaio sobre endividamento não encontra apoio.
- **Correção:** Acrescentar a linha (a) e desdobrar (b) em "carga de juros: Sim, confirmada" e "endividamento: testado, sem apoio (desalavancagem)".

### R2b-6. Atribuição genérica no 1º parágrafo da Introdução. **Menor**
- **Localização:** §1, 1º parágrafo: "Uma tradição crítica sustenta que... a taxa básica... passa a operar também por canais que pressionam preços: o custo financeiro das empresas, o custo da dívida pública e... a percepção de solvência \citep{loyo1999tight, blanchard2005fiscal, favero2005inflation}".
- **Evidência:** Nenhum dos três trata do custo financeiro das empresas, e Blanchard e Favero–Giavazzi não pertencem a uma "tradição crítica" à ortodoxia monetária: são análises convencionais de dominância fiscal.
- **Correção:** Citar Barth–Ramey e Ravenna–Walsh para o canal de custos e descrever Loyo, Blanchard e Favero–Giavazzi como literatura de interação fiscal-monetária, não como "tradição crítica".

### R2b-7. Questões menores de redação e consistência
- §2.2, 2ª conclusão: falta ponto final em "à metade da DBGG Terceiro" (o erro aparece também no PDF).
- O termo bola-de-neve (4,2 p.p. do PIB por ano) aplica o custo da DPF à DBGG. Vale reportar ao lado a versão em NFSP (8,86% do PIB de juros sobre DLSP de 69,27%, taxa implícita de 14,8%, já calculada no script) para que o leitor veja a diferença entre as bases (resíduo de REV-22).
- A grade de sensibilidade x × Δi está em `resultados/` e não no texto. Uma frase basta.
- `tesouro2026rmd` sem URL; `cochrane2026reasons` sem URL dos posts.
- Fora do meu domínio, mas visível: a compilação está com `\anonimofalse` (nome, GitHub e Apêndice B "Mudanças em relação às versões anteriores" aparecem no PDF). Para submissão anônima, REV-07 continua pendente.

---

## Pontos fortes

1. **Fidelidade muito melhor ao ensaio.** A Introdução descreve o ensaio com precisão (motor da dívida, LFT contra repique, neo-Fisher de longo prazo, posts de Cochrane "relatados" pelo ensaio). A §5.1 reconhece que o ensaio adota o canal cambial. A Tabela 1 separa com honestidade o que é e o que não é testado, e o "Não" para o componente neo-fisheriano, a dívida e a proposta é o correto.
2. **Aritmética fiscal transparente e reproduzível.** Os insumos têm código SGS ou RMD e data, que conferi contra a API e o RMD. O script reproduz as tabelas. A explicação de por que os 2,3% do PIB da versão anterior eram nominais, imediatos e sem repasse é exemplar.
3. **A pergunta de fundo foi incorporada corretamente.** O alívio na razão só existe se o juro real cair. É a contribuição conceitual mais útil do artigo para o debate brasileiro, desde que o mapeamento para o ensaio seja corrigido (R2b-1).
4. **A *duration* foi tratada corretamente:** "reduz o canal de repique; não o elimina", com a fração de cerca de metade da DPF conferida no RMD.
5. **Os ciclos históricos têm números corretos** e são rebaixados a ilustração.
6. **A literatura de fundamentos e a brasileira melhoraram** (Sargent–Wallace, Leeper, Woodford, Tanner–Ramos, Minella, Gonçalves et al.), incluindo a evidência contrária a ABL no lugar certo.

---

## Recomendação

**Minor Revision.** Confiança: **4** (área central; não verifiquei NT 55 nem EE 80, que são de outro domínio).

Todos os itens `must_fix` do meu domínio foram resolvidos no texto. Os problemas restantes estão concentrados na §2.2. R2b-2 e R2b-3 são erros de cálculo corrigíveis no script em menos de um dia e não mudam a conclusão qualitativa. R2b-1 exige reescrever duas ou três frases e acrescentar uma linha na Tabela 1. Nenhum deles afeta o núcleo empírico nem as conclusões sobre H1 e H2. Não vejo necessidade de nova rodada completa de revisão se o editor conferir esses quatro pontos.

---

## Fontes consultadas
- API do SGS/BCB, série 5793 (2011–2018), consultada em 9 nov. 2026.
- [Poder360: Com rombo de R$ 90,2 bi em setembro, dívida pública bate R$ 9,38 tri](https://www.poder360.com.br/poder-economia/com-rombo-de-r-902-bi-em-setembro-divida-publica-bate-r-938-tri/) e [Apresentação RMD setembro 2026](https://static.poder360.com.br/uploads/2026/10/Apresentacao-RMD-Setembro-2026.pdf) (composição: flutuante 51,60%; índices de preços 23,59%; prefixados 21,14%; câmbio cerca de 3,7%).
- [Poder360: Custo da dívida pública sobe para 12,63% ao ano em setembro](https://www.poder360.com.br/poder-economia/custo-da-divida-publica-sobe-para-1263-ao-ano-em-setembro/)
- [Câmara/CONOF: Raio-X da dívida, agosto de 2026](https://www2.camara.leg.br/orcamento-da-uniao/raio-x-do-orcamento/2026/raio-x-da-divida-agosto-de-2026/view) (compromissadas; valor de agosto não confirmado)
- [PUC-Rio, TD n.º 6 (Lopes e Lara Resende, 1979)](https://www.econ.puc-rio.br/uploads/adm/trabalhos/files/td6.pdf)
- Ensaio de Lara Resende (PDF do pacote), lido na íntegra.
