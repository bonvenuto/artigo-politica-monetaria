# Resposta ao roteiro de revisão (versão 4)

**Enquadramento escolhido pelo autor (REV-01):** opção (a), resultado negativo informativo. O artigo passa a perguntar se a transmissão monetária depende do patamar dos juros. Ele apresenta o nulo de H1 como inconclusivo, com poder e intervalos, e trata o canal das famílias e a aritmética fiscal como contribuições delimitadas.

Legenda: **feito**; **parcial** (com justificativa); **não feito** (com justificativa).

## Obrigatórios (`must_fix`)

| ID | Status | O que mudou | Onde |
|---|---|---|---|
| REV-01 | feito | O título pergunta, sem citar dívida pós-fixada. O resumo começa pela pergunta, e o primeiro resultado é o nulo de H1. As palavras-chave não trazem nome de pessoa. | título, resumos |
| REV-02 | feito | Parágrafo de contribuições na introdução. Tabela 8 com a diferença entre regimes, IC 95% (NW e EWC) e MDE por 1 p.p. e por 1 DP. LP totalmente interagida com N e número de regressores (Wald p = 0,001 em h = 24), discutida. "Não encontra apoio" foi trocado por "inconclusivo". | §1, §4.5, Tabela 8 |
| REV-03 | feito | Declaração explícita de que λ, a composição da dívida e o prêmio soberano não entram em nenhuma especificação; o canal "não é testado". A frase "sintetiza a dependência de estado testada" foi removida. | resumo, §1, Tabela 1, §2.1, §5.3 |
| REV-04 | feito | "Fechado" foi retirado. A §2 virou arcabouço motivador. θ*, os três regimes e o item 3 (r*, π*) foram removidos. O texto declara que a dependência de estado é suposta, não derivada. | §2.1 |
| REV-05 | feito | A §5.2 virou um parágrafo sobre o que a evidência não informa. CFMN, cláusulas de escape e efeitos distributivos foram retirados. "Expressivamente" foi retirado. Corte único em todo o texto: 13,94% → 7,5%. | §2.2, §5.2, Conclusão |
| REV-07 | parcial | Chave `\anonimotrue` oculta autor e URL e suprime o Apêndice B. Menções a versões anteriores saíram do texto principal. O nome continua na versão padrão, por decisão do autor sobre a filiação. | preâmbulo, Apêndice B |
| REV-08 | feito | Tabela 2 com fonte, data e conceito de cada insumo fiscal. Fiscal Monitor removido. Os 5,7% do ensaio foram reconciliados com os 5,05% da Eq. (5); a variação observada da DBGG (+5,6 p.p.) é informada. | §2.2, Tabela 2 |
| REV-09 | feito | §5.1 reescrita. O texto reconhece que o ensaio adota o canal cambial e lista os critérios que separariam as teorias. Frase explícita: "o desenho deste artigo não discrimina entre essas teorias". A tabela do câmbio permaneceu na §5.1, e não na §4. | §5.1 |
| REV-12 | feito | Sensibilidade a p ∈ {2, 4, 6, 9, 12} no Painel B da Tabela 10. Implicação (i) classificada como "sugestiva, mas não robusta". "Estável entre especificações" removido. Holm na mesma família, aplicado a todos os coeficientes de cabeçalho. LP com defasagens aumentadas citada como alternativa não implementada. | §4.4, §4.5, Tabela 10 |
| REV-13 | feito | p-valores EWC nas Tabelas 6 e 7. Banda sup-t na Figura 5. Bootstrap recursivo que reestima VAR, choque e estado, sob a nula linear. Tabela 9 de episódios com N por regime. Lista de testes confirmatórios, declarados sem pré-registro. | §3.4, §4.4, §4.5 |
| REV-14 | feito | Primeiro estágio da Selic por regime. Razões inflação/Selic acumuladas, com IC bootstrap, reportadas sem presumir direção. Placebo em h = 0 tratado como diagnóstico. | §4.5, §5.1 |
| REV-15 | feito | Especificação com a meta Selic de fim de mês (SGS 432): correlação de 0,31 com o choque-base, e β_mod^24 deixa de ser significativo. "Não antecipado" saiu do resumo. Reportados o F clássico (p = 0,55) e o Wald HAC (p < 0,001). | §3.2, Tabela 10, espec. 9 |
| REV-16 | feito | O SVAR-base tem dummies sazonais. Tabela 5 e Figuras 2–3 refeitas, Portmanteau reportado. O price puzzle em h = 5 cai de +0,33 para +0,21, mas persiste. | §3.2, §4.1, §4.2 |
| REV-20 | feito | +0,357 eliminado. "Quatro ciclos" virou cinco episódios, listados. Convenção da FEVD declarada na legenda da Figura 3. | §4.2, Tabela 9 |
| REV-21 | feito | Bloco fiscal em termos reais (Eq. 6), com cenários ω = 0; 0,5; 1. Os 2,3% saíram do resumo e da conclusão. | §2.2, Tabela 3 |
| REV-22 | feito | Tabela de insumos. Fluxo de juros pelas NFSP, estoque pela DBGG. Selic e custo médio distinguidos. Corte gradual em 12 meses. Grade x × Δi em `resultados/aritmetica_fiscal.txt`. | §2.2 |
| REV-23 | feito | 4–5% do PIB apresentado como limite superior condicional (prêmio a termo nulo, rolagem integral), com o ritmo de rolagem do RMD. | §2.2 |
| REV-24 | feito | "Sem elevar o valor presente" foi substituído: o corte valoriza a parcela prefixada e indexada, cerca de metade da DPF. | §2.2 |
| REV-26 | feito | Níveis do primário nos dois ciclos (SGS 5793) e menção à EC 95. A comparação passou a ser ilustração, não evidência. | §5.2 |
| REV-27 | feito | Tabela 1 cruza cada componente da tese com a obra e diz se é testado. O canal de custos não é mais atribuído ao ensaio (conferido no PDF: não aparece). O componente neo-fisheriano é declarado não testado. | §1.2, Tabela 1 |
| REV-28 | feito | γ̂ apresentado como associação compatível com Fisher e com a regra de reação. Sem contagem de votos. A especificação 5 (juro real *ex ante*) é destacada como a mais próxima da tese. "Mais estável" removido. | §1.2, §4.4, §4.6, Conclusão |
| REV-29 | feito | SGS 29042 (US$) virou a base; a 27574 (R$) ficou como especificação 10. Rótulos corrigidos na Tabela 4, na Figura 1 e nos scripts. FEVD reinterpretada. | todo o artigo |
| REV-32 | feito | Construção das séries 29033–29038 documentada (NT 55, Denton-Cholette, média móvel trimestral, retropolação, substituição de 2021). Safra informada. Robustez a MA(2): NW h+3, EWC, amostra trimestral e corte em 2023. A resposta em h = 0 é discutida. | §3.1, §4.7 |
| REV-33 | feito | Mesmo choque para J, A, S, S sem habitacional, E e 100 ln(J/E) (Tabela 11). H2 com estoque defasado como controle. | §4.7 |
| REV-34 | feito | Mesmo choque-base no serviço total. O teste J − S equivale à resposta de −A (identidade verificada nos dados). "Não se detecta transmissão significativa", com discussão dos mecanismos. | §4.7, §5.3 |

## Recomendados (`should_fix`)

| ID | Status | Observação |
|---|---|---|
| REV-06 | feito | Literatura reorganizada por questão: Ramey–Zubairy, Sargent–Wallace, Leeper, Woodford, Tanner–Ramos, Minella, Gonçalves–Holland–Spacov, Cloyne et al., Auclert. Os blogs não sustentam afirmações factuais. Ayres et al. não foi incluído (referência não verificada). |
| REV-10 | feito | Resumos com 248 (PT) e 245 (EN) palavras. |
| REV-11 | parcial | Efeitos por 1 DP no resumo, no texto e na conclusão, e coluna por DP na Tabela 6. As Tabelas 7 e 10 seguem em p.p., com fator de conversão na legenda. |
| REV-17 | feito | Igualdade em h = 0 declarada como resultado de construção. Holm sem h = 0. "Forte aderência" foi trocada pela descrição das divergências. |
| REV-18 | parcial | Grade de limiares (Figura 6) e sup-Wald por bootstrap feitos. Não foi feito um indicador de estado independente da Selic. |
| REV-19 | feito | Bootstrap de Kilian com B1 = 300 e B2 = 600. Negrito da Tabela 5 segue o intervalo bootstrap. |
| REV-23b | parcial | Ritmo de rolagem (20% em 12 meses; prazo médio de 4,1 anos) informado. Sem simulação com o cronograma de vencimentos. |
| REV-25 | feito | O canal das expectativas virou "solvência fiscal e prêmio de risco", com nota de que não é a equação de valoração da TFNP. |
| REV-30 | parcial | Cochrane (2026) é citado só pelo que o ensaio relata dos posts. URLs individuais dos posts não obtidas. |
| REV-31 | feito | Entradas sem citação removidas (Serrano, Pastore, Minsky, Limites do Possível). `resende1980causas` corrigida para Lopes e Lara Resende (1979), TD PUC-Rio 6. Blanchard e Favero–Giavazzi nas versões publicadas (2005). Sobrenome {Lara Resende}. `\date` fixa. Uribe e García-Schmidt–Woodford reescritos. O IPCA monitorado ficou como "descritivo (Figura 1)". |
| REV-35 | feito | η_pos corrigido: estoque × concessões, tetos regulatórios e TR. Série 29035 incluída. |
| REV-36 | feito | Subtítulo da Figura 1(b) e da Figura 2(b) sem "Fragilidade". |

## A considerar (`consider`)

| ID | Status | Observação |
|---|---|---|
| REV-03b | não feito | Exige séries de composição da dívida ou de CDS/EMBI; registrado nas limitações. |
| REV-14b | não feito | Identificação dependente de estado (VAR de limiar); registrado nas limitações. |
| REV-15b | não feito | HFI/LP-IV exige dados de futuros de DI; registrado nas limitações. |
| REV-37 | feito | Episódio 2021–2023 e Estudo Especial 80 citados. |
| REV-38 | feito | Tabela 9 com os cinco episódios. |
| REV-39 | parcial | Uma frase: efeitos distributivos e salvaguardas não são estudados. |

## Resultados que mudaram com a reestimação

- **SVAR:** com sazonais e IC-Br em US$, a queda da inflação em 12 meses deixou de ser significativa. Em 18 e 24 meses ela é significativa só pelos erros assintóticos; os intervalos bootstrap incluem zero.
- **LP de estado:** β_mod^24 passou de −1,98 para −2,20 (Holm p = 0,073). Ele não é robusto a p nem à meta Selic. γ̂^12 ficou praticamente igual (+1,61), mas tem p = 0,073 no bootstrap sob a nula.
- **Famílias:** J^fam em 12 meses passou de +0,459 para +0,431 por 1 p.p. (+0,067 por 1 DP).
- **Fiscal:** o "alívio de 2,3% do PIB" virou −1,1 a −1,3 p.p. com inflação rígida e +1,3 a +1,5 p.p. com Fisher pleno, no primeiro ano.
