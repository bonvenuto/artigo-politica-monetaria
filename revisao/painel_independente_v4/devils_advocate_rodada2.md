# Devil's Advocate: 2ª rodada (re-revisão)

**Manuscrito:** "O Patamar dos Juros Altera a Transmissão da Política Monetária? Evidência de Projeções Locais Dependentes de Estado e do Comprometimento de Renda das Famílias no Brasil (2005–2026)" (versão revisada, 9 nov. 2026)
**Assento:** Devil's Advocate. O DA não vota.
**Insumos lidos:** `manuscrito/` (fonte .tex, PDF, `resultados/*.txt`, `scripts/`, Figura 6 e o ensaio de Lara Resende, 2026), `rodada1/decisao_editorial.md` e `rodada1/devils_advocate.md`. Não li nada fora do pacote e não houve carta de resposta do autor.
**Reanálise própria:** `replica/scripts/da2_boot.py`, executado sobre uma cópia do pacote. Usa o mesmo DGP do bootstrap recursivo sob a nula de linearidade de `inferencia_regimes.py` (seção D), com B = 399 e semente 777. Os números que saem dessa reanálise vêm marcados **[reanálise DA]**. Os demais vêm do .tex, dos arquivos `resultados/*.txt` ou de aritmética sobre eles, indicada no texto.

`calibration_status: NOT_CALIBRATED` · `criteria_binding_unavailable`

---

## 1. Resumo

A revisão é ampla e, em geral, honesta. O artigo deixou de se vender como teste confirmatório da tese de Lara Resende:
- H1 é declarada inconclusiva;
- γ̂ é tratado como associação compatível com Fisher e com a regra de reação;
- o bloco teórico virou "arcabouço motivador";
- o canal da dívida pública é declarado não testado;
- a aritmética fiscal passou a ser feita em termos reais.

Quase todos os meus achados da rodada 1 foram resolvidos ou absorvidos como limitação declarada. Não registro nenhum achado CRÍTICO: nenhum dos problemas abaixo derruba a conclusão central, que é "não se detecta dependência de estado, e o teste tem pouco poder".

Os ataques desta rodada se concentram em três pontos novos.

1. **"Nulo informativo" é um rótulo errado.** A introdução promete tornar o nulo informativo, e a própria §4.5 conclui que ele é inconclusivo. A informação que o artigo de fato tem fica de fora: o padrão de sinal da diferença em h = 24 (positiva em 26 de 28 especificações reportadas), os limites unilaterais dos intervalos e o ponto mais alto da grade de limiares.
2. **Os padrões de inferência são assimétricos.** O bootstrap sob a nula é aplicado a γ̂ e ao Wald-base, mas não à especificação interagida (p = 0,001) nem a H2. Refiz esse bootstrap (**[reanálise DA]**) e o Wald interagido em h = 24 dá p = 0,085, praticamente o mesmo nível de γ̂¹² (p = 0,073). Os dois resultados nominalmente "favoráveis" ficam, portanto, no mesmo patamar: marginais a 10% e não significativos a 5%. O resumo trata γ̂ como "não significativa sob bootstrap" e o resultado interagido como "frágil à especificação". Tratados do mesmo modo, os dois mereciam a mesma frase.
3. **A aritmética fiscal atribui a Lara Resende um ω ≈ 1 que o ensaio não sustenta.** A grade de ω omite o caso convencional (ω < 0). A "tensão" com a tese, afirmada na Conclusão, é um falso dilema.

H2, o "resultado mais robusto", é quase mecânico, pequeno e frágil na amostra trimestral. Além disso, foi redefinido de forma mais fraca do que a alegação do ensaio ("endividamento insustentável"). Para essa alegação, os dados do próprio artigo apontam na direção contrária.

---

## 2. Status dos achados da rodada 1

| ID r1 | Achado (resumo) | REV | Status | Evidência na versão revisada |
|---|---|---|---|---|
| M1 | Alívio fiscal nominal × Fisher do próprio modelo | REV-21 | **Resolvido quanto à aritmética; gerou problema novo** (DA2-4) | §2.2, Eq. (fiscal_scen), Tab. 4 com ω ∈ {0; 0,5; 1}. A linha "regime permanente" com ω = 1 dá +0,25, ≈ neutro, como eu havia previsto. O texto passou a atribuir ω ≈ 1 à tese |
| M2 | H1 não é a previsão do ensaio de 2026 | REV-27 | **Resolvido** | §1.2: "H1 não é uma previsão explícita"; Tabela de componentes. Resta a redefinição de H2 (DA2-3) |
| M3 | γ̂ apresentado como compatível com LR; contagem de votos | REV-28 | **Resolvido** | Resumo, §4.6 item 3 e Limitação 3: Fisher/regra de reação, espec. 5 destacada, bootstrap sob a nula p = 0,073 |
| M4 | β_mod^24 superafirmado; Holm aplicado de forma desigual | REV-12 | **Resolvido** | "apoio sugestivo, mas não robusto"; Holm em todos os coeficientes de cabeçalho; Painel B de p |
| M5 | Selic média mensal não é surpresa | REV-15 | **Resolvido como divulgação; o problema substantivo continua** | SGS 432 reportada (espec. 9). Correlação com o choque-base de 0,31; C2 falha (p = 0,057); "não antecipado" saiu do resumo |
| M6 | Primeiro estágio por regime omitido | REV-14 | **Resolvido** | §4.5 "Primeiro estágio e normalização"; razões com IC bootstrap sem direção |
| M7 | Ciclos 2011–13 × 2016–18 como base; cinco platôs não descritos | REV-26, 38 | **Resolvido em grande parte** | §5.2 "apenas como ilustração"; Tab. de episódios. Resta uma descrição seletiva da tabela (DA2-6) |
| M8 | O modelo impõe o resultado do platô | REV-04 | **Resolvido** | §2: "é preciso *supor* que θ e ρ′ crescem" |
| M9 | Estado do modelo ≠ estado empírico | REV-03 | **Resolvido (por concessão)** | §2.1: "O canal da dívida pós-fixada, portanto, **não é testado**" |
| m1 | "Modelo fechado" | REV-04 | Resolvido | Termo ausente do .tex |
| m2 | Canal de custos atribuído ao ensaio | REV-27 | Resolvido | Tab. de componentes: Barth–Ramey; Ravenna–Walsh |
| m3 | 5,7% × 5,3% | REV-08 | Resolvido | §2.2 explica o diferencial antes da divisão por 1+g |
| m4 | r*, π*, i* sem fonte | REV-04 | Resolvido (removido) | — |
| m5 | "alivie expressivamente" | REV-05 | Resolvido | Ausente |
| m6 | "não se transmite" | REV-34 | Resolvido | "ausência de evidência ... e não evidência de ausência" (§4.7) |
| m7 | Rolagem de 4–4,5% | REV-23 | Resolvido | "limite superior" com prazo médio e vencimentos |
| m8 | "quatro" × cinco episódios | REV-20 | Resolvido | Tab. de episódios com cinco |

Minha observação da rodada 1 de que "a evidência se inclina para a transmissão convencional" foi corretamente rejeitada pelo editor (D1). Não a reapresento. O DA2-1 trata do que o artigo deixa de dizer sobre o mesmo ponto.

---

## 3. Novos achados

### DA2-1 (MAIOR): "Tornamos o resultado nulo informativo" é falso pelo próprio critério do artigo, e a informação que existe não é reportada

**Alegação atacada.** Introdução, 1ª contribuição: "testamos a dependência de estado [...] e tornamos o resultado nulo informativo". A seção do artigo sobre o nulo (§4.5) se chama "O nulo de H1 é informativo?".

**Contra-argumento mais forte.** Um nulo é informativo quando o intervalo exclui as magnitudes que a hipótese alternativa prevê. Aqui o MDE em 24 meses (0,42 p.p. por DP) é **maior** que o próprio efeito do regime moderado (−0,34 por DP). O artigo admite que "o desenho não detectaria [...] nem a diferença entre uma política eficaz no regime moderado e uma política sem efeito algum no platô". Esse nulo não é informativo, e o artigo documenta isso. O que foi feito é **diagnosticar** a falta de informação. Isso tem valor, mas é outra contribuição, e o rótulo da introdução vende mais do que existe. Esse nulo também não discrimina entre a leitura convencional e a de Lara Resende, e por isso não serve de evidência para nenhum dos lados do debate de política.

Há ainda um ponto inverso. A informação que os dados contêm não aparece no texto:

1. **Limites unilaterais.** Por DP, o IC 95% NW da diferença vai de [−0,04; +0,54] em h = 24 e de [−0,44; +0,11] em h = 12 (Tab. `tab:nulo` × 0,156).
   - Em 24 meses os dados excluem um platô *mais* eficaz que o regime moderado, mas não excluem perda total de eficácia.
   - Em 12 meses vale o oposto.
   - O artigo não diz isso. Também não diz que as duas conclusões apontam em sentidos opostos conforme o horizonte, o que é por si só um sinal de instabilidade.
2. **Padrão de sinal.** A diferença β̂_alto − β̂_mod em h = 24 é positiva:
   - na base (+1,60);
   - nas 10 especificações alternativas do Painel A da Tab. `tab:robustez`, entre +1,11 (espec. 9) e +2,51 (espec. 7), por subtração das colunas;
   - na especificação interagida (+4,15);
   - nos 11 limiares da grade (+0,16 a +4,53; `inferencia_regimes.txt` §G);
   - com p = 4 e p = 9.
   
   Só é negativa com p = 2 (−0,14) e p = 12 (−2,04). São 26 de 28. Em h = 12 o padrão é o inverso: negativa em 10 das 11 especificações do Painel A. As especificações são fortemente correlacionadas, porque usam os mesmos dados, e por isso a contagem não é evidência independente (ver DA2-2). Mesmo assim, a estimativa pontual em 24 meses corresponde a perder 50% a 110% do efeito moderado, magnitude da ordem que H1 prevê. Um leitor do resumo ("não encontramos diferença [...] em nenhum horizonte") não fica sabendo disso.

**Evidência.** .tex l. 73 versus l. 432 ("esse nulo é pouco informativo") e l. 439 ("O nulo de H1 é *inconclusivo*"); `inferencia_regimes.txt` §A, §B, §C e §G; Tab. `tab:robustez`.

**O que o autor teria de fazer.**
- Trocar a 1ª contribuição por "quantificamos o poder do teste e mostramos que o nulo não é informativo".
- Reportar os limites unilaterais por horizonte.
- Apresentar uma curva de especificações (*specification curve*) da diferença em h = 12 e h = 24, com todas as escolhas já exploradas (p, limiar, medida de juros e de inflação, controles), e dizer no texto que a direção da estimativa pontual se inverte entre 12 e 24 meses.

### DA2-2 (MAIOR): Padrões de inferência assimétricos e descrição seletiva da grade

**Alegação atacada.** O resumo e a §4.5 usam o bootstrap recursivo sob a nula para rebaixar γ̂ ("não significativa sob bootstrap") e o Wald-base. A especificação totalmente interagida (Wald p = 0,001 em h = 24) é descartada com um argumento de parcimônia ("98 regressores [...] pouco parcimoniosa"), sem passar pelo mesmo procedimento. H2, o teste C4, também nunca passa pelo bootstrap sob a nula. Ao descrever a grade de limiares, o texto omite o ponto mais favorável a H1.

**Contra-argumento mais forte.** Se o argumento para rebaixar γ̂ é que "regressores de estado persistentes produzem estatísticas t grandes com frequência" (quantil de 95% de |t| = 3,40), a coerência exige o mesmo teste para *toda* estatística dependente de estado. Isso vale em particular para a única que contradiz a frase de abertura do resumo. Com o Wald interagido χ²(1) ≈ 10,8 contra o quantil de 6,59 do Wald-base sob a nula, não se podia saber a resposta sem calcular. Na prática, o autor escolheu qual teste submeter ao procedimento mais exigente.

A descrição da grade (§4.5) diz que a diferença em h = 24 "é positiva entre 9,5% e 13%" e que, em h = 12, "é negativa e significativa para limiares de 9% a 10%". Pelos números de §G:
- a diferença em h = 24 é positiva em **todos** os limiares de 9% a 14%;
- no limiar de 14%, o mais próximo de "juros persistentemente altos" (31 meses), a diferença é **+4,53 com p = 0,001** em h = 24 e **+3,17 com p = 0,040** em h = 12, ambas no sentido de H1.

O texto cita os pontos significativos contrários a H1 (9%–10% em h = 12) e omite os favoráveis (14%). Os dados estão na Figura 6, mas o texto é o que o leitor lê. A mesma figura mostra ainda que γ̂¹² vai a zero ou fica negativo nos limiares de 13,5% e 14%. Isso pesa contra a leitura "platô → inflação mais alta" exatamente onde os juros são mais altos, e também não é comentado.

**Evidência.**
- `inferencia_regimes.txt` §D, §G; .tex l. 468, 472; Figura 6.
- **[reanálise DA]** bootstrap recursivo sob a nula, mesmo DGP do autor, B = 399: 
  - Wald da LP totalmente interagida em h = 24: observado 10,35, **p bootstrap = 0,085**, quantil de 95% sob a nula = 13,65. Em h = 18: p = 0,521.
  - Diferença em h = 24 positiva nos 11 limiares da grade: ocorre em **10,5%** das réplicas sob a nula (cerca de 21% para "mesmo sinal, qualquer que seja"). A média da diferença na grade (+1,93) tem p unilateral de 0,068 e bilateral de 0,168.
  - Leitura: o resultado interagido **não** sobrevive a 5%, o que apoia o "inconclusivo" do autor. Mas fica no mesmo patamar marginal de γ̂¹², e a consistência de sinal na grade é pouco informativa, porque sob a nula ocorre em uma de cada cinco amostras. A conclusão do autor se mantém. O que não se mantém é o tratamento retórico diferente dado a dois resultados com o mesmo p-valor de bootstrap.

**O que o autor teria de fazer.**
- Aplicar o bootstrap sob a nula à especificação interagida e a H2, ou declarar por que não.
- Descrever a grade inteira, inclusive os pontos de 13,5% e 14% e o número de episódios por trás deles. Em h = 24 com limiar de 14%, a amostra termina em 2024:08, então restam praticamente os episódios de 2006 e de 2015–16.

### DA2-3 (MAIOR): H2, o "resultado mais robusto", é quase mecânico, pequeno, frágil na amostra trimestral e testa uma versão mais fraca da alegação do ensaio

**Alegação atacada.** No resumo e na introdução, "o resultado mais robusto é o canal das famílias". Na Tabela de componentes, "Juros altos elevam a carga de juros das famílias — H2 — Sim".

**Contra-argumento mais forte.**

1. **É mecânico.** As séries 29033/29037 são estimativas do BCB (numerador = serviço *estimado*; §3.1). A razão J/E, que o artigo chama de "taxa implícita", é essencialmente a taxa média estimada do estoque de crédito das famílias. Dizer que ela sobe com a Selic é afirmar o repasse da taxa básica às taxas de empréstimo, o elo inicial do canal convencional. O artigo mesmo admite que o sinal é "quase mecânico" (§1.2), mas mesmo assim chama esse resultado de "mais robusto". Robustez de algo que vale por construção não informa sobre o debate.
2. **Aponta contra a alegação de Lara Resende, não a favor.** O ensaio afirma que os juros "provoca[m] o endividamento insustentável das famílias e das empresas" (ensaio, p. 2). O artigo trocou "endividamento insustentável" por "carga de juros" e marcou "Sim". Para o endividamento, que é a alegação de fato, a Tabela `tab:servico` mostra **queda** (E: −1,0 p.p. da renda em 12 meses; desalavancagem). Também não se detecta efeito no serviço total. O que H2 documenta é o canal convencional funcionando: juro mais alto, taxa efetiva mais alta, desalavancagem. O texto não diz que isso contradiz o componente "endividamento insustentável".
3. **É frágil onde a estrutura dos dados mais importa.** Na amostra trimestral não sobreposta, a única imune por construção à MA(2) da renda, o efeito em h = 3, 6, 9 e 12 cai à metade ou menos e não é significativo (+0,19, p = 0,43 em h = 12). Só h = 18 é significativo. O "0,07 p.p. por DP em 12 meses" do resumo não sobrevive a esse corte. O ajuste NW h + 3 corrige o erro-padrão, não a estimativa pontual.
4. **É pequeno.** São 0,07 p.p. de uma razão de cerca de 10,9% (≈ 0,6% do nível). A correlação em nível entre J e a Selic em 2005–2026 é 0,09 (`canal_familias.txt`, descritivos). A trajetória de J/E (29,2% em 2005, 16,4% em 2021) é dominada pela composição do crédito, não pela Selic.

**Evidência.** `canal_familias.txt` (seção de robustez, coluna "trimestral"; descritivos); Tab. `tab:servico`; ensaio, p. 2.

**O que o autor teria de fazer.**
- Desdobrar a Tabela de componentes em "carga de juros" (Sim, quase mecânico) e "endividamento" (testado: queda, sem significância após Holm).
- Tirar "mais robusto" do resumo ou condicioná-lo à amostra trimestral.
- Dizer explicitamente que H2 é evidência do canal convencional de repasse, e não da tese.

### DA2-4 (MAIOR): A aritmética fiscal atribui ω ≈ 1 a Lara Resende sem base no ensaio, omite ω < 0 e cria um falso dilema

**Alegação atacada.** §2.2: "a tese de que a dívida curta permite reduzir juros sem repique inflacionário, porque a inflação 'inicia imediatamente sua convergência para um nível mais baixo', corresponde a ω próximo de 1, cenário em que a razão piora no primeiro ano". Conclusão: "[o alívio depende de] o quanto a inflação *não* acompanha a queda dos juros, o que está em tensão com a tese de que a dívida curta permitiria reduzir juros e inflação ao mesmo tempo". Introdução, 3ª contribuição.

**Contra-argumento mais forte.**

1. **Leitura errada do ensaio.** No ensaio, o "nível mais baixo" é o de longo prazo, "dado pela taxa de juros". O próprio ensaio o define: "no longo prazo a inflação converge para a diferença entre a taxa básica de juros e a taxa de crescimento real da economia" (p. 9), com crescimento real potencial de 2,5% (p. 10). Com a Selic em 7,5%, esse nível é **5,0%**, *acima* do IPCA corrente de 4,22% (Tab. de insumos). Com o piso final de 5,5%, é 3,0%. Pela regra do próprio ensaio, a passagem de 13,94% para 7,5% implica Δπ entre +0,8 e −1,2 p.p., isto é, ω entre −0,12 e +0,14, e não ω ≈ 1. O ensaio também concede que, "no curto prazo, a relação [...] pode ser inversa" (p. 9), o que é ω ≤ 0. A tese do ensaio é que o juro *real* (≈ 9,7%) está muito acima de r = g, e que o corte reduz o juro real. É exatamente o cenário ω ≈ 0, em que a Tab. 4 do próprio artigo dá o **maior** alívio.
2. **O ponto de equilíbrio está longe de 1.** Pela Eq. (fiscal_scen), o alívio no 1º ano é nulo quando ω* = x(1+g)/[b(1+ī)]. Isso dá **0,41** para x = 36,1% do PIB e **0,49** para x = 42,8% (aritmética DA com os insumos do artigo). Qualquer leitura plausível do ensaio fica na região de alívio. O "dilema" só existe se se atribui à tese um repasse de mais de 40% do corte à inflação em 12 meses, o que nem a tese nem a visão convencional sustentam.
3. **A grade omite justamente o caso convencional.** ω ∈ {0; 0,5; 1} cobre apenas o repasse "neo-fisheriano". A previsão convencional, e o sinal do próprio C2 do artigo (aperto reduz a inflação, então corte a eleva), é ω < 0. Nesse caso o alívio contábil da razão é *maior*, por inflação. O custo é outro: desancoragem e prêmio de risco, que a equação não modela. A grade cobre um lado do debate e deixa o outro de fora.
4. **A parcela indexada a preços tem tratamento de prefixada.** Na Eq. (fiscal_scen), todo o estoque fora de x mantém o custo nominal ī. Com ω = 1, porém, o custo nominal dos títulos indexados ao IPCA também cai com π. Com uma participação ilustrativa de 25% da DPF (≈ 17,5% do PIB; esse número não está no pacote), o termo omitido vale cerca de −0,53 p.p. no corte gradual. Isso reduz o "+1,53" de ω = 1 para cerca de +1,0 **[aritmética DA, participação suposta]**.
5. **O modelo não é o dela, e o canal dela fica de fora.** A lei de movimento da dívida é uma identidade, e nessa parte a crítica é legítima: Lara Resende precisa aceitá-la. Mas o ganho que o ensaio postula vem do prêmio de solvência (θ, ρ′; "dissipa a desconfiança", p. 11). Esse prêmio entra no ī da rolagem e foi fixado. A própria linha de "regime permanente" do artigo dá **+0,25 p.p. com ω = 1**, essencialmente neutro. A "piora" de ω = 1 é um efeito transitório do denominador no primeiro ano, não uma refutação de longo prazo.

**Evidência.** .tex l. 186–214, 631; `aritmetica_fiscal.txt`; ensaio, p. 7–11.

**O que o autor teria de fazer.**
- Remover a equivalência "tese = ω ≈ 1" ou fundamentá-la com uma citação que diga isso.
- Mapear a regra de longo prazo do ensaio (π → i − g_real) para ω.
- Estender a grade para ω < 0.
- Separar prefixados de indexados.
- Reescrever a frase de "tensão" da Conclusão. A versão defensável é: "o alívio exige queda do juro real, e a tese o prevê; o que está em disputa é se essa queda desancora as expectativas, e este artigo não estima isso".

### DA2-5 (MENOR): Jardim de caminhos bifurcados na especificação-base

**Alegação atacada.** A especificação-base (p = 6, limiar na mediana, MM12 nominal, NW h + 1, IPCA livres, Selic média) e os quatro "testes confirmatórios".

**Contra-argumento mais forte.** Todos os critérios de informação escolhem p = 2 (`resultados_svar_summary.txt`). p = 6 é a única escolha em que C2 é significativo a 5% pelos dois critérios (Painel B). Os testes confirmatórios foram declarados "depois de uma análise exploratória dos mesmos dados" (§3.4). O MDE é comparado com o efeito moderado justamente na especificação que maximiza esse efeito. Com p = 2, o efeito é −0,20 por DP e o MDE fica em cerca do dobro, o que reforça o DA2-1. O autor divulga tudo isso, o que é um mérito. Mas "confirmatório" é um rótulo impróprio para testes escolhidos depois de olhar os dados.

**O que o autor teria de fazer.** Trocar "confirmatórios" por "principais (pré-especificados nesta versão, sem pré-registro)" e incluir a curva de especificações do DA2-1.

### DA2-6 (MENOR): A Tabela de episódios mostra "repique" após o fim de todos os platôs completos, e o texto não comenta

**Alegação atacada.** §4.5, "Episódios": "Dois deles (2015–2017 e 2022–2024) terminaram com forte queda da inflação". Tabela de componentes: "Dívida curta (LFT) evita repique inflacionário após corte: Não [testado]".

**Contra-argumento mais forte.**
- A inflação caiu durante **quatro** dos cinco platôs, não dois: 7,82→5,61 também é queda.
- Nos quatro episódios completos, a inflação de itens livres 12 meses após o fim do platô foi **maior** que no fim: 4,12→5,94; 5,61→8,11; 1,48→2,76; 4,06→5,20 (Tab. `tab:episodios`). Em todos houve LFT em participação alta.

É descritivo e confundido, mas é o dado mais próximo da previsão específica do ensaio ("sem repique"), e ele aparece na direção contrária. O artigo marca o componente como "não testado" e não usa o próprio quadro. Isso não é viés de confirmação a favor da tese. Mostra uma tendência a não extrair consequências de nenhum lado, coerente com o "inconclusivo" mas pouco útil ao leitor.

**O que o autor teria de fazer.** Descrever a tabela inteira e comentar o padrão pós-platô, com a ressalva de endogeneidade (o corte segue a queda da inflação).

### DA2-7 (MENOR): Assimetria de H2 sustentada por testes a 10%, com anomalia em h = 0 e anedota confundida

**Alegação atacada.** §4.7, item 4; §5.2 ("surpresas negativas não reduziram J^fam"); Conclusão.

**Contra-argumento mais forte.**
- A simetria só é rejeitada a 10% (p entre 0,057 e 0,095).
- Em h = 0, na especificação assimétrica, as duas partes do choque **elevam** J de forma significativa: b⁺ = +0,144 (p = 0,003) e b⁻ = −0,171 (p = 0,001), que aplicado a um choque negativo também eleva J. A simetria é rejeitada com p < 0,001 justamente no horizonte em que, segundo o próprio texto, nada deveria acontecer (média móvel da renda). Isso indica que surpresas negativas ocorrem quando J já está subindo, o que contamina a leitura de b⁻ ≈ 0 nos horizontes seguintes.
- A anedota de fevereiro a agosto de 2026 (Selic de 14,90% para 13,94%, J sobe) é confundida pelo efeito defasado das altas de 2024–25. Pela IRF do próprio artigo, esse efeito atinge o pico em 12–18 meses.

**O que o autor teria de fazer.** Rebaixar a assimetria a "sugestiva a 10%", reportar a anomalia de h = 0 e retirar a anedota, ou controlar pelas defasagens da Selic.

### DA2-8 (MENOR): Contradição interna sobre a natureza do nulo

O resumo diz "Não encontramos diferença estatisticamente significativa [...] em nenhum horizonte" e, duas frases depois, que a especificação interagida "produz diferença significativa [...] em 24 meses". A Conclusão repete o padrão. A frase de abertura vale só para a especificação-base. A grade (4 limiares significativos em h = 24 e 4 em h = 12) e o Painel A (2 de 22) também a contradizem se lida de forma incondicional. Sugestão: "Na especificação-base, não encontramos [...]; o sup-Wald sob a nula não rejeita em nenhum horizonte".

---

## 4. O contra-argumento mais forte ao artigo inteiro

O artigo virou um relatório cuidadoso de que **os dados mensais brasileiros não conseguem responder à pergunta do título**. As três contribuições declaradas não se sustentam como formuladas.

1. **O nulo não é informativo.** O MDE é maior que o efeito, e o próprio texto o diz. O pouco que os dados sugerem não é relatado: perda de eficácia em 24 meses da ordem prevista por H1, ganho em 12 meses, e o limiar mais alto favorecendo H1 enquanto γ̂ se anula. Com cinco episódios e um choque que muda substancialmente com a medida da taxa (correlação de 0,31 com a meta Selic), nenhuma especificação mensal resolve isso. O autor admite exatamente isso na Limitação 2.
2. **H2 é robusto porque é quase uma identidade contábil do repasse de juros.** Na parte que poderia discriminar (endividamento e serviço total), aponta para o canal convencional ou não detecta nada.
3. **A aritmética fiscal acerta a identidade, mas erra a leitura.** Atribui à tese um repasse ω ≈ 1 que o ensaio não afirma (pela regra do ensaio, ω ≈ 0) e omite o lado convencional (ω < 0). A "tensão" da Conclusão é um espantalho.

O que sobra, e tem valor real, é um exercício de auditoria: mostrar como um resultado anterior aparentemente favorável (β̂_alto > 0) era artefato sazonal e quantificar quão pouco poder há para testar dependência de estado com surpresas mensais. É uma contribuição metodológica e negativa. O título, o resumo e a introdução ainda a apresentam como resposta substantiva a uma pergunta de política.

---

## 5. Teste "e daí?"

- **Para o debate de política** (proposta de Lara Resende): quase nada. O artigo declara não avaliar a proposta, não testar o componente neo-fisheriano, não testar o canal da dívida e não ter poder para H1. A única peça que toca a proposta, a aritmética fiscal, tem o problema do DA2-4.
- **Para a literatura de transmissão monetária no Brasil:** um alerta útil. LPs dependentes de estado com um estado persistente construído a partir da própria Selic produzem |t| grandes por acaso (quantil de 95% = 3,40). Os p-valores NW são enganosos. O efeito desinflacionário de 24 meses depende de p e da medida da taxa. Isso vale publicar, mas como nota metodológica, curta e enquadrada assim.
- **Para finanças das famílias:** o repasse da Selic à taxa média do estoque é conhecido. A magnitude agregada (0,07 p.p. por DP) é pequena e frágil na amostra trimestral.

**Veredito "e daí?":** a versão revisada responde honestamente "não sabemos". Ela ainda não assume que esse é o resultado, e não extrai do "não sabemos" o pouco de informação que os próprios números contêm.

---

### Resumo de severidades

| ID | Severidade | Tema |
|---|---|---|
| DA2-1 | MAIOR | "Nulo informativo"; limites unilaterais e padrão de sinal omitidos |
| DA2-2 | MAIOR | Bootstrap sob a nula aplicado seletivamente; grade descrita seletivamente |
| DA2-3 | MAIOR | H2 mecânico, pequeno, frágil no trimestral e redefinido em relação ao ensaio |
| DA2-4 | MAIOR | ω ≈ 1 atribuído à tese; ω < 0 omitido; indexados; falso dilema |
| DA2-5 | MENOR | Caminhos bifurcados; testes "confirmatórios" pós-exploração |
| DA2-6 | MENOR | Repique pós-platô na Tab. de episódios não comentado |
| DA2-7 | MENOR | Assimetria de H2 a 10%, anomalia em h = 0, anedota confundida |
| DA2-8 | MENOR | Frase de abertura do nulo contradita no próprio resumo |

Nenhum achado CRÍTICO.
