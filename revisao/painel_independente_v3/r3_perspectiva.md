# Relatório de Revisão por Pares — Revisor 3 (Perspectiva: finanças das famílias e crédito)

## Informações do Manuscrito
- **Título**: Patamar de Juros, Dívida Pós-Fixada e Comprometimento de Renda das Famílias: Formalização Analítica e Evidência de Projeções Locais Dependentes de Estado para o Brasil (2005–2026)
- **ID do manuscrito**: não informado
- **Data da revisão**: 2026-11-09
- **Rodada**: 1ª rodada deste painel simulado

---

## Informações do Revisor

### Papel do revisor
Revisor 3 (Perspectiva)

### Identidade do revisor
Economista de finanças das famílias e mercado de crédito, com experiência nos indicadores de comprometimento de renda do BCB (*debt service ratios* no sentido de Drehmann et al.) e na heterogeneidade do crédito às famílias (consignado, rotativo, imobiliário).

### Foco da revisão
(1) Como as séries SGS 29033/29034 são construídas e se comportam inferência mensal; (2) se H2 vai além do mecanismo contábil da equação de $J^{fam}$, e por que o efeito some no serviço total; (3) as afirmações distributivas da Seção 5.2 (poupadores, fundos DI, previdência).

**Ponto cego declarado**: não avalio a identificação macroeconômica (Cholesky, efeito-informação, LPs dependentes de estado sobre a inflação) nem o bloco da TFNP. Não me pronuncio sobre H1/H1'.

### Vínculo com critérios do periódico
`criteria_binding_unavailable`. Nenhum periódico-alvo foi confirmado. Este relatório não avalia a adequação do manuscrito a um periódico.

### Status de calibração
`NOT_CALIBRATED`

---

## Avaliação Geral

### Recomendação
- [ ] Accept
- [ ] Minor Revision
- [x] **Major Revision**
- [ ] Reject

### Grau de confiança
4. As séries de comprometimento e a transmissão ao crédito das famílias estão no centro da minha área. A identificação do choque está fora dela.

A confiança só delimita incerteza e escopo. Ela não altera severidades nem a recomendação.

### Avaliação resumida
O artigo testa três hipóteses inspiradas em Lara Resende. A que me cabe, H2, afirma que um choque positivo na Selic eleva o comprometimento da renda das famílias com juros (SGS 29033). Com SVAR e LP, o efeito estimado é de +0,46 p.p. da renda em 12 meses por choque de 1 p.p. ($p_{Holm}=0,006$). O efeito não aparece de forma significativa no serviço total da dívida (SGS 29034).

Do meu ângulo, o resultado empírico parece robusto. Minhas checagens exploratórias com os dados do pacote mostram que ele resiste a controlar pelo estoque de dívida/renda (29037) e ao período da pandemia. O artigo também tem o mérito de reconhecer que o sinal é "quase mecânico" e de recusar a leitura de fragilidade financeira.

O problema é o que falta entre o número e a interpretação. O artigo não documenta como o BCB constrói as séries: média móvel trimestral, renda mensalizada por Denton-Cholette, retropolação. Também não decompõe a resposta entre taxa e estoque, embora 29036 (amortização) e 29037 (endividamento) estejam disponíveis. A explicação de por que o efeito some no serviço total não é testada. Na Seção 5.2, o artigo afirma um alívio "expressivo" para os endividados e perdas para poupadores, fundos DI e previdência sem nenhuma evidência.

Nada disso invalida H2, mas tudo exige reanálise ou reescrita substantiva. Por isso recomendo Major Revision.

---

## Pontos Fortes

### S1: Escopo de H2 delimitado com honestidade
O artigo admite que o sinal da resposta decorre quase da própria definição de $J^{fam}$. Ele situa o conteúdo empírico na magnitude, na persistência e na transmissão ao serviço total, e recusa explicitamente a leitura de fragilidade financeira (H2 na Seção 1; Limitação 5). Isso é raro em trabalhos que usam esse indicador e protege o artigo da leitura mais comum e mais errada.
**Evidence Anchor**: `text: §1, H2 "Dada a Equação (\ref{eq:household_interest}), o sinal dessa resposta é quase mecânico"`

### S2: Uso da série só de juros, com o serviço total reportado
O artigo troca o serviço total (29034) pela série só de juros (29033), que é a mais diretamente ligada à Selic. Mesmo assim, reporta o serviço total no Apêndice A, com SVAR, LP, p-valores de Holm e FEVD. Assim o leitor vê que o resultado não se estende ao serviço total, em vez de receber só a especificação favorável.
**Evidence Anchor**: `table: Tabela A (tab:servico) — 29034 sem significância no SVAR; LP h=18 p=0,026, p_Holm=0,184`

### S3: Dados oficiais replicáveis e resultado de H2 robusto
Conferi os valores de 29033, 29034 e 29037 entre set. e dez. de 2025 contra a API do SGS, e eles coincidem com `data/base_macro_bcb.csv`. Fiz checagens exploratórias com o mesmo choque da especificação-base. Elas não constam do manuscrito e os autores devem reproduzi-las.

| Variação da especificação-base | Resposta de 29033 em h=12 |
|---|---|
| Base (manuscrito) | +0,459 (p=0,001) |
| Com 6 defasagens de 29037 como controle | +0,456 (p=0,004) |
| Com dummy de COVID (2020:03–2021:06) | +0,492 (p=0,002) |
| Amostra restrita a $t \le$ 2019:12 | +0,751 (p=0,002) |

O sinal e a significância de H2 não dependem desses fatores.
**Evidence Anchor**: `dataset: data/base_macro_bcb.csv — coluna juros_divida (SGS 29033), valores idênticos à API SGS em 2025:09–2025:12`

### S4: Separação entre estimativas e proposta de política na conclusão
A conclusão afirma explicitamente que as estimativas se referem a surpresas marginais e não informam sobre uma redução coordenada e permanente da Selic. É a postura correta; a Seção 5.2 só precisa segui-la (ver W5).
**Evidence Anchor**: `text: §6 "Essas conclusões devem ser separadas da proposta de política discutida na Seção 5.2."`

---

## Pontos Fracos

### W1: As séries 29033/29034 não são documentadas, e sua construção limita a inferência mensal
**Problem**: A Tabela 1 descreve 29033 só como "Comprometimento de renda familiar com juros c/ ajuste", e o texto justifica o início da amostra pela "disponibilidade das séries". Pela nota de imprensa do BCB de 28/12/2021 (item 5 da Nota de Crédito de novembro de 2021) e pela Nota Técnica 55, as séries são diferentes do que essa descrição sugere:
- **Numerador**: é o "valor médio estimado para o pagamento do serviço das dívidas". É uma estimativa do BCB, não o pagamento observado.
- **Denominador**: é a média móvel trimestral da RNDBF restrita.
- **RNDBF restrita**: é mensalizada por Denton-Cholette a partir das Contas Econômicas Integradas anuais, que o IBGE publica só no segundo semestre de t+2. Antes de 2012, a parte de rendimentos do trabalho é retropolada com a PME. A própria NT 55 avisa que a estimativa está "sujeita a revisões significativas".
- **Origem**: as séries 29033–29038 substituíram as antigas 19879–19882 (denominador MSAD) em dezembro de 2021. Os valores de 2005 a 2021 são, portanto, uma reconstrução retroativa.
- **Ajuste sazonal**: as séries vêm dessazonalizadas pelo BCB, com método não informado no artigo.

Não consegui confirmar nas fontes públicas como o BCB estima a parcela de juros e a de amortização (taxa do estoque ou das concessões, prazo remanescente, fórmula de anuidade). **A verificar** pelos autores junto ao DSTAT/BCB.

**Evidence Anchor**: `text: §3.1, Tabela 1 "Comprometimento de renda familiar com juros c/ ajuste"`

**Why it matters**:
- **Correlação mecânica**: uma média móvel de 3 meses introduz correlação serial MA(2) por construção. A variação mensal da série carrega menos informação independente do que 258 observações sugerem, e os p-valores HAC com janela $h+1$ podem estar subestimados nos horizontes curtos.
- **Impacto em $h=0$**: a resposta contemporânea ao choque mistura meses anteriores ao choque, o que torna pouco interpretável a ordenação de $J^{fam}$ por último no Cholesky.
- **Revisões**: os dados de 2024–2026 serão revisados quando sair a RNDBF anual. Os resultados dependem da safra de dados, e a safra usada não é informada.
- **Base da equação do Bloco III**: se o numerador for construído como taxa média × saldo, a Equação (household_interest) descreve quase a fórmula do BCB, e não um comportamento.

**Suggestion**:
1. Descrever a construção das séries no texto ou em apêndice, citando a NT 55 e a nota de 28/12/2021.
2. Informar a data de extração dos dados (safra).
3. Reestimar H2 em frequência trimestral, com observações não sobrepostas (por exemplo, o último mês de cada trimestre), ou usar erros-padrão que tratem explicitamente a estrutura MA(2).
4. Discutir a resposta em $h=0$ à luz da média móvel.
5. Se possível, obter do BCB a descrição de como juros e amortização são estimados e reportá-la.

**Severity**: Major
**Confidence**: 4 — área central: metodologia dos indicadores de comprometimento do BCB (cálculo exato do numerador não confirmado)

### W2: H2 não é separada da identidade contábil; falta decompor a resposta em taxa e estoque
**Problem**: A Equação (household_interest) escreve $J^{fam}=\bar i^{fam}D^{fam}_{t-1}/Y^{fam}_t$, e o texto atribui a resposta a três vias: o repreço das linhas pós-fixadas, as novas concessões e a queda da renda no denominador. Nenhuma das três é medida. A base contém `endividamento` (SGS 29037, $D/Y$), e o BCB publica a amortização (29036), mas nenhuma das duas entra na análise.

Fiz uma checagem exploratória com o mesmo choque e as mesmas defasagens da LP-base:

| Variável de resposta | h=12 | h=18 | h=24 |
|---|---|---|---|
| $100\ln(J/E)$ (taxa efetiva implícita) | +8,1 (p<0,001) | +10,2 (p<0,001) | — |
| $100\ln E$ (dívida/renda) | — | −3,1 (p=0,025) | −2,9 (p=0,014) |

A resposta de $J$ vem, portanto, inteiramente do preço (a taxa efetiva sobe), parcialmente compensada por desalavancagem (o estoque cai). Nos níveis, a correlação de 29033 com a Selic é de só 0,09, contra 0,85 com 29037. A taxa implícita $J/E$ caiu de cerca de 29,5% em 2005 para 16,7% em 2021, o que sugere uma mudança de composição da carteira (consignado, imobiliário) que o modelo ignora.

**Evidence Anchor**: `equation: Eq. (household_interest) — termo \bar{i}_t^{fam} D_{t-1}^{fam}/Y_t^{fam}, cujos componentes não são estimados separadamente`

**Why it matters**: O artigo afirma que o conteúdo de H2 está na "magnitude, persistência e transmissão". Sem a decomposição, o leitor não sabe se está diante de repasse de taxa, de mudança de composição ou de efeito-denominador, e são esses os elementos que dariam conteúdo econômico a H2. A queda do endividamento é por si um resultado relevante sobre o canal de crédito, e hoje está ausente.

**Suggestion**:
1. Estimar, com o mesmo choque, LPs para $J$, $A$ (29036), $S$ (29034), $E$ (29037) e $J/E$ (ou $\ln J = \ln(J/E) + \ln E$), apresentadas em uma única tabela.
2. Reportar H2 com controle pelo estoque (defasagens de 29037).
3. Se viável, acrescentar a resposta das concessões e das taxas médias de crédito às pessoas físicas. As séries existem no SGS; os códigos ficam **a verificar**.

**Severity**: Major
**Confidence**: 4 — área central: decomposição de *debt service ratios*

### W3: A explicação de por que o efeito some no serviço total não é testada, e "não se transmite" diz mais do que os dados mostram
**Problem**: O texto atribui o desaparecimento do efeito no serviço total à "variabilidade das amortizações" e conclui que o efeito "não se transmite" a 29034. Há três problemas.

(a) **"Não se transmite" contra "não se detecta"**: as estimativas pontuais para 29034 têm o mesmo sinal e magnitude parecida (+0,33 contra +0,46 em h=12), com erros-padrão cerca de 2,5 vezes maiores. Os dados mostram ausência de evidência, não evidência de ausência.

(b) **Mecanismos alternativos não discutidos**:
- *Composição da anuidade*: em contratos tipo Price, uma taxa maior desloca a parcela de amortização para juros. O serviço total sobe menos que o componente de juros (Drehmann et al., 2015, usam exatamente essa fórmula).
- *Alongamento de prazos e portabilidade/refinanciamento*: comuns no consignado e no imobiliário, reduzem a amortização mensal.
- *Desalavancagem e queda das concessões*: na minha checagem, o estoque $E$ cai em 18–24 meses.

(c) **Choques diferentes**: o script `robustez_servico_divida.py` reestima o VAR substituindo 29033 por 29034. Os resultados de juros e de serviço total vêm, portanto, de choques diferentes. Com o mesmo choque-base, obtive para 29034 respostas parecidas (h=18: +0,81, p=0,035) e, para $A=S-J$, estimativas pequenas e não significativas.

**Evidence Anchor**: `text: §4.2, item 2 "o efeito da Selic se concentra no componente de juros e é diluído, no serviço total, pela variabilidade das amortizações"`

**Why it matters**: Na literatura de DSR (Drehmann e Juselius), o que tem relevância macroeconômica (consumo, restrição de caixa, risco) é o serviço total, porque é ele que sai do orçamento da família. Se só o componente de juros responde, o canal de caixa para o consumo não está estabelecido. É exatamente isso que separa um resultado contábil de um resultado com conteúdo econômico.

**Suggestion**:
1. Usar o mesmo choque para todas as variáveis de comprometimento.
2. Estimar diretamente a resposta da amortização (29036).
3. Testar a diferença entre as respostas de $J$ e $S$.
4. Trocar "não se transmite" por "não se detecta transmissão significativa", no resumo, na Seção 4.2, na Limitação 5 e na conclusão.
5. Discutir os três mecanismos alternativos.

**Severity**: Major
**Confidence**: 4 — área central: mecânica de juros e amortização em DSR

### W4: A taxa pós-fixada das famílias é descrita de forma imprecisa e não há desagregação por modalidade
**Problem**: O texto afirma que a fração $\eta_{pos}$ ("rotativo do cartão de crédito, cheque especial e novas concessões") "reage positivamente às elevações da Selic". Isso tem três problemas.

- **Linhas tabeladas**: o rotativo e o cheque especial têm taxas dominadas pelo spread e, em boa parte da amostra, sujeitas a tetos regulatórios. Que eu saiba, o cheque especial tem teto de 8% a.m. desde 2020 (Res. CMN 4.765/2019), e os juros e encargos do rotativo foram limitados a 100% do principal pela Lei 14.690/2023. Esses detalhes ficam **a confirmar** pelos autores. O repasse da Selic a essas linhas é fraco e muda ao longo da amostra.
- **Estoque contra fluxo**: "novas concessões" não são uma fração do estoque com taxa flutuante. O texto mistura repreço do estoque com fluxo novo.
- **Imobiliário**: o crédito imobiliário indexado à TR tem exposição indireta à Selic, porque a TR é positiva quando a Selic está alta (**a verificar**). Classificá-lo como prefixado é impreciso.

O artigo não usa nenhuma série por modalidade, nem a série sem habitacional (29035).

**Evidence Anchor**: `text: §2, Bloco III "rotativo do cartão de crédito, cheque especial e novas concessões) reage positivamente às elevações da Selic"`

**Why it matters**: A heterogeneidade por modalidade decide quem paga o aperto: o tomador de consignado com taxa fixa, o de rotativo com taxa tabelada ou o de capital de giro de pessoa física. Também decide o quão rápido um corte se repassa. Sem ela, o Bloco III fica como uma racionalização plausível, mas não testada.

**Suggestion**:
1. Corrigir a descrição de $\eta_{pos}$ (estoque contra concessões; tetos regulatórios; TR).
2. Reestimar H2 com 29035 (sem habitacional).
3. Como extensão desejável, estimar as respostas das taxas médias e dos saldos por modalidade (consignado, pessoal não consignado, veículos, cartão, cheque especial, imobiliário).

**Severity**: Minor. O resultado central de H2 sobrevive; o que fica comprometido é a descrição do mecanismo.
**Confidence**: 3 — área central: crédito por modalidade; detalhes normativos a confirmar

### W5: As afirmações distributivas da Seção 5.2 não têm evidência e contrariam o próprio escopo do artigo
**Problem**: O item 3 da Seção 5.2 afirma que um corte da Selic "alivie expressivamente o comprometimento de renda das famílias endividadas" e que haveria perdas para fundos de pensão, previdência complementar e "poupadores de classe média via fundos DI". Nenhuma das duas afirmações é sustentada.

(a) **O alívio "expressivo"**:
- As estimativas se referem a surpresas de cerca de 0,16 p.p. A própria Seção 5.2 diz que elas não permitem inferir o efeito de uma mudança de 6,5 p.p.
- A simetria entre aperto e corte foi testada só para a inflação, não para $J^{fam}$.
- O estoque prefixado (consignado, veículos) só se reprecifica com amortização, refinanciamento ou novas concessões, o que gera defasagem e possível assimetria. Um dado descritivo ilustra o ponto: entre fev. e ago. de 2026, a Selic recua de 14,90 para 13,94, e 29033 sobe de 10,58 para 10,92.

(b) **Os perdedores**:
- Não há dados sobre quem detém as LFTs, direta ou indiretamente.
- A poupança tem remuneração regrada (Lei 12.703/2012) e não acompanha a Selic acima de 8,5% a.a. Os "poupadores de classe média" não são, em geral, os detentores de LFT.
- O denominador de 29033 (RNDBF restrita) exclui por construção as rendas de propriedade, inclusive os juros recebidos. O indicador mede um lado só, a carga bruta dos devedores. Ele não informa sobre a redistribuição líquida entre devedores e credores.
- Pela Tabela 1 da NT 55, os juros líquidos recebidos pelas famílias somavam 1,7% da RNDBF em 2019 no conceito das Contas Nacionais. A ordem de grandeza agregada é bem diferente da que o texto sugere.

**Evidence Anchor**: `text: §5.2, item 3 "alivie expressivamente o comprometimento de renda das famílias endividadas"`

**Why it matters**: Este é o único ponto do artigo que liga H2 a bem-estar e a política. Do jeito que está escrito, ele usa como evidência uma estimativa que o próprio artigo declara inaplicável à proposta. Também omite as partes interessadas do lado do ativo sem quantificá-las. Um leitor de política (Tesouro, BCB, reguladores de previdência) sairia com uma impressão de alívio e de custo distributivo que o artigo não mede.

**Suggestion**: O remédio mínimo, e barato, é retirar "expressivamente". Nesse caso, o item deve dizer que a evidência de H2 se refere a apertos marginais e não quantifica o alívio de um corte de regime. Também deve marcar como hipótese não testada a afirmação sobre poupadores e fundos.

O remédio mais forte, e custoso, é trazer evidência:
- composição dos detentores da DPMFi por tipo (Relatório Mensal da Dívida do Tesouro);
- estoque do Tesouro Direto e dados de fundos DI e de previdência (Anbima/Previc);
- juros pagos e recebidos pelas famílias nas Contas Econômicas Integradas;
- uma LP assimétrica de $J^{fam}$ para surpresas negativas.

O artigo poderia ainda citar a literatura sobre o canal de redistribuição (Auclert, 2019).

**Severity**: Major. A correção mínima é simples, mas o texto atual faz uma afirmação de política e de distribuição sem apoio, e ela precisa ser removida ou documentada antes da aceitação.
**Confidence**: 4 — área central: distribuição de ativos e passivos financeiros das famílias

### W6: O título do painel da Figura 2 contradiz a ressalva do texto
**Problem**: O painel (b) da Figura 2 tem o subtítulo "[Canal de Fragilidade Financeira das Famílias]". Isso contradiz H2 e a Limitação 5, que recusam explicitamente essa leitura. O mesmo rótulo aparece no script `estimacao_svar_lara_resende.py`.
**Evidence Anchor**: `figure: Figura 2, painel (b) — subtítulo "Canal de Fragilidade Financeira das Famílias"`
**Why it matters**: As figuras circulam separadas do texto. Esse rótulo induz justamente a interpretação que o artigo descarta.
**Suggestion**: Trocar por "Comprometimento de renda com juros (SGS 29033)", sem qualificativo.
**Severity**: Minor
**Confidence**: 5 — verificação direta da figura

### W7: Magnitude econômica e agregação pouco traduzidas
**Problem**: Para a inflação, o artigo reporta o efeito de um choque de 1 desvio-padrão, mas não para $J^{fam}$. Como o próprio artigo mostra, o choque de +1 p.p. dispara uma trajetória da Selic com pico de cerca de +3,1 p.p. Em termos de choque observável, o efeito é de cerca de 0,46 × 0,16 ≈ 0,07 p.p. da renda em 12 meses por desvio-padrão, ou de cerca de 0,15 p.p. da renda por p.p. de aperto acumulado no pico.

Além disso, o indicador é uma média agregada que inclui as famílias sem dívida. O BCB identificou cerca de 4,6 milhões de "endividados de risco" em dezembro de 2019, 5,4% dos tomadores no SCR (Estudo Especial 80/2020). A carga se concentra nesse grupo, e a média agregada a dilui.
**Evidence Anchor**: `table: Tabela 3 (tab:lp_svar_comp) — LP h=12 +0,4594 sem conversão para choque de 1 d.p. ou por p.p. acumulado`
**Why it matters**: Sem essa tradução, "+0,46 p.p." parece maior do que é. E o agregado não informa sobre os tomadores mais expostos.
**Suggestion**:
1. Reportar o efeito por desvio-padrão e por p.p. acumulado de Selic.
2. Comparar com o episódio de 2021–2023, em que 29033 subiu cerca de 2,4 p.p. com uma Selic de 2% para 13,75%.
3. Mencionar que análises com microdados do SCR por faixa de renda são o passo natural.

**Severity**: Minor
**Confidence**: 4 — área central

---

## Comentários Detalhados

### Auditoria de pressupostos
- **Explícitos**: H2 pressupõe que a "parcela da renda comprometida com juros" é uma medida de pressão financeira. O artigo relativiza isso corretamente (S1), mas a Figura 2 e a Seção 5.2 voltam a pressupô-lo (W5, W6).
- **Implícitos**:
  - O artigo trata 29033 como se fosse observada mensalmente, quando é estimada, suavizada e retropolada (W1).
  - Supõe que o repasse da Selic às famílias opera pelas linhas rotativas, quando são justamente as linhas com tetos e spreads dominantes (W4).
  - Supõe que o efeito de um corte é o espelho do efeito de um aperto (W5).
- **Paradigmáticos**: o modelo agregado de agente representativo esconde que a mesma variação da Selic é custo para um devedor e renda para um credor. O indicador escolhido, com a renda restrita sem rendas de propriedade no denominador, só enxerga o primeiro lado.

### Conexões com a literatura de finanças das famílias
- **Pesquisa paralela**: a literatura de transmissão monetária via balanço das famílias usa variação na exposição a taxas flutuantes para identificar o canal de caixa: Cloyne, Ferreira e Surico (2020); Di Maggio et al. (2017); Flodén et al. (2021). Ela oferece desenhos que o Brasil comporta, como a variação regional ou por modalidade da exposição pós-fixada.
- **Empréstimo conceitual**: Drehmann, Juselius e Korinek, sobre a dinâmica de novos empréstimos e serviço da dívida, explicam por que o serviço total reage com defasagem e com sinal ambíguo. Isso é diretamente útil para W3.
- **Empréstimo metodológico**: decomposição contábil de $\Delta J$ em taxa, estoque e renda (W2); LPs assimétricas também para $J^{fam}$ (W5).

### Impacto prático
- **Aplicação**: a decomposição de W2 seria útil ao próprio BCB e à política de crédito, por exemplo na avaliação dos tetos do rotativo e do consignado.
- **Viabilidade**: todas as séries que sugiro (29035, 29036, 29037, taxas e saldos por modalidade) são públicas no SGS.
- **Partes interessadas**: os devedores de baixa renda, os mais expostos, não aparecem no agregado. Do lado do ativo, poupadores, cotistas de fundos DI e participantes de previdência são citados, mas não medidos.

### Implicações mais amplas
- **Social e distributiva**: a redistribuição entre devedores e credores é o argumento distributivo central de qualquer proposta de corte de juros. O artigo hoje a afirma sem medi-la (W5).
- **Direções futuras**: microdados do SCR por renda e modalidade; um painel por UF da exposição pós-fixada; integração com as Contas Econômicas Integradas para o lado do ativo.

---

## Recomendações de Leitura
- Drehmann, M., & Juselius, M. (2012). *Do debt service costs affect macroeconomic and financial stability?* BIS Quarterly Review, set. 2012. Mostra por que o serviço total da dívida, e não só os juros, é o indicador com relevância macroeconômica.
- Drehmann, M., Juselius, M., & Korinek, A. (2018). *Going with the flows: New borrowing, debt service and the transmission of credit booms.* NBER Working Paper 24549. Trata da defasagem entre crédito novo e serviço da dívida, relevante para W3.
- Cloyne, J., Ferreira, C., & Surico, P. (2020). *Monetary policy when households have debt: new evidence on the transmission mechanism.* Review of Economic Studies, 87(1). Traz heterogeneidade por posição no balanço.
- Di Maggio, M., Kermani, A., Keys, B., Piskorski, T., Ramcharan, R., Seru, A., & Yao, V. (2017). *Interest rate pass-through: Mortgage rates, household consumption, and voluntary deleveraging.* American Economic Review, 107(11). Analisa repasse a contratos flutuantes e desalavancagem.
- Flodén, M., Kilström, M., Sigurdsson, J., & Vestman, R. (2021). *Household debt and monetary policy: Revealing the cash-flow channel.* Economic Journal, 131. Isola o canal de caixa.
- Auclert, A. (2019). *Monetary policy and the redistribution channel.* American Economic Review, 109(6). É o arcabouço para a afirmação distributiva da Seção 5.2.
- Coibion, O., Gorodnichenko, Y., Kueng, L., & Silvia, J. (2017). *Innocent bystanders? Monetary policy and inequality.* Journal of Monetary Economics, 88. Trata dos efeitos distributivos da política monetária.
- Banco Central do Brasil (2021). *Nota Técnica nº 55 — Estimativa mensal da Renda Nacional Disponível Bruta das Famílias.* É a metodologia do denominador (W1). Verificada: https://www.bcb.gov.br/content/publicacoes/notastecnicas/NT_55_202112.pdf
- Banco Central do Brasil (2020). *Estudo Especial nº 80 — Indicadores de endividamento de risco e perfil do tomador de crédito.* Traz a heterogeneidade do comprometimento entre tomadores (W7). Verificado: https://www.bcb.gov.br/conteudo/relatorioinflacao/EstudosEspeciais/EE080_Indicadores_de_endividamento_de_risco_e_perfil_do_tomador_de_credito.pdf
- Banco Central do Brasil (2021). Nota para a Imprensa de 28/12/2021, "Aprimoramentos nas estatísticas de comprometimento e endividamento" (Estatísticas Monetárias e de Crédito, nov. 2021, item 5). Apresenta as séries 29033–29038 e a correspondência com as antigas 19879–19882.

~~~yaml suggested-references
- title: "Do debt service costs affect macroeconomic and financial stability?"
  authors: ["Drehmann, M.", "Juselius, M."]
  year: "2012"
  doi: null
  arxiv_id: null
- title: "Going with the flows: New borrowing, debt service and the transmission of credit booms"
  authors: ["Drehmann, M.", "Juselius, M.", "Korinek, A."]
  year: "2018"
  doi: null
  arxiv_id: null
- title: "Monetary policy when households have debt: new evidence on the transmission mechanism"
  authors: ["Cloyne, J.", "Ferreira, C.", "Surico, P."]
  year: "2020"
  doi: null
  arxiv_id: null
- title: "Interest rate pass-through: Mortgage rates, household consumption, and voluntary deleveraging"
  authors: ["Di Maggio, M.", "Kermani, A.", "Keys, B.", "Piskorski, T.", "Ramcharan, R.", "Seru, A.", "Yao, V."]
  year: "2017"
  doi: null
  arxiv_id: null
- title: "Household debt and monetary policy: Revealing the cash-flow channel"
  authors: ["Flodén, M.", "Kilström, M.", "Sigurdsson, J.", "Vestman, R."]
  year: "2021"
  doi: null
  arxiv_id: null
- title: "Monetary policy and the redistribution channel"
  authors: ["Auclert, A."]
  year: "2019"
  doi: null
  arxiv_id: null
- title: "Innocent bystanders? Monetary policy and inequality"
  authors: ["Coibion, O.", "Gorodnichenko, Y.", "Kueng, L.", "Silvia, J."]
  year: "2017"
  doi: null
  arxiv_id: null
- title: "Estimativa mensal da Renda Nacional Disponível Bruta das Famílias (Nota Técnica nº 55)"
  authors: ["Banco Central do Brasil"]
  year: "2021"
  doi: null
  arxiv_id: null
- title: "Indicadores de endividamento de risco e perfil do tomador de crédito (Estudo Especial nº 80)"
  authors: ["Banco Central do Brasil"]
  year: "2020"
  doi: null
  arxiv_id: null
~~~

---

## Perguntas aos Autores
1. Qual é a safra (data de extração) de 29033/29034/29037? Os resultados de H2 mudam se os anos com RNDBF ainda não ancorada nas Contas Nacionais (2024–2026) forem excluídos?
2. Com o mesmo choque, como se decompõe a resposta de $J^{fam}$ entre taxa efetiva e estoque/renda, e qual é a resposta da amortização (29036)?
3. Os autores têm do BCB a descrição de como o numerador (juros e amortização esperados) é estimado? Ele usa as taxas do estoque ou das concessões?
4. Que evidência sustenta a afirmação de que fundos DI, previdência e "poupadores de classe média" são os principais detentores indiretos de LFTs, e de que um corte "aliviaria expressivamente" os endividados?

---

## Questões Menores
- Tabela 1: usar os nomes oficiais. 29033 é "Comprometimento de renda das famílias com juros da dívida com o Sistema Financeiro Nacional – Com ajuste sazonal (RNDBF)", e 29034 é o mesmo para o serviço da dívida. Indicar "média móvel trimestral".
- O resumo, a Seção 4.2, a Limitação 5 e a conclusão devem dizer "não se detecta transmissão significativa", e não "não se transmite" (ver W3).
- Bloco III: a citação de Drehmann et al. (2015) sugere uma equivalência com a metodologia do BIS que não foi verificada. Convém dizer que a série é do BCB, não da base do BIS.
- A ligação com Minsky em H2 pode ser retirada, já que o artigo não a testa.

---

## Julgamentos por Critério

Status de calibração: `NOT_CALIBRATED`. Fonte dos critérios: dimensões do template de revisão aplicadas ao cartão de configuração do R3. O arquivo `quality_rubrics.md` não foi carregado. Não há periódico-alvo vinculado (`criteria_binding_unavailable`).

| Dimensão | Fonte do critério | Julgamento | Âncoras | Justificativa | Incerteza / escopo | Pesa na decisão? |
|---|---|---|---|---|---|---|
| Originalidade | template + cartão R3 | PARTLY_MEETS | `text: §1, H2` | Usar 29033 em vez do serviço total é útil; H2 em si é próximo de uma identidade | Avalio só H2 | não — não limita a decisão |
| Rigor metodológico | template + cartão R3 | PARTLY_MEETS | W1, W3 | Construção das séries não tratada; comparação J/S com choques distintos | Identificação do choque fora do meu escopo | sim — W1 e W3 exigem reanálise |
| Suficiência da evidência | template + cartão R3 | PARTLY_MEETS | W2, S3 | H2 robusto, mas sem decomposição nem amortização | Checagens próprias exploratórias | sim — W2 |
| Coerência argumentativa | template + cartão R3 | PARTLY_MEETS | W5, W6 | Ressalvas corretas no texto, contrariadas pela Seção 5.2 e pela Figura 2 | — | sim — W5 |
| Qualidade da redação | template | MEETS | §1–§6 | Clara e com ressalvas explícitas | Avaliação limitada às seções de H2 | não |
| Integração da literatura | template + cartão R3 | PARTLY_MEETS | Recomendações de leitura | Falta a literatura de finanças das famílias e do canal de redistribuição | Cobertura sistemática é do R2 | não |
| Significância e impacto | template + cartão R3 | PARTLY_MEETS | W5, W7 | Pode ser relevante para política se a decomposição e a distribuição forem tratadas | — | não isoladamente |

**Justificativa da recomendação (Major Revision)**: O resultado empírico de H2 se sustenta. Ficam em aberto quatro pontos que pesam na decisão, todos reparáveis: a documentação e o tratamento inferencial de séries suavizadas e estimadas (W1); a decomposição que daria conteúdo econômico a H2 além da identidade (W2); o tratamento correto da não detecção no serviço total (W3); e a retirada ou documentação das afirmações distributivas (W5). Nenhum deles invalida o artigo, mas juntos exigem reanálise e reescrita além de uma revisão menor. Não avalio H1, H1' nem a TFNP.

---

### Fontes consultadas (metodologia BCB)
- [Nota Técnica nº 55 (BCB, dez. 2021)](https://www.bcb.gov.br/content/publicacoes/notastecnicas/NT_55_202112.pdf)
- [Estatísticas Monetárias e de Crédito, nov. 2021, item 5 — nota de 28/12/2021 (cópia em poder360)](https://static.poder360.com.br/2021/12/BC_notadecredito_novembro2021.pdf)
- [Dados abertos BCB — série 29033](https://dadosabertos.bcb.gov.br/dataset/29033-comprometimento-de-renda-das-familias-com-juros-da-divida-com-o-sistema-financeiro-nacional--)
- [Estudo Especial nº 80/2020 (BCB)](https://www.bcb.gov.br/conteudo/relatorioinflacao/EstudosEspeciais/EE080_Indicadores_de_endividamento_de_risco_e_perfil_do_tomador_de_credito.pdf)
- API SGS (`api.bcb.gov.br/dados/serie/bcdata.sgs.{29033,29034,29035,29037}`), consultada em 2026-11-09.
