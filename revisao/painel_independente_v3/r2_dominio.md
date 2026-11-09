# Relatório de Revisão por Pares

## Informações do Manuscrito
- **Título**: Patamar de Juros, Dívida Pós-Fixada e Comprometimento de Renda das Famílias: Formalização Analítica e Evidência de Projeções Locais Dependentes de Estado para o Brasil (2005–2026)
- **ID do manuscrito**: não disponível
- **Data da revisão**: 9 de novembro de 2026
- **Rodada**: 1ª rodada (painel simulado; assento isolado)

`criteria_binding_unavailable`

Não há periódico-alvo confirmado. Por isso, este relatório não afirma nada sobre adequação a um periódico e avalia o manuscrito apenas pelos padrões gerais do campo (macroeconomia monetária e fiscal aplicada ao Brasil).

---

## Informações do Revisor

### Papel do revisor
Revisor 2 (Domínio)

### Identidade do revisor
Pesquisador sênior em política monetária brasileira e dominância fiscal. Tenho trabalhos sobre o episódio de 2002–03, o "tight money paradox" (Loyo) e a estrutura da Dívida Pública Mobiliária Federal (LFTs, compromissadas). **Ponto cego declarado: finanças das famílias.** Não avalio aqui o mérito substantivo do Bloco III nem a interpretação das séries 29033/29034 além do que toca o argumento fiscal-monetário.

### Foco da revisão
(1) Precisão da aritmética do Bloco II: λ ≈ 0,50, base DBGG versus DLSP, alívio de 2,3% e de 4,0% do PIB e ausência de resposta endógena de prêmios e de prazo na rolagem. (2) Se a TFNP e o neo-fisherianismo (Cochrane, Sims, Uribe) estão lidos corretamente, incluindo a tese de que *duration* zero elimina o efeito de valor presente. (3) Se a literatura brasileira está completa, e se os ciclos de 2011–13 e 2016–18 são usados como narrativa ou como evidência.

---

## Avaliação Geral

### Recomendação
- [ ] Accept
- [ ] Minor Revision
- [x] **Major Revision**
- [ ] Reject

### Grau de confiança
**4** (o tema está majoritariamente na minha área; o Bloco III, sobre famílias, fica fora dela)

A confiança apenas declara incerteza e escopo. Ela não altera severidade, consenso nem arbitragem.

### Status de calibração
`NOT_CALIBRATED`

### Avaliação-síntese
O artigo formaliza em três blocos a tese de Lara Resende: juros altos persistentes perdem eficácia, e a dívida indexada à Selic tornaria o corte de juros fiscalmente virtuoso. A tese é testada com SVAR e LPs dependentes de estado (2005–2026). Do ponto de vista do domínio, a parte empírica é relatada com honestidade incomum: o próprio autor conclui que H1 não encontra apoio e que γ̂ não discrimina causalidade.

O problema está no Bloco II e na discussão de política, que o próprio texto declara ser a base do argumento a favor da redução da Selic. Há quatro defeitos substantivos:
- **Inconsistência teórica:** o alívio fiscal é calculado em termos nominais, com crescimento nominal fixo, ao mesmo tempo em que se invoca um mecanismo neo-fisheriano. Se esse mecanismo opera, ele anula o alívio na razão dívida/PIB.
- **Aritmética:** a aritmética mistura o custo médio da DPF com a base DBGG e a Selic com o custo médio. Ela ignora o cronograma de rolagem e o prêmio a termo.
- ***Duration*:** o texto afirma que a *duration* zero "elimina" o efeito de valor presente, mas a Eq. (13) do próprio artigo preserva metade dele.
- **Ciclos históricos:** a comparação 2011–13 versus 2016–18 traz fatos fiscais invertidos em nível e é usada como base de avaliação da proposta.

Há ainda uma leitura incorreta do ensaio na discriminação entre Blanchard e Lara Resende: o próprio ensaio aceita o canal cambial no curto prazo. Também é provável que a série SGS 27574 esteja rotulada errado (IC-Br em reais, não em dólares).

Todos os defeitos são corrigíveis sem refazer o núcleo empírico. Por isso a recomendação é Major Revision, não Reject.

---

## Pontos Fortes

### S1: Relato honesto de resultados nulos e das limitações da hipótese
O autor não força a evidência a favor da tese que motiva o artigo. H1 é declarada sem apoio, o resultado positivo sem dummies sazonais é explicitamente descartado e γ̂ recebe a ressalva de causalidade reversa. Em uma literatura em que trabalhos sobre Lara Resende tendem a ser militantes, para um lado ou para o outro, esse é um mérito real.
**Evidence Anchor**: `text: §6 Conclusão "A hipótese $H_1$, na forma em que distingue os regimes, não encontra apoio nos dados."`

### S2: Separação explícita entre a evidência de surpresas marginais e a proposta de mudança de regime
O texto reconhece que choques com desvio-padrão de 0,16 p.p. não informam sobre um corte coordenado de 6,5 p.p. e invoca a crítica de Lucas. Para um artigo que discute a proposta do CFMN, essa é a distinção de domínio correta.
**Evidence Anchor**: `text: §5.2 "não permitem inferir o efeito de uma mudança de regime da ordem de $6{,}5$ p.p., sujeita à crítica de Lucas"`

### S3: Antecedentes brasileiros corretos para a hipótese
O artigo ancora a tese em Loyo (1999), Blanchard (2004) e Favero e Giavazzi (2004), a genealogia correta do argumento de que dívida indexada ao juro curto pode inverter o sinal da política monetária. Também registra a diferença de prescrição entre Blanchard e Lara Resende.
**Evidence Anchor**: `text: §1.1 "formalizou pioneiramente, sob a ótica da TFNP aplicada ao Brasil dos anos 1980 e 1990, o \textit{``tight money paradox''}"`

### S4: Formalização que torna a tese verbal falsificável
A derivação de dπ/di e do limiar θ* identifica com clareza quais parâmetros teriam de prevalecer para que o aperto fosse inflacionário. O modelo inclui o canal de renda financeira (δλb), que é o argumento distributivo de Lara Resende, e o canal de custos. Também é correto o uso de McLeay e Tenreyro (2020) para não ler a FEVD baixa do IBC-Br como κ = 0.
**Evidence Anchor**: `equation: Eq. (theta_star), §2 Bloco II`

### S5: Teste direto do canal cambial por regime
Estimar a resposta da PTAX por regime, em vez de apenas controlar pelas defasagens da PTAX, é a verificação certa para o mecanismo de Blanchard. O artigo admite que a ausência de CDS ou EMBI limita a conclusão. Ressalvo, porém, que a leitura dessa tabela como discriminante entre teorias é problemática (ver W8).
**Evidence Anchor**: `table: Tabela tab:ptax_regime — resposta acumulada da PTAX por regime, h = 0 a 24`

---

## Pontos Fracos

### W1: O alívio fiscal nominal é incompatível com o mecanismo neo-fisheriano invocado
**Problema**: O Bloco II e a Conclusão medem o ganho do corte da Selic como queda da despesa nominal de juros (λbΔi), mantendo g_nom ≈ 7% fixo. O mesmo texto (Bloco II, item 3; Introdução, item 3), apoiado em Cochrane e no ensaio, afirma que, com dívida curta, o corte leva a inflação a convergir para baixo sem repique.
- Pela Eq. (3) do próprio artigo, a dinâmica de b depende de (ī − g_nom)/(1 + g_nom) ≈ r − g real.
- Se a inflação cai junto com i (Fisher: π = i − r com r independente de i, exatamente como o ensaio o formula), g_nom cai na mesma medida e o diferencial ī − g_nom não muda. O alívio na razão dívida/PIB é então aproximadamente nulo.
- O ganho fiscal só existe na medida em que o corte reduz o juro **real**, isto é, na medida em que a política monetária não é neutra. Mas esse é justamente o canal convencional de demanda (σ, κ) que a tese diz estar enfraquecido.
- No arcabouço da TFNP, o que importa é o valor presente dos superávits primários descontado à taxa real. A queda da conta nominal de juros, acompanhada de queda equivalente da inflação, não muda esse valor.

**Evidence Anchor**: `text: §6 Conclusão "um corte da Selic reduz imediatamente a despesa nominal de juros, em cerca de $2{,}3\%$ do PIB no primeiro ano"`
**Por que importa**: A Conclusão declara que "o argumento a favor dessa redução apoia-se, neste artigo, na aritmética fiscal". Essa aritmética contradiz o mecanismo teórico que o artigo usa para afastar o risco inflacionário. Ou há alívio (r cai, e o canal de demanda opera), ou há neutralidade fisheriana (π cai, e o alívio na razão b some). Não é possível ter os dois ao mesmo tempo sem uma rigidez nominal explícita.
**Sugestão**: Reescrever o Bloco II em termos reais. Decompor o efeito do corte sobre Δb em (a) queda do juro real ex post e (b) queda da inflação e do crescimento nominal. Apresentar ao menos dois cenários: inflação rígida no primeiro ano, com alívio real e estímulo de demanda, e ajuste fisheriano pleno, com alívio nulo na razão. Retirar da Conclusão e do Resumo a apresentação do número de 2,3% do PIB como alívio fiscal sem essa qualificação.
**Severity**: Major
**Confidence**: 4 — área central: aritmética da dívida e TFNP

### W2: A aritmética do Bloco II mistura bases, taxas e horizontes
**Problema**: Os números do Bloco II vêm do ensaio sem verificação independente e combinam grandezas incompatíveis:
1. **Custo médio aplicado à base errada.** ī = 12,68% é o *custo médio do estoque da DPF acumulado em 12 meses*, divulgado pelo Tesouro no RMD (setembro de 2026: 12,63%; DPMFi: 13,03%). O texto o aplica à DBGG, que inclui as compromissadas do BCB e exclui a carteira do BCB. O resultado, "R$ 1,4 trilhão (10,5% do PIB)", é um produto hipotético, não a despesa observada. A despesa de juros nominais do setor público consolidado nas NFSP é de cerca de 8,9% do PIB: SGS 5727 menos SGS 5793 dá 9,48 − 0,62 em agosto de 2026, e a imprensa reporta R$ 1,18 trilhão em 12 meses. Esse número próximo de 8,7–8,9% é o que o próprio ensaio cita para a base líquida.
2. **Selic confundida com custo médio.** LFTs e compromissadas pagam a Selic, não o custo médio. O custo de emissão das LFTs em 12 meses foi de 14,40% (RMD de setembro de 2026), e a Selic na base do próprio autor é de 13,94% em agosto de 2026. Mesmo assim, o "alívio imediato" usa Δi = −5,5 p.p. ("de 13,0% para 7,5%"). A Seção 5.2, por sua vez, fala em "∼14% para 7,5%" e em "6,5 p.p.". O texto adota duas magnitudes diferentes para o mesmo choque.
3. **Horizonte.** A proposta do ensaio prevê redução *gradual em cerca de 12 meses*. Com um corte gradual, o alívio médio no primeiro ano é aproximadamente metade do alívio em regime permanente. Chamá-lo de "imediato... no primeiro ano" não é consistente com a proposta avaliada.
4. **λ não documentado.** O valor "≈ 0,50" corresponde à participação da taxa flutuante na DPF (48,3% em dezembro de 2025 e 52% em setembro de 2026, segundo o RMD), mas é aplicado a b = DBGG e descrito como "LFTs e compromissadas". Se as compromissadas entram no numerador, o λ relevante sobre a DBGG é diferente de 0,50. Na base líquida (DLSP), a exposição à Selic também é outra, porque parte dos ativos do setor público rende Selic ou taxas correlatas.
5. **Incoerência interna.** A Introdução fala em crescimento relativo de "5,7% ao ano" da razão, enquanto a Eq. (3) aplicada aos mesmos dados dá 5,3%. A Seção 5.1 fala em "ī − g > +5,5%".

**Evidence Anchor**: `text: §2 Bloco II "o \textbf{alívio fiscal imediato é de $\approx 2{,}27\%$ do PIB} no primeiro ano"`
**Por que importa**: Esta é a parte do artigo que, segundo o próprio autor, "independe das estimativas econométricas" e sustenta a discussão de política. Com a Selic de fato vigente e corte imediato, o alívio bruto seria maior (cerca de 0,5 × 0,83 × 6,4 ≈ 2,7% do PIB). Com o corte gradual, seria menor no primeiro ano. Na base líquida, seria menor ainda. O número de 2,3% não corresponde a nenhum cenário bem definido.
**Sugestão**: Incluir uma tabela de insumos fiscais com fonte, data e conceito de cada número: SGS 13762 (DBGG), 4513 (DLSP), 5727 e 5793 (NFSP); RMD/Tesouro (composição e custo da DPF); estoque de compromissadas. Usar a base líquida e as NFSP para fluxos de juros e a DBGG apenas para estoques. Distinguir a Selic (que remunera LFT e compromissadas) do custo médio. Fazer o alívio seguir a trajetória gradual da proposta e apresentar uma grade de sensibilidade em λ, Δi e base. Reconciliar o +4,4 p.p. ao ano com a variação observada da DBGG: +2,4 p.p. de dezembro de 2024 a dezembro de 2025 e +5,7 p.p. de junho de 2025 a junho de 2026 (SGS 13762), usando os fatores condicionantes divulgados pelo BCB.
**Severity**: Major
**Confidence**: 4 — área central (DPMFi, NFSP); números conferidos na API do SGS e no RMD de setembro de 2026

### W3: O alívio de 4,0–4,5% do PIB "após rolagem" supõe que toda a curva converge para 7,5%
**Problema**: O alívio "após rolagem" equivale a refinanciar todo o estoque ao novo patamar da Selic (5,5 × 0,825 ≈ 4,5). Isso pressupõe:
- **Fim do prêmio a termo e do juro real longo.** As NTN-Bs custam IPCA mais o cupom real. Em setembro de 2026, o custo médio de emissão em 12 meses foi de 7,64% real + 4,30% de IPCA = 12,27% (RMD). Refinanciá-las a 7,5% nominais exigiria juro real longo de cerca de 3%.
- **Rolagem rápida.** O prazo médio da DPF é de 4,10 anos, e só 19,95% do estoque vence em 12 meses (RMD, setembro de 2026). O "gradualmente" do texto corresponde a vários anos.
- **Nenhuma resposta endógena de prêmios.** É exatamente o que o modelo do próprio artigo, via θ e ρ'(b), diz que pode ocorrer se o corte for lido como dominância fiscal.

Além disso, o spread das LFTs (ágio ou deságio sobre a Selic) não tem *duration* zero em relação ao risco fiscal. Ele é a margem pela qual o prêmio de risco se manifesta na parte pós-fixada.

**Evidence Anchor**: `text: §2 Bloco II "ampliando-se gradualmente para \textbf{$\approx 4{,}0\%$ a $4{,}5\%$ do PIB} à medida que as parcelas prefixadas vencem e são refinanciadas ao novo patamar"`
**Por que importa**: O número de 4% do PIB vem do ensaio e é o argumento retórico mais forte da proposta. Reproduzi-lo sem condicionantes transforma em fato contábil algo que depende da hipótese contestada: que a credibilidade fiscal e monetária sobreviveria ao corte.
**Sugestão**: Apresentar a rolagem com o cronograma efetivo de vencimentos e com cenários de prêmio a termo e de juro real longo (por exemplo, curva inalterada, curva paralela a −Δi e curva com prêmio elevado). Declarar explicitamente que 4% é um limite superior, condicional a prêmio a termo nulo.
**Severity**: Major
**Confidence**: 4 — área central: composição e custo da DPMFi

### W4: "*Duration* zero elimina o efeito de valor presente" está superdimensionado
**Problema**: O Resumo afirma que o corte reduz os encargos "sem elevar o valor presente do passivo público". A Eq. (13) do próprio artigo mostra que só a parcela λ ≈ 0,5 tem *duration* zero. A parcela (1 − λ), com prefixados e NTN-Bs e um prazo médio de 4,1 anos para a DPF, se valoriza com o corte. Pela lógica que o artigo atribui a Cochrane (2023) e a Sims (2011) para a dívida longa, o Brasil é um caso **intermediário**: o canal de repique de curto prazo fica reduzido, não eliminado. A Introdução (item 3) repete a afirmação sem a ressalva.
**Evidence Anchor**: `text: Resumo "reduzem imediatamente o fluxo nominal de encargos (...) sem elevar o valor presente do passivo público"`
**Por que importa**: Essa é a afirmação teórica central que separa a proposta de Lara Resende da recomendação usual da TFNP. Exagerá-la contraria a equação do próprio artigo e a leitura correta de Cochrane e de Sims (2011), na qual a maturidade da dívida determina a *magnitude* do efeito de curto prazo.
**Sugestão**: Substituir "sem elevar" por "elevando apenas a parcela de *duration* positiva (≈ metade do estoque)". Quantificar a variação de valor de mercado da parcela prefixada e indexada a um corte de Δi com a *duration* efetiva (RMD). Discutir o spread da LFT como canal remanescente de valor.
**Severity**: Major
**Confidence**: 4 — área central: TFNP e estrutura da DPMFi

### W5: O "canal fiscal-expectacional" da Eq. (5) é rotulado como TFNP, mas é um canal de solvência e risco de *default*
**Problema**: Na Eq. (5), as expectativas de inflação sobem com a velocidade de crescimento da dívida (θ ∂Δb/∂i). Isso é um canal *ad hoc* de desconfiança na solvência, mais próximo de Blanchard (2004) e da leitura do próprio ensaio ("dívidas que possam vir a não ser honradas") do que da equação de valoração da TFNP. Nesta, o nível de preços ajusta o valor real do passivo ao valor presente dos superávits descontado pelo juro real, e um corte de juros que reduz o juro real **eleva** esse valor presente, com efeito desinflacionário na TFNP. O texto (Bloco II e Seção 1, item 3) atribui à TFNP propriedades que vêm de outro mecanismo.
**Evidence Anchor**: `equation: Eq. (eq:expectations), §2 Bloco II — termo θ·(∂Δb_t/∂i_t)·i_t`
**Por que importa**: A confusão impede o leitor de saber qual teoria está sendo formalizada e torna ainda mais difícil distinguir Lara Resende de Blanchard (ver W8).
**Sugestão**: Renomear o canal como "solvência fiscal e prêmio de risco nas expectativas" e reservar "TFNP" para a equação de valoração. Se o autor quiser um canal TFNP genuíno, escrever a restrição de valor presente e mostrar o papel da taxa de desconto real.
**Severity**: Minor
**Confidence**: 4 — área central: TFNP

### W6: Os ciclos de 2011–13 e 2016–18 têm fatos fiscais invertidos e são usados como evidência
**Problema**: A comparação descreve 2011–13 com "deterioração progressiva do resultado primário" e 2016–18 com "contenção fiscal primária". Em nível, ocorreu o inverso. O resultado primário do setor público consolidado (SGS 5793, 12 meses, % do PIB; sinal das NFSP, em que valor negativo indica superávit) foi:

| Ano | Resultado primário (% do PIB) |
|---|---|
| 2011 | superávit de 2,94 |
| 2012 | superávit de 2,18 |
| 2013 | superávit de 1,71 |
| 2016 | déficit de 2,48 |
| 2017 | déficit de 1,68 |
| 2018 | déficit de 1,55 |

O que distinguiu 2016–18 foi a mudança nas expectativas de superávits futuros (EC 95/2016, o teto de gastos), a credibilidade renovada do BCB, um hiato do produto muito negativo após a recessão de 2015–16 e o choque favorável de alimentos em 2017. Não foi contenção primária corrente.

A Seção 5.2 declara que a avaliação da proposta "apoia-se sobretudo na aritmética fiscal da Seção 2 e na comparação entre os ciclos". Isso eleva uma narrativa com n = 2, sem nenhum dado apresentado, à condição de evidência.

**Evidence Anchor**: `text: §1.1 "sob ancoragem institucional das expectativas, estabilidade cambial e contenção fiscal primária, resultando em rápida convergência da inflação"`
**Por que importa**: (a) É um erro factual verificável em números fiscais. (b) O episódio de 2016–18 é ambíguo para a tese, porque a Selic caiu a partir de um platô de 14,25% enquanto a inflação caía. Ele é compatível com efeitos defasados do aperto de 2015–16 e com a recessão, mas também com a leitura de Lara Resende, e o artigo não o explora nem num sentido nem no outro. (c) Uma base de avaliação que não discrimina hipóteses não pode sustentar as "salvaguardas" propostas.
**Sugestão**: Corrigir os fatos fiscais, separando o fluxo primário corrente das expectativas de superávit futuro. Ou reduzir a comparação a uma ilustração explicitamente narrativa, ou transformá-la num estudo de caso estruturado com dados: Focus, primário, hiato, câmbio, alimentos e Selic real *ex ante*, nos dois ciclos. Retirar da Seção 5.2 a frase que faz a avaliação da proposta repousar nesse contraste.
**Severity**: Major
**Confidence**: 5 — números conferidos na API do SGS (série 5793)

### W7: Lara Resende ora aparece como hipótese, ora como autoridade
**Problema**: A Introdução apresenta como "fatos estilizados" números e códigos SGS copiados do ensaio, inclusive a referência ao FMI, sem verificação própria (ver W2). O item 3 transforma uma proposição teórica contestada em fato. A Seção 5.1 (item 3) afirma que atribuir o crescimento da dívida ao diferencial de juros "é contábil e independe das estimativas". A identidade é contábil, mas a atribuição causal à Selic, isto é, o contrafactual de que a Selic poderia ser menor sem que a inflação e os prêmios mudassem, não é. A Seção 5.2 adota o enquadramento do ensaio ("Para superar a armadilha de juros elevados..."), e "André Lara Resende" aparece como palavra-chave.
**Evidence Anchor**: `text: §1 item 3 "reduz imediatamente a despesa nominal de juros do Tesouro, melhorando a trajetória fiscal sem exigir um repique inflacionário de curto prazo"`
**Por que importa**: O valor do artigo está em testar a tese. Ao adotar as premissas do ensaio como fatos na Introdução e na Discussão, o texto pressupõe a parte que deveria examinar, e o leitor perde a distinção entre o que foi testado (e rejeitado, no caso de H1) e o que é afirmação do ensaio.
**Sugestão**: Reformular a Introdução como "proposições de Lara Resende (2026)", cada uma com o status (fato verificado / proposição teórica / conjectura) e com verificação própria dos números. Na Seção 5.1, item 3, separar a identidade contábil do contrafactual. Retirar o nome próprio das palavras-chave.
**Severity**: Major
**Confidence**: 4 — leitura do ensaio e do manuscrito

### W8: A discriminação entre Blanchard e Lara Resende parte de uma leitura incorreta do ensaio
**Problema**: A Seção 5.1 opõe os dois autores pelo canal: "a primeira, por depreciação cambial; a segunda, por canais domésticos". O ensaio, porém, **adota** o canal cambial como explicação da relação inversa de curto prazo entre juros e inflação: o corte provoca saída de *carry trade*, depreciação e inflação. A proposta neutraliza esse canal com as reservas. Além disso, em Blanchard (2004) o gatilho também é o juro real elevando o serviço de uma dívida indexada à Selic e ao câmbio. Os dois diferem sobretudo (i) na fatia de dívida em moeda estrangeira e no elo probabilidade de *default* → aversão ao risco → câmbio, e (ii) na prescrição. A tese de Loyo é, por sua vez, o mesmo mecanismo de dívida curta. O desenho do artigo, sem CDS ou EMBI e com uma tabela de PTAX de baixa potência, não separa os mecanismos. Ele também não poderia separá-los com o critério de canal adotado, porque os dois preveem depreciação após o corte no curto prazo.
**Evidence Anchor**: `text: §5.1 "preveem ambas que a Selic perde potência desinflacionária no platô alto, mas por canais diferentes: a primeira, por depreciação cambial; a segunda, por canais domésticos"`
**Por que importa**: A seção pretende delimitar o que a evidência diz sobre duas teorias concorrentes, mas a delimitação parte de uma premissa equivocada sobre uma delas.
**Sugestão**: Reescrever a Seção 5.1 com o critério certo. As implicações que de fato separam as teorias são: o papel do primário corrente *versus* o nível do juro; a reação do prêmio soberano (CDS ou EMBI) e do spread das LFTs ao aperto no platô; e a dependência da fatia de dívida cambial (alta em 2002–03, baixa em 2025–26). Declarar explicitamente que o desenho atual não discrimina as duas teorias.
**Severity**: Major
**Confidence**: 4 — leitura direta do ensaio (págs. 9–10 do PDF) e de Blanchard (2004)

### W9: H1 testa surpresas transitórias, enquanto a tese neo-fisheriana trata de mudanças permanentes de patamar
**Problema**: H1(ii) prevê β_alto ≥ 0 para choques de Cholesky, que são surpresas transitórias em torno da regra. Na formulação do ensaio, a relação positiva entre juro e inflação vale "no longo prazo", e "no curto prazo, a relação pode ser inversa". O próprio Uribe (2022), citado no artigo, conclui que choques transitórios continuam desinflacionários e que o efeito neo-fisheriano aparece em mudanças permanentes. Assim, a rejeição de H1 informa sobre o canal de custos e o canal de prêmio fiscal, mas pouco diz sobre a dimensão neo-fisheriana atribuída a Lara Resende. O texto não deixa isso claro.
**Evidence Anchor**: `text: §1 Hipótese H1 "(ii) $\beta_{alto}^h \ge 0$ no platô persistentemente elevado (canal de custos e de prêmio de risco fiscal)"`
**Por que importa**: Sem essa delimitação, um leitor pode tomar a rejeição de H1 como rejeição da tese neo-fisheriana. Um defensor da tese poderia, com razão, dizer que ela não foi testada.
**Sugestão**: Declarar quais componentes da tese cada hipótese testa. Ou adotar uma decomposição permanente versus transitória no espírito de Uribe (2022), ou reconhecer explicitamente que o componente neo-fisheriano não é testado.
**Severity**: Major
**Confidence**: 4 — área central: literatura neo-fisheriana

### W10: O efeito de nível γ̂ é a própria relação de Fisher, que é neutra entre teorias
**Problema**: O artigo apresenta γ̂ > 0 como "compatível com a tese de Lara Resende" e com causalidade reversa. Juros nominais altos associados a inflação mais alta é o que a equação de Fisher prevê em qualquer teoria, convencional ou neo-fisheriana. O fato de o resultado desaparecer quando o regime é definido pelo juro real *ex ante* confirma essa leitura.
**Evidence Anchor**: `text: §6 Conclusão "ele é compatível com a tese de \citet{resende2026euacuso}, mas também com a manutenção de juros altos quando a inflação é persistente"`
**Por que importa**: γ̂ é chamado de "resultado mais estável do artigo", mas, do ponto de vista teórico, não carrega informação discriminante.
**Sugestão**: Dizer explicitamente que γ̂ espelha a relação de Fisher e não discrimina entre teorias, e deixá-lo como resultado descritivo.
**Severity**: Minor
**Confidence**: 4 — área central

### W11: A série SGS 27574 parece ser o IC-Br em reais, não em dólares
**Problema**: A Tabela 1 descreve ICBr como "Índice de Commodities Brasil em USD, SGS 27574", e o script repete o rótulo. Comparei a série da base com a SGS 29042 para 2005–2026, em variações mensais de log. A diferença entre as duas tem correlação de 0,70 com a variação da PTAX de fim de período, e a razão de crescimento acumulado de 27574/PTAX (×2,20) é praticamente igual à de 29042 (×2,24). Isso indica que 27574 é a versão em reais e 29042, a versão em dólares. A evidência é indireta e deve ser confirmada no metadado do SGS.
**Evidence Anchor**: `table: Tabela tab:series — linha ICBr_t "Índice de Commodities Brasil em USD", BCB/SGS 27574`
**Por que importa**: Um índice em reais contém o câmbio e está ordenado antes da PTAX como "choque externo de oferta". Se confirmado, o primeiro bloco do ordenamento não tem a interpretação declarada, e o SVAR e as LPs precisam ser reestimados. Deixo as consequências para a identificação ao revisor de metodologia; meu ponto é a precisão factual da série.
**Sugestão**: Confirmar o metadado. Se confirmado, usar a SGS 29042 (ou a versão em USD indicada pelo BCB) e reestimar, ou corrigir o rótulo e justificar o ordenamento.
**Severity**: Major
**Confidence**: 4 — verificação própria na API do SGS; metadado não confirmado

### W12: Atribuição a Cochrane (2026) de uma afirmação específica sobre o Brasil e a Selic
**Problema**: O texto atribui a "Resende (2026) e Cochrane (2026)" a tese de que "o próprio nível excessivo da Selic sob primário equilibrado é o gerador da dinâmica explosiva da dívida", e cita Cochrane (2026) para "D_LFT = 0" no Brasil. Pelo que o próprio ensaio relata, os posts de Cochrane defendem reduzir juros encurtando a maturidade da dívida e comentam Bigio e Mengus. Nada no ensaio indica que tratem da Selic ou do Brasil. Não consegui localizar os posts para conferir.
**Evidence Anchor**: `text: §1.1 "o próprio nível excessivo da Selic sob primário equilibrado é o gerador da dinâmica explosiva da dívida"`
**Por que importa**: Atribuir a um autor de referência em TFNP uma tese sobre o Brasil que ele possivelmente não formulou reforça indevidamente a autoridade da hipótese (ver W7).
**Sugestão**: Citar Cochrane apenas pelo que os posts dizem, com o URL completo de cada post (o .bib traz só o domínio), e atribuir as proposições sobre o Brasil somente a Lara Resende.
**Severity**: Minor
**Confidence**: 3 — não tive acesso aos posts

### W13: Lacunas na literatura de fundamentos e na literatura brasileira
**Problema**: Faltam:
- **TFNP e "unpleasant arithmetic":** os textos originais (Sargent e Wallace, 1981; Leeper, 1991; Sims, 1994; Woodford, 1995). O artigo cita apenas Cochrane, e Loyo (1999) é uma extensão direta desses trabalhos.
- **Teoria neo-fisheriana:** Garín, Lester e Sims (2018); Schmitt-Grohé e Uribe (2017); Cochrane (2018).
- **Transmissão monetária no Brasil:** Minella (2003); Minella e Souza-Sobrinho (2013), que, a propósito, apontam o canal de juros das famílias como o mais importante para o produto.
- **Dominância fiscal no Brasil:** Tanner e Ramos (2003); Ayres, Garcia, Guillén e Kehoe (2021).
- **Juro real elevado no Brasil:** Segura-Ubiergo (2012) e, sobretudo, Gonçalves, Holland e Spacov (2007), que testam a conjectura de Arida, Bacha e Lara-Resende e obtêm resultados em geral desfavoráveis. O artigo usa ABL como fundamento de r* = g + ρ(b*) sem mencionar essa evidência contrária, e a fórmula com ρ(b) fiscal não está em ABL, que trata de incerteza jurisdicional e inconversibilidade.
- **Inflação inercial:** o texto canônico (Arida e Lara-Resende, 1985).

**Evidence Anchor**: `absence: §1 e §1.1 (Introdução e Diálogo com a Literatura) e referencias.bib — expected referências originais de TFNP e Sargent–Wallace, literatura empírica brasileira de transmissão e de dominância fiscal, e evidência contrária a ABL; checked §1, §1.1, §2, §5 e referencias.bib integral`
**Por que importa**: A ausência de evidência contrária a ABL é a mais séria, porque um bloco do modelo (o item 3 do Bloco II) se apoia em ABL. As demais lacunas afetam o posicionamento da contribuição.
**Sugestão**: Ver a lista em "Referências-chave ausentes". [FIELD-NORM UNVERIFIED]: não fundamentei em fonte externa a norma de que o campo exige a citação desses textos, por isso a severidade fica em Minor.
**Severity**: Minor
**Confidence**: 4 — área central

---

## Julgamentos Vinculados a Critérios

| Dimensão / critério | Fonte do critério | Julgamento | Âncoras de evidência | Justificativa | Incerteza ou limite de escopo | Pesa na decisão? |
|---|---|---|---|---|---|---|
| Precisão factual de números fiscais e séries SGS | Cartão de configuração, foco (1) | DOES_NOT_MEET | W2, W3, W6, W11 | Base e taxa misturadas, rolagem irrealista, primário dos ciclos invertido, provável rótulo errado de série | Metadado de 27574 não confirmado | sim — sustenta a discussão de política |
| Leitura de TFNP e neo-fisherianismo | Cartão, foco (2) | PARTLY_MEETS | W1, W4, W5, W9, S4 | A estrutura é boa, mas há contradição alívio × Fisher e exagero sobre a *duration* | — | sim — núcleo teórico |
| Completude da literatura brasileira | Cartão, foco (3) | PARTLY_MEETS | W13, S3 | Os antecedentes certos estão presentes; faltam a literatura empírica e a evidência contrária a ABL | Severidade limitada por norma não fundamentada | não, isoladamente |
| Ciclos históricos: narrativa × evidência | Cartão, foco (3) | DOES_NOT_MEET | W6 | n = 2, sem dados e com fatos invertidos, usado como base de avaliação | — | sim |
| Lara Resende como hipótese × autoridade | Cartão, "tende a cobrar" | PARTLY_MEETS | W7, W12, S1, S2 | Os resultados são honestos, mas a Introdução e a Discussão adotam as premissas do ensaio | — | sim — enquadramento |
| Discriminação Blanchard × Lara Resende | Cartão, "tende a cobrar" | PARTLY_MEETS | W8, S5 | O autor reconhece que a discriminação é limitada, mas o critério de canal está errado | — | sim |
| Contribuição e posicionamento | Protocolo do Revisor 2, passo 4 | MEETS | S1, S4 | Primeiro teste empírico formal e transparente da tese, com resultado majoritariamente nulo | Depende de correções no Bloco II | não |

Estes julgamentos não foram somados nem ponderados para chegar à recomendação.

---

## Comentários Detalhados

### Título e Resumo
- O Resumo reproduz a tese de que o corte se dá "sem elevar o valor presente do passivo público" e o número de 2,3% e 4,0% do PIB, o que já antecipa os problemas de W1 a W4. Com as correções, o Resumo deveria apresentar esses números como cenários condicionais.

### Introdução e revisão da literatura
- **Cobertura**: a genealogia Loyo, Blanchard, Favero-Giavazzi e ABL é correta (S3), mas faltam os fundamentos e a literatura empírica brasileira (W13).
- **Integração**: a seção sintetiza criticamente, além de enumerar, sobretudo no item sobre o efeito-informação e McLeay-Tenreyro. O item sobre os ciclos históricos é narrativa sem dados (W6).
- **Lacuna de pesquisa**: o artigo seria o primeiro teste formal da tese de Lara Resende com dados recentes. É uma lacuna real, mas o argumento é enfraquecido pela adoção das premissas do ensaio como fatos (W7).

### Arcabouço teórico
- **Adequação**: o modelo em três blocos é uma escolha razoável para tornar a tese falsificável (S4).
- **Profundidade**: a aplicação da TFNP é superficial no ponto crucial, porque o canal "fiscal-expectacional" não é a equação de valoração (W5). A *duration* zero é exagerada (W4), e a aritmética nominal contradiz a neutralidade fisheriana (W1).
- **Alternativas**: um modelo com TFNP genuína e dívida de maturidade geométrica, no espírito de Cochrane (2023) e Sims (2011), calibrado com a *duration* da DPMFi, permitiria quantificar o efeito "intermediário" brasileiro. Seria uma contribuição teórica própria e original.

### Qualidade da argumentação
- **Precisão factual**: ver W2, W3, W6 e W11. Também: o resultado primário de 12 meses em junho de 2026 era um déficit de 1,19% do PIB (SGS 5793), fora do intervalo de "0,4% a 0,7%" citado. O intervalo vale para dezembro de 2025 (0,43) e agosto de 2026 (0,62). Convém fixar a data de referência. A DBGG de agosto de 2026, fim da amostra, era de 82,9% do PIB (SGS 13762); o texto usa 82,5% (junho).
- **Lógica**: o salto lógico principal é W1. A Seção 5.1, item 3 ("argumento contábil"), confunde identidade com contrafactual (W7).
- **Terminologia**: "TFNP" usada para um canal de risco de *default* (W5). "Choque de −1 p.p." lido às vezes como corte (o texto, corretamente, se corrige na especificação assimétrica).

### Contribuição para o campo
- **Incremental**: um teste empírico transparente, com p-valores de Holm e robustez extensa, de uma tese muito presente no debate brasileiro. O resultado é majoritariamente nulo para H1, o que tem valor informativo.
- **Posicionamento**: é preciso deixar claro quais componentes da tese foram testados (W9) e quais não podem ser discriminados (W8).
- **Exagero**: aparece no Bloco II e na Discussão de política, não na parte empírica.

---

## Perguntas ao Autor

1. No seu próprio modelo, se o corte de 5,5 p.p. levar a inflação a cair na mesma magnitude no horizonte relevante, como prevê o mecanismo fisheriano que o texto invoca, qual é o alívio na **razão** dívida/PIB? Se a resposta for "positivo", qual rigidez nominal o garante, e por que essa rigidez não reativa o canal convencional de demanda?
2. Qual é a fonte exata de ī = 12,68% e de λ ≈ 0,50? Qual é a participação indexada à Selic (LFT + compromissadas) na DBGG e na DLSP na data de referência, e por que a Selic vigente (~14%) não é usada como Δi da parcela pós-fixada?
3. Que passagem de Cochrane (2026) sustenta afirmações sobre a Selic e o Brasil?
4. A série usada como "IC-Br em USD" é a 27574 ou a 29042? Os resultados das Tabelas 2 a 6 se mantêm com a versão em dólares?

---

## Problemas Menores

### Linguagem e consistência interna
- Introdução: "5,7% ao ano" contra os 5,3% da Eq. (3); Seção 5.1: "> +5,5%". Uniformizar.
- Bloco II, item 3: "r* = g + ρ(b*)" implica, com os números dados (g real ≈ 2–2,5%), um prêmio de cerca de 6 p.p. sem fonte, e a fórmula não está em ABL.
- Seção 1.1: Uribe (2022) é descrito como "aumentos permanentes... acompanhados de acomodação inflacionária". A formulação é imprecisa: o resultado é que aumentos permanentes da taxa nominal elevam a inflação já no curto prazo.
- García-Schmidt e Woodford (2019): o resultado é mais forte do que "não produz deflação imediata", porque, sob equilíbrio reflexivo, juros baixos prolongados tendem a ser *inflacionários*. Convém dizê-lo, já que contraria diretamente a proposta.
- Sims (2011) é citado como inspiração "neo-fisheriana", mas seu mecanismo central é a dívida longa, e o texto ficaria mais útil no Bloco II, junto à Eq. (13).
- Retirar "André Lara Resende" das palavras-chave.

### Formato das citações
- Blanchard (2004) e Favero e Giavazzi (2004) foram publicados em Giavazzi, Goldfajn e Herrera (orgs.), *Inflation Targeting, Debt, and the Brazilian Experience, 1999 to 2003* (MIT Press, 2005), o mesmo volume de ABL. Preferir as versões publicadas.
- A chave `pastore1996reforma` não corresponde à entrada (artigo de 1995). Além disso, "Passividade monetária e inércia" trata de passividade monetária e inércia, não do *price puzzle* em VARs, e não sustenta a frase em que é citado. Verificar a paginação.
- `resende1980causas`: verificar ordem dos autores (Lopes e Lara Resende?), ano, volume e paginação em *Pesquisa e Planejamento Econômico* (a verificar).
- `cochrane2026reasons`: incluir os URLs completos dos dois posts.
- Entradas do .bib que não são citadas (`serrano2010juros`, `resende2014limites`) podem ser removidas ou citadas.

### Figuras e tabelas
- Tabela 1: corrigir o rótulo de 27574 (W11). Indicar a data de acesso e a versão das séries do SGS.

---

## Referências-chave ausentes

- Sargent, T. J.; Wallace, N. (1981). Some unpleasant monetarist arithmetic. *Federal Reserve Bank of Minneapolis Quarterly Review*, 5(3), 1–17. Base do "tight money paradox".
- Leeper, E. M. (1991). Equilibria under "active" and "passive" monetary and fiscal policies. *Journal of Monetary Economics*, 27(1), 129–147. Fundamento da TFNP.
- Sims, C. A. (1994). A simple model for study of the determination of the price level and the interaction of monetary and fiscal policy. *Economic Theory*, 4(3), 381–399. Fundamento da TFNP.
- Woodford, M. (1995). Price-level determinacy without control of a monetary aggregate. *Carnegie-Rochester Conference Series on Public Policy*, 43, 1–46. Fundamento da TFNP.
- Cochrane, J. H. (2018). Michelson-Morley, Fisher, and Occam: the radical implications of stable quiet inflation at the zero bound. *NBER Macroeconomics Annual 2017*, 32, 113–226 (paginação a verificar). Base acadêmica do argumento neo-fisheriano de Cochrane, preferível aos posts.
- Garín, J.; Lester, R.; Sims, E. (2018). Raise rates to raise inflation? Neo-Fisherianism in the New Keynesian model. *Journal of Money, Credit and Banking*, 50(1), 243–259. Condições para o efeito neo-fisheriano.
- Schmitt-Grohé, S.; Uribe, M. (2017). Liquidity traps and jobless recoveries. *American Economic Journal: Macroeconomics*, 9(1), 165–204 (paginação a verificar). Origem do argumento neo-fisheriano de Uribe.
- Minella, A. (2003). Monetary policy and inflation in Brazil (1975–2000): a VAR estimation. *Revista Brasileira de Economia*, 57(3), 605–635. Referência de VARs de política monetária no Brasil.
- Minella, A.; Souza-Sobrinho, N. F. (2013). Monetary policy channels in Brazil through the lens of a semi-structural model. *Economic Modelling*, 30, 405–419. Canais de transmissão no Brasil, incluindo juros das famílias.
- Tanner, E.; Ramos, A. M. (2003). Fiscal sustainability and monetary versus fiscal dominance: evidence from Brazil, 1991–2000. *Applied Economics*, 35(7), 859–873. Testes de dominância no Brasil.
- Ayres, J.; Garcia, M.; Guillén, D.; Kehoe, P. (2021). The monetary and fiscal history of Brazil, 1960–2016. Em: Kehoe, T. J.; Nicolini, J. P. (orgs.), *A Monetary and Fiscal History of Latin America, 1960–2017*. Minneapolis: University of Minnesota Press. Contexto histórico da interação fiscal-monetária.
- Gonçalves, F. M.; Holland, M.; Spacov, A. D. (2007). Can jurisdictional uncertainty and capital controls explain the high level of real interest rates in Brazil? Evidence from panel data. *Revista Brasileira de Economia*, 61(1), 49–76. Evidência contrária a ABL, usada no Bloco II.
- Segura-Ubiergo, A. (2012). The puzzle of Brazil's high interest rates. *IMF Working Paper* 12/62. Determinantes do juro real brasileiro.
- Arida, P.; Lara-Resende, A. (1985). Inertial inflation and monetary reform: Brazil. Em: Williamson, J. (org.), *Inflation and Indexation: Argentina, Brazil, and Israel*. Washington/Cambridge, MA: Institute for International Economics/MIT Press. Referência canônica da inflação inercial, preferível a 1980 para o argumento do item 2.

~~~yaml suggested-references
- title: "Some unpleasant monetarist arithmetic"
  authors: ["Sargent, T. J.", "Wallace, N."]
  year: "1981"
  doi: null
  arxiv_id: null
- title: "Equilibria under 'active' and 'passive' monetary and fiscal policies"
  authors: ["Leeper, E. M."]
  year: "1991"
  doi: null
  arxiv_id: null
- title: "A simple model for study of the determination of the price level and the interaction of monetary and fiscal policy"
  authors: ["Sims, C. A."]
  year: "1994"
  doi: null
  arxiv_id: null
- title: "Price-level determinacy without control of a monetary aggregate"
  authors: ["Woodford, M."]
  year: "1995"
  doi: null
  arxiv_id: null
- title: "Michelson-Morley, Fisher, and Occam: The radical implications of stable quiet inflation at the zero bound"
  authors: ["Cochrane, J. H."]
  year: "2018"
  doi: null
  arxiv_id: null
- title: "Raise rates to raise inflation? Neo-Fisherianism in the New Keynesian model"
  authors: ["Garín, J.", "Lester, R.", "Sims, E."]
  year: "2018"
  doi: null
  arxiv_id: null
- title: "Liquidity traps and jobless recoveries"
  authors: ["Schmitt-Grohé, S.", "Uribe, M."]
  year: "2017"
  doi: null
  arxiv_id: null
- title: "Monetary policy and inflation in Brazil (1975-2000): a VAR estimation"
  authors: ["Minella, A."]
  year: "2003"
  doi: null
  arxiv_id: null
- title: "Monetary policy channels in Brazil through the lens of a semi-structural model"
  authors: ["Minella, A.", "Souza-Sobrinho, N. F."]
  year: "2013"
  doi: "10.1016/j.econmod.2012.04.027"
  arxiv_id: null
- title: "Fiscal sustainability and monetary versus fiscal dominance: evidence from Brazil, 1991-2000"
  authors: ["Tanner, E.", "Ramos, A. M."]
  year: "2003"
  doi: "10.1080/0003684032000056832"
  arxiv_id: null
- title: "The monetary and fiscal history of Brazil, 1960-2016"
  authors: ["Ayres, J.", "Garcia, M.", "Guillén, D.", "Kehoe, P."]
  year: "2021"
  doi: null
  arxiv_id: null
- title: "Can jurisdictional uncertainty and capital controls explain the high level of real interest rates in Brazil? Evidence from panel data"
  authors: ["Gonçalves, F. M.", "Holland, M.", "Spacov, A. D."]
  year: "2007"
  doi: null
  arxiv_id: null
- title: "The puzzle of Brazil's high interest rates"
  authors: ["Segura-Ubiergo, A."]
  year: "2012"
  doi: null
  arxiv_id: null
- title: "Inertial inflation and monetary reform: Brazil"
  authors: ["Arida, P.", "Lara-Resende, A."]
  year: "1985"
  doi: null
  arxiv_id: null
~~~

---

## Fontes consultadas pelo revisor (verificação de fatos)

- API do SGS/BCB (consultada em 9 nov. 2026): séries 5793 (resultado primário NFSP, % do PIB, 12 meses; dezembro de 2011 a 2018, dezembro de 2025, junho e agosto de 2026), 5727 (resultado nominal NFSP), 13762 (DBGG, % do PIB), 4513 (DLSP, % do PIB), 27574 e 29042 (IC-Br), via `https://api.bcb.gov.br/dados/serie/bcdata.sgs.{código}/dados`.
- Tesouro Nacional, Relatório Mensal da Dívida (RMD), apresentação de setembro de 2026 (composição da DPF por indexador, faixas do PAF 2026, custo médio do estoque e das emissões, prazo médio, % vincendo em 12 meses): [Apresentacao-RMD-Setembro-2026.pdf](https://static.poder360.com.br/uploads/2026/10/Apresentacao-RMD-Setembro-2026.pdf)
- [Poder360 — Custo da dívida pública sobe para 12,63% ao ano em setembro](https://www.poder360.com.br/poder-economia/custo-da-divida-publica-sobe-para-1263-ao-ano-em-setembro/)
- [Poder360 — Dívida bruta atinge 82,9% do PIB em agosto](https://www.poder360.com.br/poder-economia/divida-bruta-atinge-829-do-pib-em-agosto-diz-banco-central/)
- [Paraíba Business — Juros da dívida pública chegam a R$ 1,18 trilhão em 12 meses](https://paraibabusiness.com.br/juros-da-divida-publica-chegam-a-r-118-trilhao-em-12-meses-e-pressionam-divida-do-brasil/)
- [SciELO/RBE — Gonçalves, Holland e Spacov (2007)](https://scielo.br/j/rbe/a/BjHQX6LtLSdnGtNJQ5MnJ8b/?lang=en)
- [EconPapers — Tanner e Ramos (2003)](https://econpapers.repec.org/RePEc:taf:applec:v:35:y:2003:i:7:p:859-873)
- [EconPapers — Minella e Souza-Sobrinho (2013)](https://econpapers.repec.org/RePEc:eee:ecmode:v:30:y:2013:i:c:p:405-419)
- Ensaio de Lara Resende (PDF do pacote), págs. 3–4 e 9–11, lido integralmente.
- Os posts de Cochrane (2026) não foram localizados por busca; as afirmações a respeito deles estão marcadas como não verificadas.

---

## Justificativa da recomendação: Major Revision

O núcleo empírico é transparente e relatado com honestidade, e seus resultados majoritariamente nulos não dependem dos defeitos apontados aqui. A exceção é W11, que pode exigir reestimação. Já o Bloco II e a Discussão, que o próprio autor declara serem a base do argumento de política, têm uma contradição teórica (W1), uma aritmética com bases e taxas incompatíveis (W2, W3), uma afirmação sobre *duration* contrária à própria Eq. (13) (W4), fatos fiscais invertidos usados como base de avaliação (W6), uma premissa equivocada na comparação entre Blanchard e Lara Resende (W8) e um desalinhamento entre H1 e a tese neo-fisheriana (W9). Nenhum desses defeitos, isoladamente, invalida o artigo, e todos são corrigíveis com reescrita, cenários de sensibilidade documentados e, se W11 se confirmar, reestimação. Juntos, porém, são substanciais demais para uma revisão menor, e o texto precisa ser revisto de novo após as correções.
