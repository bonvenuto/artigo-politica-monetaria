# Conferência editorial da 3ª versão — Roteiro RR2-01…RR2-38

**Manuscrito**: "O Patamar dos Juros Altera a Transmissão da Política Monetária? Evidência de Projeções Locais Dependentes de Estado e do Comprometimento de Renda das Famílias no Brasil (2005–2026)"
**Papel**: editor responsável (conferência editorial, sem nova rodada de pareceres)
**Data**: 9 de novembro de 2026
**Base**: somente o pacote `conferencia_v5/editorial/` (roteiro, carta, `manuscrito/`). Nada foi modificado em `manuscrito/`.

**Decisão: Accept com correções menores (aceite condicional).** O aceite definitivo depende de três complementos de texto em itens `must_fix` (RR2-01, RR2-02 e RR2-17) e da correção do problema bloqueante B1. Todos são só de texto, e os números já estão em `resultados/`. A condição de R3 sobre RR2-29 **foi cumprida**.

---

## 0. Método

- **.tex**: li `artigo_svar_lara_resende.tex` por inteiro (670 linhas). As linhas citadas abaixo são as desse arquivo. `artigo_anonimo.tex` só define `\ANONIMO` e inclui o arquivo principal.
- **PDFs**: extraí os dois com `pdftotext -layout`. Busquei nome, URL e apêndice no texto e também nos *streams* descomprimidos e nos metadados do PDF anônimo. Procurei referências não resolvidas ("??", "(?)") e comparei o texto dos dois PDFs com o .tex.
- **Resultados**: conferi cada número citado nos itens abaixo contra `resultados/*.txt`.
- **Scripts**: conferi `canal_familias.py` (função `lp`, bloco da meta Selic), `estimacao_svar_lara_resende.py` (teste F das sazonais), `coleta_series_complementares.py` (safra e SHA-256) e a presença de rótulos e de nome em `scripts/`, `resultados/` e `data/`.
- **Ensaio**: extraí `ensaio_eu_acuso.pdf` com `pdftotext` e confirmei a paginação pelos rodapés "n / 14". Conferi todas as citações literais e páginas usadas no manuscrito.
- **Aritmética fiscal**: recalculei a Tabela de cenários, inclusive ω\*, a partir da Eq. (`fiscal_scen`).
- Não reexecutei os scripts econométricos.

---

## 1. Itens `must_fix`

### Resumo

| ID | Veredito | Em uma linha |
|---|---|---|
| RR2-01 | **Parcialmente atendido** | "Nulo informativo" saiu e a Conclusão tem a frase pedida. A contribuição 1 menciona o MDE, mas não a falta de poder. |
| RR2-02 | **Parcialmente atendido** | (a)–(d) atendidos. O resumo, a Introdução e a Conclusão não trazem o p calibrado da interagida (0,107). |
| RR2-07 | **Atendido** (ressalva menor) | Linhas separadas, citação literal (p. 5) e linha da Curva de Phillips. A linha "carga de juros: Sim" ainda é atribuída ao ensaio. |
| RR2-08 | **Atendido** | A equivalência ω ≈ 1 saiu. O texto cita a regra de longo prazo (p. 9) e ω\* ≈ 0,5–0,6, e a "tensão" foi reescrita. |
| RR2-09 | **Atendido** | Termo dos indexados na equação, participação de 23,59% (RMD set./2026) e −0,03 / +1,03, conferidos. |
| RR2-10 | **Atendido** | Painel B com −3,97 (−4,27 pela DPMFi) atribuído ao ensaio (p. 11). Legenda separada, "2,3%" e "DBGG Terceiro" eliminados. |
| RR2-14 | **Atendido** | A §3.2 descreve o que os scripts fazem. H2 com a SGS 432 é reportado. Há um rótulo errado na LP linear (M2). |
| RR2-17 | **Parcialmente atendido** | O Painel B traz p_boot e o quantil. A justificativa de C4 está só em `resultados/`, e a calibração que ela produziu é desfavorável e não foi reportada (B1). |
| RR2-18 | **Atendido** | Grade completa, limiar de 14% com o número de meses, "γ̂¹² estável" qualificado também na Conclusão. |
| RR2-27 | **Atendido** | "Taxa implícita" no resumo, na §4.7 e na Conclusão. O método declarado não público na §3.1. "Mais robusto" qualificado, com pico em 12–18 meses. |
| RR2-28 | **Atendido** | Controles padronizados, "desalavancagem" retirada como resultado, p_Holm ≤ 0,003, conferido. |
| RR2-29 | **Atendido** (ressalva menor) | §5.2 e Conclusão sem afirmação sobre cortes. A §4.7 traz p_Holm = 0,34, h = 0 e o termo em \|s\|. O episódio de 2026 foi retirado. |
| RR2-36 | **Atendido** no critério literal (ressalva) | PDF anônimo limpo. Sem "VERSÃO", "versão 3" ou "v3". Mas o nome do autor está em 9 scripts, e há rótulos de rodada REV-/RR2- (M5). |

**Contagem**: 10 atendidos (RR2-07, 08, 09, 10, 14, 18, 27, 28, 29, 36), 3 parcialmente atendidos (RR2-01, 02, 17) e nenhum não atendido.

### Detalhamento

**RR2-01 — Parcialmente atendido.**
- Critério 1, ausência de "nulo informativo": a busca por `informativ` no .tex não retorna nada. ✔
- Critério 3, frase na Conclusão: l. 638 traz "a evidência mensal agregada não arbitra a controvérsia". ✔ O título da §4.5 passou a ser "O que os dados identificam sobre H₁" (l. 444).
- Critério 2, "a contribuição 1 menciona o MDE e a falta de poder": a contribuição 1 (l. 73) diz "Reportamos o intervalo da diferença entre regimes, o efeito mínimo detectável e limites unilaterais". O MDE aparece como quantidade reportada, mas a contribuição não diz que o poder é baixo nem que "nem a tese nem a sua negação têm apoio", como pedia a coluna "O que fazer". Essa informação está só no parágrafo seguinte (l. 75: "mas o teste tem pouco poder").
- **Correção**: acrescentar uma oração à contribuição 1, por exemplo: "…e mostramos que o desenho não tem poder para detectar diferenças da ordem do próprio efeito da política, de modo que os dados não sustentam a hipótese nem a sua negação".
- A 3ª contribuição foi rebaixada a "observação analítica" (opcional, cumprido).

**RR2-02 — Parcialmente atendido.**
- (a) O resumo condiciona o nulo à especificação-base e ao teste calibrado sobre a grade (l. 46). A única ocorrência de "em nenhum horizonte" (l. 439) está restrita à especificação-base. ✔
- (b) "maiores que o efeito estimado no regime moderado em 24 meses" (l. 46). ✔
- (c) "não é significativa a 5% sob bootstrap (p = 0,093)" (l. 75). Confere com `inferencia_regimes.txt` §D: p = 0,093. ✔
- (d) O MDE está definido corretamente: "diferenças de até cerca de 0,4 p.p. … seriam detectadas com probabilidade inferior a 80%" (l. 46) e "Diferenças menores que 1,5 a 2,7 p.p. …" (l. 446). Confere com §A: 0,228–0,420 por DP, e 0,518 com EWC. ✔
- Resumo PT com 248 palavras e EN com 246 (contagem própria). ✔
- (e) **Não cumprido**: o critério exige que "a frase sobre a interagida traga o p calibrado". O resumo (l. 46: "perdem significância quando calibradas"), a Introdução (l. 75: "não resistem à calibração por bootstrap") e a Conclusão (l. 638: "perdem significância quando calibradas") não dão o p. O valor 0,107 só aparece na §4.5 (l. 479) e no Painel B (l. 471).
- **Correção**: acrescentar "(p calibrado = 0,107)" na Introdução e na Conclusão. No resumo, que está a 2 palavras do limite, trocar a construção por algo como "(controles interagidos, p calibrado de 0,11; limiar de 14%)" e cortar palavras em outro ponto.

**RR2-07 — Atendido, com ressalva menor.**
- Tabela 1 (l. 115–117): há linhas separadas para "Juros altos elevam a carga de juros das famílias" (Sim) e para "Juros altos provocam 'o endividamento insustentável das famílias'" (p. 5; "Testado: sem efeito detectável"), e uma linha "Curva de Phillips horizontal: 'recessão e capacidade ociosa não reduzem a inflação'" (p. 5–6, 9; "Não identificado").
- Citações conferidas no ensaio:
  - "provoca o endividamento insustentável das famílias e das empresas", p. 5;
  - "a Curva de Phillips tornou-se praticamente horizontal", p. 6;
  - "Recessão e capacidade ociosa não reduzem a inflação", p. 9.
- **Ressalva**: o ensaio não fala em "carga de juros das famílias". A linha marcada "Sim" continua a citar `resende2026euacuso` em "Onde aparece", o que colide com a última frase do critério ("Nenhuma linha marca 'Sim' para uma paráfrase"). O próprio roteiro prescreveu essa linha (coluna "O que fazer", item a), e por isso não conto o item como parcial.
- **Correção de uma célula**: "Onde aparece" → "formulação deste artigo (a partir de Lara Resende, 2026, p. 5)".

**RR2-08 — Atendido.**
- l. 221 cita o ensaio (p. 9): "é inercial — tende a ficar onde está" e a convergência de longo prazo para a "diferença entre o juro básico e o crescimento real". As duas passagens estão de fato na p. 9 do PDF; a decisão da rodada 2 indicava a p. 8 para "inercial", mas o rodapé mostra que o manuscrito está certo.
- O texto conclui "ω próximo de zero no primeiro ano" e informa ω\* ≈ 0,5–0,6 (Tabela 3, l. 208–211: 0,51 e 0,61). Recalculei ω\* = x / [b(1+ī)/(1+g) − x_IPCA] e obtive 0,512 e 0,607. ✔
- Nenhuma frase atribui ω ≈ 1 ao ensaio: "Fisher pleno" aparece só no cabeçalho da tabela, sem atribuição.
- A frase de tensão foi substituída: "Alívio fiscal e ausência de pressão inflacionária exigem, juntos, que o canal de demanda da política monetária seja pouco operante, hipótese que o ensaio sustenta (…) e que este artigo não testa" (l. 221 e l. 642). A busca por "tensão" não retorna nada. ✔
- Observação opcional: pela regra do próprio ensaio, a inflação de longo prazo (≈ 5%) fica acima do IPCA corrente (4,22%), o que equivale a ω ligeiramente negativo, e o ensaio admite um "repique transitório" (p. 8–9). "Próximo de zero" é defensável.

**RR2-09 — Atendido.**
- A Eq. (`fiscal_scen`) (l. 192) tem o termo x_IPCA·Δg/(1+g).
- A Tabela 2 (l. 181) traz "Títulos indexados a preços na DPF (set./2026) 23,59% — RMD; 23,22% em agosto; 16,5% do PIB".
- A Tabela 3 (l. 208) dá −0,03 e +1,03 (gradual, x = 36,1%), na direção de R2b-2.
- `aritmetica_fiscal.txt` reproduz a tabela e traz a versão antiga (+0,22 / +1,53) para comparação.
- Recalculei a tabela: diferenças só no 2º decimal (−0,025 contra −0,03), por arredondamento dos insumos.

**RR2-10 — Atendido.**
- Painel B (l. 214–215): Δī = −5,13, com ω = 0 dando −3,97, e −4,27 pela DPMFi. Confere com o arquivo ("Conferência ω=0, DPF: … = −3.97 p.p. PIB (ensaio: cerca de 4% do PIB, p. 11)").
- O ensaio diz "de quase 13% para 7,5% … cerca de 4% do PIB ao ano" na p. 11 (conferido). O texto atribui o número ao ensaio e o liga ao Painel B com ω = 0 (l. 221).
- A legenda (l. 200) não chama nada de "primeiro ano". Os painéis estão rotulados "Painel A: primeiro ano" e "Painel B: regime permanente".
- A busca por "2,3\\%" e por "DBGG Terceiro" não retorna nada. ✔

**RR2-14 — Atendido.**
- l. 286: "reestimamos com a meta Selic … as LPs dependentes de estado (Tabela 10), a LP linear da inflação e a resposta de J (Seção 4.7); o SVAR e as demais especificações usam apenas a SGS 4189".
- Os scripts fazem isso: `build_system(policy='meta_selic')` em `estimacao_regime_juros_altos.py` (l. 136) e em `canal_familias.py` (l. 127), este para J, IPCA livres e Selic.
- H2 com a SGS 432 (l. 588): +0,27, p = 0,012, p_Holm = 0,035 e +0,071 por DP. Confere com `canal_familias.txt` (+0,2697; 0,012; [0,035]; +0,0711). ✔
- Problema novo derivado: M2 (l. 556 chama de "acumulada" uma inflação mensal).

**RR2-17 — Parcialmente atendido.**
- Painel B da `tab:nulo` (l. 471–472): p_boot de 0,928/0,937 (h = 12) e 0,107/0,104 (h = 24), com quantis de 11,6 e 16,1. Confere com §D (11,62; 16,05). ✔
- O resumo e a Conclusão não usam "significativa" para a interagida. ✔
- Teste C4: o roteiro pedia "aplicar o mesmo bootstrap **ou justificar no texto** por que não", e o critério pede "bootstrap de C4 ou uma justificativa explícita". A justificativa existe, mas **só** em `inferencia_regimes.txt` ("TESTE C4 … por que não há bootstrap"). O .tex não fala do assunto: a busca por "C4" só encontra l. 316.
- Mais grave: a calibração de tamanho que o autor fez no lugar do bootstrap é desfavorável a H2 e não foi reportada. O teste NW rejeita a IRF verdadeira em 21,1% das réplicas a 5% nominal, e o valor crítico calibrado de |t| é 3,06, contra t observado de 2,76. Ver B1.
- Por isso, parcial.

**RR2-18 — Atendido.**
- l. 483: "positiva em todos eles, com p-valores pontuais abaixo de 0,05 em quatro (11,5%, 12%, 13% e 14%)". Também: "No limiar de 14%, que define um platô de apenas 31 meses (22 na amostra de h = 24, nos episódios de 2006–2007 e 2016–2017), a diferença é de +4,53 em h = 24 (p = 0,001) e de +3,17 em h = 12 (p = 0,040)".
- Os números conferem com §G: 31 meses; +4,53 com p = 0,001; +3,17 com p = 0,040; p < 0,05 em 4 limiares para h = 24. O número 22 não está em `resultados/` e foi tomado de R1.
- A grade de γ̂¹² também confere: "+0,95 a 13% e desaparece acima disso (+0,13 a 13,5%; −0,56 a 14%)", e t > 1,96 em 9 de 11.
- l. 557: "γ̂¹² é estável em p e no Painel A, exceto quando o regime é definido pelo juro real ex ante … e desaparece para limiares acima de 13%". ✔
- Conclusão (l. 638): "desaparece com a definição do regime pelo juro real e para limiares acima de 13%". Não diz "resiste". ✔
- Trimming de 15% (RR2-20), conferido: 11,37 → 4,87, com p = 0,458.

**RR2-27 — Atendido.**
- "Taxa implícita" aparece no resumo (l. 46), na §4.7 (l. 586) e na Conclusão (l. 640). A busca por "taxa efetiva" não retorna nada.
- §3.1 (l. 236): "a documentação pública consultada não descreve como o BCB estima e separa juros e amortização no numerador". ✔
- A §4.7 discute o repasse implícito alto, e os dados não distinguem as explicações.
- "Mais robusto" vem qualificado (l. 75, 591 e 640: "documenta o repasse convencional da Selic, e não evidência sobre a tese"). O pico robusto aparece em 12–18 meses (l. 588). ✔
- A qualificação "estatisticamente robusto" fica comprometida por B1, que trato como problema novo.

**RR2-28 — Atendido.**
- (a) A legenda da Tabela 11 (l. 566) informa "Todas as linhas incluem, além dos controles do sistema, seis defasagens da própria variável dependente", e a versão antiga está em `canal_familias.txt`. As linhas conferem com o bloco "COM defasagens da própria variável" (A, S, S', E e J/E). Para J, as defasagens próprias já estão no VAR. ✔
- (b) l. 586: "os dados não sustentam a leitura de desalavancagem". A busca por "desalavanc" só encontra esse trecho e o mecanismo teórico da l. 230. A Conclusão (l. 640) diz "Não se detecta efeito sobre o endividamento". ✔
- (c) "p_Holm ≤ 0,003 em todos os horizontes (p_Holm^EWC ≤ 0,024)" (l. 586). Confere com o arquivo: máximo NW de 0,0025 e máximo EWC de 0,0239. ✔

**RR2-29 — Atendido, com ressalva menor.**
- §4.7, item 4 (l. 589): "Assimetria (exploratória)". Traz p_Holm = 0,34, b⁺ = +0,14 e b⁻ = −0,17 em h = 0, e o termo em |s| de +0,16 em h = 0 (p < 0,001). Confere com `canal_familias.txt`: 0,343; +0,144/−0,171; b = +0,157 com p = 0,000.
- §5.2 (l. 623): "surpresas negativas não têm efeito detectável sobre J, mas a simetria não é rejeitada, e surpresas negativas em torno da regra não são cortes anunciados".
- Conclusão (l. 640): "não há evidência robusta de que surpresas negativas reduzam o comprometimento de forma diferente das positivas".
- O episódio de fev.–ago./2026 não aparece. ✔
- Ressalva: ver M3. A frase "a Selic também responde de modo diferente aos dois sinais" é seletiva, e a normalização pedida não é reportada.

**RR2-36 — Atendido quanto ao critério literal, com ressalva.**
- `artigo_anonimo.pdf` (31 p.) não contém "Bonvenuto", "Ângelo", "github" nem "Mudanças em relação", nem no texto extraído, nem nos *streams* descomprimidos, nem nos metadados (Author vazio). O repositório aparece como "(omitido na versão anônima)". ✔
- `scripts/`, `resultados/` e `data/` não contêm "VERSÃO", "versão 3", "v3" nem "Número da versão". As ocorrências de "versão" são "versão em reais" e o caminho da API Olinda `/versao/v1/`, ambos inócuos. ✔
- **Ressalva** (M5): o pacote de replicação ainda identifica o autor e a história da revisão:
  - `Autor: Ângelo Augusto Bonvenuto` em 9 scripts (`comum.py`, `canal_familias.py`, `inferencia_regimes.py`, `estimacao_*.py`, `aritmetica_fiscal.py`, `coleta_series_complementares.py`, `tex_para_markdown.py`);
  - rótulos de rodada ("REV-16 e REV-29", "RR2-09 a RR2-12 do painel independente", "RR2-15; 'p < 10^-11' do texto") nos cabeçalhos dos scripts;
  - "(RR2-22)" em `resultados/inferencia_regimes.txt`, l. 110.
- Se o pacote for anexado a uma submissão duplo-cega, isso anula a anonimização. Com o aceite condicional, a gravidade é menor, mas a limpeza é obrigatória antes de qualquer circulação cega.

---

## 2. Amostragem dos `should_fix` que a carta declara "feitos"

Conferi 16 dos 17 itens declarados "feitos" (só RR2-23b não existe; a carta não declara outros). Também conferi os itens declarados "parcial" e "não feito".

| ID | Carta | Conferência | Evidência |
|---|---|---|---|
| RR2-03 | feito | **Atendido** | l. 49 e 62: "interação monetária-fiscal" / "monetary-fiscal interaction" |
| RR2-04 | feito | **Atendido** | l. 69: Barth–Ramey e Ravenna–Walsh no canal de custos; Loyo, Blanchard e Favero–Giavazzi como "literatura de interação monetária-fiscal" |
| RR2-05 | feito | **Atendido** | l. 83: `cochrane2001long`; o .bib e o PDF trazem *Econometrica* 69(1):69–116 |
| RR2-11 | feito | **Atendido** | Coluna ω = −0,5 (l. 205–215) e frase sobre o que a equação omite (l. 195, 221) |
| RR2-12 | feito | **Parcialmente atendido** | (b) NFSP: 4,6 p.p. (l. 160; arquivo: +4,55). (c) Justificativa dos 51,6% (l. 195). (a) O critério diz "A grade aparece no texto", mas o texto só remete ao arquivo ("Sensibilidades a x e a Δi estão em resultados/…"). A carta diz "feito" |
| RR2-15 | feito | **Atendido** | l. 279: F(11,246) = 8,08 e F(11,204) = 4,12. `resultados_svar_summary.txt` l. 25–26: p = 5,15e−12 e 1,72e−05, gerados por `estimacao_svar_lara_resende.py` (l. 109 e seguintes) |
| RR2-19 | feito | **Atendido** | l. 440 e 483: variante *wild* (0,092; p praticamente iguais), Selic negativa em 4% (arquivo: 0,041/0,044), descarte sem efeito (n = 958/955) |
| RR2-20 | feito | **Atendido** | l. 483: 11,4 → 4,9, p = 0,458 (arquivo: 11,367 → 4,873; 0,458) |
| RR2-21 | feito | **Atendido** | `tab:nulo` l. 464–465: 2,70/3,32 e 0,42/0,52. Confere com §A. Sem banda simultânea, o que a carta admite (era "considerar") |
| RR2-22 | feito | **Atendido** | l. 446: limites unilaterais (−0,40; +0,07) e (0,00; +0,50) / (−0,05; +0,55). l. 483: 25% e 16% sob a nula (arquivo: 0,253; 0,159) |
| RR2-23 | feito | **Atendido** (ressalva) | Tabela 10 com p EWC (l. 530–540). "Por acaso" substituído (l. 555). O N por regime está na legenda da Tabela 7 só para h = 12 e 24; os demais estão no arquivo |
| RR2-24 | feito | **Atendido** | l. 494: queda em quatro platôs, alta leve em 2006–09 e repique nos quatro completos. Confere com §F |
| RR2-30 | feito | **Atendido** | l. 588: +0,55/+0,77/+0,19 (p de 0,004 a 0,43) e trimestre agregado de +0,42 a +0,49 (p ≤ 0,009). Confere com o arquivo |
| RR2-31 | feito | **Atendido** | l. 587: MDE de S = 1,13 e de J − S = 0,76 (arquivo: 1,13; 0,76); mecanismos como hipóteses |
| RR2-33 | feito | **Atendido** | l. 236: `bcb2021notacredito`, presente na bibliografia do PDF. l. 255: "nível; nível e ln" |
| RR2-34 | feito | **Atendido** | l. 633: RNDBF restrita sem rendas de propriedade; carga bruta, não redistribuição líquida |
| RR2-16 (consider) | feito | **Atendido** | l. 316: "Testes principais … pré-especificados nesta versão … não houve pré-registro" |
| RR2-35 (consider) | feito | **Atendido** | l. 591: ≈ 0,2 por p.p. e +2,3 a +2,5 contra +2,6 (arquivo: 2,28–2,49; 7,09 → 9,69) |
| RR2-37 | parcial | Parcial (confere) | O script grava a data e o SHA-256 (l. 66–98); `safra_dados.txt` continua em texto fixo, como a carta declara |
| RR2-38 | parcial | Parcial (confere) | Páginas acrescentadas (49–80, 85–108, 605–635, 265–294). Cochrane (2026) só com o domínio do blog e o RMD sem URL, como a carta declara |
| RR2-32 | não feito | Não feito (confere) | A carta justifica, mas o critério ("comparação reportada **ou justificativa de omissão**") pede a justificativa no texto, e o .tex só diz que "os dados não distinguem essas explicações" (l. 586). Aceitável para `should_fix`, mas convém uma frase explícita |

Resultado da amostragem: 14 de 16 itens declarados "feitos" conferem integralmente, 1 confere com ressalva (RR2-23) e 1 é parcial (RR2-12).

---

## 3. Fidelidade da carta de resposta

No geral a carta é **fiel e verificável**. Os números de "Números que mudaram nesta rodada" conferem todos com `resultados/`:
- 0,093; 0,380/0,268; 0,335/0,128; 3,44;
- +6,4 contra +8,2;
- ≤ 0,003;
- +1,53 → +1,03; +0,22 → −0,03; −4,98 → −3,97; +0,20.

Os itens parciais e não feitos (RR2-32, 37, 38, 06, 13, 25 e 26) estão declarados com honestidade. Há, porém, quatro alegações falsas ou exageradas e uma omissão relevante:

1. **RR2-02** ("A interagida aparece com o p calibrado", em "resumos, §1, §6"): **falso** para esses locais. O p = 0,107 só está na §4.5 e na Tabela 8.
2. **RR2-17** ("Resumo, introdução e Conclusão usam o p calibrado"): **falso** pelo mesmo motivo. A carta também diz que a justificativa de C4 e "uma calibração do tamanho do teste HAC" estão "no arquivo de resultados", sem informar o resultado dessa calibração: tamanho efetivo de 21% e valor crítico de 3,06 > t = 2,76. **Omissão material**, porque o resultado enfraquece o cabeçalho de H2 (B1).
3. **RR2-12(a)** ("A grade x × Δi é citada no texto"): verdadeiro só como remissão a um arquivo. O critério pedia que a grade aparecesse no texto. "Feito" é **exagerado**.
4. **RR2-29** ("A resposta da Selic difere por sinal (+2,5 contra +1,6 p.p. em 12 meses)"): o número confere para o **nível** em t + 12, mas a média da Selic de t a t + 12 é praticamente igual (+2,21 e +2,23), e a normalização que o roteiro pedia (J por Selic: +0,41 e −0,01) está no arquivo e não no texto. **Seletivo**.
5. **RR2-36** ("Os rótulos de versão … saíram de scripts e resultados"): verdadeiro para os rótulos listados. A carta não menciona que o nome do autor continua em 9 scripts, nem os rótulos REV-/RR2- de rodada ainda presentes.

---

## 4. Problemas novos introduzidos ou revelados pela revisão

Severidade: **bloqueante** = deve ser corrigido antes do aceite definitivo (aqui, só texto); **menor** = pode ser corrigido na versão final ou nas provas.

### B1 — Bloqueante: o teste C4 (H2) não passa pela régua que o artigo aplica a γ̂

- **Localização**: resumo (l. 46); Introdução (l. 75: "O resultado estatisticamente mais robusto…"); §3.4 (l. 316, C4); §4.7, item 3 e último parágrafo (l. 588, 591: "O resultado é estatisticamente robusto"); Conclusão (l. 640).
- **Evidência** (`resultados/inferencia_regimes.txt`, bloco "TESTE C4"), sob o mesmo DGP linear usado para γ̂:
  - o teste NW de J em h = 12 rejeita a IRF verdadeira em **21,1%** (iid) e **20,1%** (*wild*) das réplicas a 5% nominal;
  - o valor crítico calibrado de |t| é **3,06 / 3,04**, e o t observado é **2,76** (0,4312 / 0,1562);
  - P(|t_réplica| ≥ |t_obs|) = **0,085 / 0,076**.

  É exatamente a régua com que o artigo declara γ̂¹² "não significativa a 5% sob bootstrap" (|t| = 2,96 contra o quantil de 3,44; p = 0,093). O autor rotula a razão de "só descritiva", mas a conta é a mesma.
- **Consequência**: pela régua do próprio artigo, o teste principal C4 em h = 12 é marginal (p ≈ 0,08), da mesma ordem de γ̂ (0,093) e da interagida (0,107). "Estatisticamente mais robusto" deixa de valer sem qualificação em h = 12. A robustez entre especificações (EWC 0,015; NW h+3; amostra até 2023:12; SGS 432; fases trimestrais agregadas) continua de pé, mas o tamanho do EWC sob esse DGP não foi calibrado.
- **Correção** (texto; números já disponíveis):
  - reportar na §4.7 a calibração (tamanho de 21% e valor crítico de 3,06) e a justificativa de não usar o bootstrap sob a nula para C4;
  - trocar "estatisticamente mais robusto" por uma formulação como "o mais robusto entre especificações; com valor crítico calibrado, marginal em 12 meses (p ≈ 0,08)";
  - no resumo, falar em "12 a 18 meses" em vez de fixar 12;
  - opcionalmente, calibrar também o tamanho do teste EWC no mesmo laço e o valor crítico em h = 9 e 18, onde t ≈ 3,3.
- Se o autor contestar, consultar R1.

### Menores

| # | Localização | Evidência | Correção |
|---|---|---|---|
| M1 | §4.5, "Primeiro estágio e normalização" (l. 492) | O texto diz "a diferença entre as razões tem intervalo de [−0,30; +0,07] em 12 meses e [−1,08; +1,68] em 24 meses". `inferencia_regimes.txt` §E traz **[−0,375; +0,069]** e **[−1,749; +1,056]**. Número velho, divergente da saída. A conclusão ("se sobrepõem") não muda | Atualizar para os valores do arquivo |
| M2 | §4.6, item 2 (l. 556) | "Na LP linear com o choque da meta Selic, a **inflação acumulada** cai 0,14 p.p. em 24 meses". O script usa `lp(y) = ols_hac(y.shift(-h), …)` sobre `ipca_livres` (`canal_familias.py`, l. 49 e 133), ou seja, a inflação **mensal** em t + 24, no mesmo conceito da Tabela 6 (−0,289 % a.m.), e não a acumulada da Eq. (`lp_state`). O parágrafo a justapõe a β̂_mod^24 (acumulada) | "a inflação mensal em h = 24 cai 0,14 p.p. (contra −0,29 com o choque-base; p = 0,012; p_Holm = 0,071)" |
| M3 | §4.7, item 4 (l. 589) | (i) "A Selic também responde de modo diferente aos dois sinais (+2,5 / +1,6)" usa o nível em t + 12; a média de t a t + 12 é +2,21 / +2,23, e J normalizado pela Selic média é +0,41 / −0,01 (arquivo, bloco c). A normalização pedida em RR2-29 não elimina a assimetria e não é reportada. (ii) O termo em \|s\| é dito "não significativo depois", mas tem p entre 0,057 e 0,095 em h = 9–24 e magnitude igual à do termo linear | Reportar a razão normalizada e descrever \|s\| como "marginal (p < 0,10) de 9 a 24 meses". A conclusão "assimetria não robusta" fica |
| M4 | Tabela 1, l. 115 | "Juros altos elevam a carga de juros das famílias" atribuído a `resende2026euacuso` e marcado "Sim". O ensaio não contém essa formulação (só "endividamento insustentável", p. 5) | "Onde aparece" → "formulação deste artigo (a partir de p. 5)" |
| M5 | `scripts/` (9 arquivos); `resultados/inferencia_regimes.txt` l. 110; cabeçalhos de `comum.py`, `aritmetica_fiscal.py`, `inferencia_regimes.py`, `estimacao_regime_juros_altos.py` e `estimacao_svar_lara_resende.py` (l. 109) | "Autor: Ângelo Augusto Bonvenuto"; "REV-16 e REV-29", "RR2-09 a RR2-12 do painel independente", "(RR2-22)". Também `scripts/__pycache__/` incluído no pacote | Retirar o nome e os rótulos de rodada do pacote (ou não anexá-lo até a publicação). Bloqueante se o pacote for a referees em regime duplo-cego |
| M6 | §2.2 (l. 195) | A grade x × Δi (RR2-12a) é só remetida a `resultados/` | Incluir como nota ou painel (quatro linhas no arquivo) |
| M7 | Resumo (l. 46, 59) e Conclusão (l. 640) | A magnitude de H2 continua fixada "em 12 meses", embora a §4.7 diga que o pico robusto está em 12–18 meses (resíduo de CN-10 / RR2-30) | Resolver junto com B1 |
| M8 | Eq. (1) e l. 135 (PDF, p. 5) | `s_{firm}` é composto como produto itálico ("s f irm") | `s_{\text{firm}}` |
| M9 | `referencias.bib` | Cochrane (2026) sem os URLs dos dois posts e RMD sem URL (RR2-38 parcial, declarado). Grafia "Lara-Resende" em Arida et al. e "Lara Resende" no resto | Completar e uniformizar, se o periódico exigir |
| M10 | RR2-32 / l. 586 | Sem frase que justifique, no texto, a omissão da comparação com as taxas médias do SGS e o ICC | Uma frase nas Limitações |

**O que conferi e não tem problema**:
- citações e páginas do ensaio: p. 4 (5,7%), p. 5, 6, 7 (hipótese H₁, "dissociada da política fiscal…"), 8, 9 e 11;
- insumos fiscais (DBGG +5,56 p.p.; NFSP 4,55; 16,5% do PIB);
- Tabelas 6, 7 e 10 contra os arquivos;
- números do SVAR;
- episódios;
- sinais do Wald na Tabela 10 ("dois rejeitam … com sinais opostos");
- referências cruzadas de seção e tabela, todas resolvidas;
- ausência de "??" ou de citações não resolvidas nos dois PDFs.

O texto dos PDFs corresponde ao .tex conferido.

---

## 5. Decisão editorial

### Decisão: **Accept com correções menores (aceite condicional)**

**Justificativa.**
- Dos 13 `must_fix`, **10 estão atendidos** e **3 parcialmente atendidos**, e nenhum está não atendido. Os três parciais (RR2-01, 02, 17) se resolvem com uma oração ou um número em cada lugar, e os números já estão no manuscrito ou em `resultados/`.
- A revisão foi substancial e correta nos pontos que motivaram a 2ª rodada:
  - a interagida foi calibrada (p = 0,107) e o artigo deixou de chamá-la de significativa;
  - a grade é descrita por inteiro;
  - a aritmética fiscal incorporou os indexados e corrigiu o limite superior (−3,97, atribuído ao ensaio com página);
  - a leitura do ensaio (ω ≈ 0, Curva de Phillips horizontal) confere com o texto do ensaio, página por página;
  - H2 passou a falar em "taxa implícita", sem "desalavancagem";
  - a anonimização do PDF foi executada.
- Nenhum problema novo inverte a conclusão central ("H₁ inconclusiva; H₂ documenta o repasse da Selic à taxa implícita").
- O problema bloqueante **B1** é sério do ponto de vista da coerência inferencial, que foi o tema de consenso da rodada anterior: a mesma régua para todas as estatísticas. Ele exige, porém, só reescrita e o relato de números que o próprio autor já calculou. Não justifica uma nova rodada com referees.
- R1 e R2 declararam que os itens do seu domínio podiam ser conferidos pelo editor.

**Condições para o aceite definitivo** (conferência pelo editor, sem nova rodada):
1. RR2-01: acrescentar à contribuição 1 a falta de poder e "nem a tese nem a sua negação".
2. RR2-02 e RR2-17: p calibrado da interagida (0,107) no resumo, na Introdução e na Conclusão (resumo ≤ 250 palavras); justificativa de C4 no texto.
3. **B1**: reportar a calibração de tamanho de C4 (21%; valor crítico de 3,06 contra t = 2,76; p ≈ 0,08) e requalificar "estatisticamente mais robusto" no resumo, na Introdução, na §4.7 e na Conclusão. Se o autor contestar, consultar R1.
4. M1 e M2: corrigir os números e rótulos divergentes de `resultados/`.
5. M5: não enviar o pacote de replicação com nome e rótulos de rodada a nenhuma leitura cega. Limpar antes da publicação.

Os demais itens (M3, M4 e M6–M10) podem ser feitos na versão final.

### Condição de R3 (RR2-29): **cumprida**

R3 passaria a Major "se a assimetria de H2 for mantida na §5.2 e na Conclusão como afirmação sobre cortes de juros". Conferido:
- a §5.2 (l. 623) afirma o oposto ("a simetria não é rejeitada, e surpresas negativas em torno da regra não são cortes anunciados");
- a Conclusão (l. 640) diz que "não há evidência robusta de que surpresas negativas reduzam o comprometimento de forma diferente das positivas";
- a §4.7 rebaixa a assimetria a "exploratória", com p_Holm = 0,34, h = 0 e o termo em |s|;
- o episódio de 2026 foi retirado.

A ressalva M3 (normalização e descrição de |s|) é de precisão e não reabre a condição.
