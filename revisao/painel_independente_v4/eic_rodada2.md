# Relatório de Re-revisão (2ª rodada) — Journal-Fit Reviewer (EIC)

- **Manuscrito (novo título)**: "O Patamar dos Juros Altera a Transmissão da Política Monetária? Evidência de Projeções Locais Dependentes de Estado e do Comprometimento de Renda das Famílias no Brasil (2005–2026)"
- **Data**: 9 de novembro de 2026
- **Material lido**: `manuscrito/artigo_svar_lara_resende.tex` (659 linhas, lido por inteiro); PDF compilado (29 p.; conferido que corresponde à fonte); `referencias.bib` (45 entradas, cruzadas com as citações); os seis arquivos de `resultados/`; `data/safra_dados.txt`; Figura 5; o ensaio `ensaio_eu_acuso.pdf`, só para conferir as citações literais. Não houve carta de resposta: cada item foi conferido diretamente no texto.
- `criteria_binding_unavailable`: não há periódico-alvo confirmado. `calibration_status: NOT_CALIBRATED`.
- Régua: a mesma da 1ª rodada. Avalio enquadramento, contribuição, proporção, correspondência entre afirmações e evidência e anonimização. Não reaudito a inferência; só verifico se os números citados batem com `resultados/`.

---

## 1. Resumo da avaliação

A revisão é profunda e, no meu foco, quase completa. Eu disse na 1ª rodada que recomendaria Reject se o enquadramento confirmatório voltasse. Ele não voltou. O título agora é uma pergunta. O resumo (249/228 palavras) abre pelo nulo e o declara **inconclusivo**, com o MDE. As palavras-chave não trazem mais nome de pessoa. "Modelo fechado" virou "arcabouço motivador", que declara não gerar restrição testável (l. 124, 149). A dívida pós-fixada é dita explicitamente "não testada", no resumo, na §2.1 e nas Limitações. A §5.2 virou um parágrafo sobre o que a evidência **não** informa. A nova Tabela 1 (componentes da tese × hipótese × testado/não testado) resolve de forma exemplar o problema de um artigo ancorado num ensaio de blog.

Conferi contra `resultados/` todos os números do resumo, da introdução e da conclusão, e quase todos batem (MDE 0,40–0,42 por DP; β_mod^24 = −0,34 por DP; J^fam = +0,067 por DP; p = 0,057 com a SGS 432; γ̂ com bootstrap p = 0,073; 22 Walds com 2 rejeições; cinco episódios; FEVD; insumos e cenários fiscais). Os problemas novos são menores: (i) duas afirmações de estabilidade e significância que os próprios resultados desmentem em parte (γ̂ na grade de limiares; Holm da taxa implícita); (ii) um resíduo do histórico de versões na §2.2; (iii) anonimização só preparada, não executada; (iv) uma palavra-chave ("dominância fiscal") que promete o que o artigo diz não testar.

A questão editorial que resta é de **suficiência da contribuição**, não de correção. O artigo agora entrega (a) um nulo bem documentado, mas assumidamente sem poder, sobre a dependência de estado; (b) uma decomposição do canal de juros das famílias (taxa efetiva × estoque × amortização); (c) uma aritmética fiscal em termos reais que não é estimada. Para um periódico brasileiro de campo, isso é uma contribuição modesta e legítima, e o enquadramento como "resultado negativo informativo" pode ser mais afiado (EIC2-1). Para um periódico internacional de campo, eu ainda a consideraria limítrofe.

---

## 2. Verificação do roteiro

Legenda: R = resolvido; P = parcialmente resolvido; N = não resolvido; ↓ = piorou. Itens fora do meu foco (R1/R3) recebem verificação breve, só de existência e coerência textual, sem reauditoria técnica.

| ID | Status | Evidência |
|---|---|---|
| REV-01 (título, resumo, palavras-chave) | **R** | Título interrogativo, sem "Dívida Pós-Fixada" (l. 30). A 1ª frase de resultado do resumo é o nulo (l. 46). Palavras-chave PT/EN sem nome próprio (l. 49, 62). Ressalva menor em EIC2-6 |
| REV-02 (contribuição; nulo informativo; LP interagida) | **R** | Parágrafo de contribuições (l. 73). Tabela `tab:nulo` com diferença, IC NW/EWC e MDE em h=3…24, e Painel B interagido com N e 98 regressores (l. 441–466), batendo com `inferencia_regimes.txt` §A–B. "Não encontra apoio" não aparece mais; "inconclusivo" aparece no resumo, em §4.5 e na Conclusão. Ver EIC2-1 sobre o enquadramento |
| REV-03 (canal pós-fixado não testado) | **R** | l. 149 ("**não é testado**"), última frase do resumo, Tabela 1, Limitação 4 (l. 620). A frase "sintetiza a dependência de estado testada" foi removida |
| REV-04 ("fechado"; condensar §2; item 3) | **R** | "fechad" não aparece no .tex. A §2.1 ocupa cerca de 1 página e declara não resolver o equilíbrio nem derivar a dependência de estado (l. 124, 149). O item 3 (r*, π*) foi removido |
| REV-05 (§5.2) | **R** | §5.2 em um parágrafo (l. 612). Sem CFMN nem "expressivamente". Ciclos tratados "apenas como ilustração", com níveis do primário. Δi único (13,94→7,5; 6,4 p.p.) na §2.2, na Tabela 3 e na §5.2. A Conclusão não defende a redução (l. 631) |
| REV-06 (literatura) | **R** (com ressalva) | Nova §1.1 com LPs de estado, TFNP (Sargent–Wallace, Leeper, Woodford, Sims), Brasil (Loyo, Tanner–Ramos, Minella, Céspedes), contra-evidência a ABL (Gonçalves) e famílias (Drehmann–Juselius, Cloyne, Auclert). O ensaio não sustenta mais "fatos estilizados". Falta a literatura empírica de dominância fiscal no Brasil pós-2015 (não obrigatória) |
| REV-07 (anonimização) | **P** | Há uma chave `\anonimotrue` (l. 21–36, 649) que oculta autor, URL e o apêndice de versões. Mas o PDF enviado está compilado com `\anonimofalse` (nome, URL do GitHub com o sobrenome, apêndice "Mudanças em relação às versões anteriores"). No pacote de replicação ficam "VERSÃO 4" (cabeçalhos de `resultados/`), "Número da versão 3" (`aritmetica_fiscal.txt`) e "Base v3" (`estimacao_svar_lara_resende.py`, l. 236). Ver EIC2-5 |
| REV-08 (números da introdução) | **R** | Fiscal Monitor removido. O 5,7% do ensaio é explicado como diferencial antes da divisão por 1+g (l. 158). Tabela de insumos com fonte e data (l. 160–184). As séries citadas estão na Tabela 4 ou na Tabela 2 |
| REV-09 (§5.1) | **R** / P em um subitem | §5.1 renomeada por canais; diz que o ensaio também adota o canal cambial; declara em negrito a não discriminação (l. 586); o h=0 é tratado como diagnóstico (l. 608). A Tabela de câmbio ficou na §5.1 e não foi para a §4 (subitem cosmético) |
| REV-10 (resumo ≤ 250) | **R** | 249 (PT) e 228 (EN) palavras |
| REV-11 (1 DP como unidade principal) | **P** | Resumo, introdução e Conclusão usam DP. Tabela 3 tem coluna por DP. As Tabelas 5–6 e as Figuras 2, 4 e 5 continuam em +1 p.p. (a Tabela 5 traz o fator 0,156 na legenda). Aceitável |
| REV-12 (sensibilidade a p; Holm) | **R** | Painel B da Tabela de robustez (l. 531–536) confere com `inferencia_regimes.txt` §C. "Estável entre especificações" removido. Holm em todos os coeficientes de cabeçalho (l. 305) |
| REV-13 (inferência robusta; episódios; confirmatórios) | **R** (breve) | EWC, sup-t (Fig. 5), bootstrap sob a nula, tabela de episódios e lista C1–C4, com a declaração honesta de que não houve pré-registro (l. 309) |
| REV-14 (primeiro estágio; normalização; placebo) | **R** (breve) | l. 481, que confere com §E. A direção é reportada sem presunção |
| REV-15 (alternativa à Selic média) | **R** (breve) | Espec. 9 (SGS 432); correlação de 0,31 (0,308); "não antecipado" removido do resumo |
| REV-16 (SVAR com sazonais) | **R** (breve) | l. 268–272; Tabela 2 reestimada; o price puzzle é reescrito (pico de +0,21 contra +0,33 sem dummies, batendo com `resultados_svar_summary.txt`) |
| REV-17 (h=0 por construção) | **R** | l. 288; Tabela 3 "(por construção)"; h=0 fora da família Holm |
| REV-18 (grade de limiares; sup-Wald) | **R** | Fig. 6 e l. 472. Ver EIC2-2 sobre a síntese seletiva da grade |
| REV-19 (bootstrap de Kilian) | **R** (breve) | Tabela 2 com intervalos entre chaves; negrito segue o critério bootstrap |
| REV-20 (inconsistências numéricas) | **R** | Cinco episódios listados; pico em h=5 = 0,2117; convenção de horizonte da FEVD na legenda da Fig. 3 |
| REV-21 (aritmética fiscal real) | **R** | Eq. `fiscal_scen` e Tabela 3 com ω ∈ {0; 0,5; 1}, que conferem com `aritmetica_fiscal.txt`. O número de 2,3% não aparece mais no resumo nem na Conclusão. Ver EIC2-4 |
| REV-22 (insumos e bases; grade λ × Δi) | **P** | A tabela de insumos existe; DBGG/DPF e Selic/custo médio estão distinguidos; o corte é gradual. A grade de sensibilidade x × Δi existe em `aritmetica_fiscal.txt`, mas **não** está no manuscrito, e o critério de aceitação pedia a grade no texto |
| REV-23 (4% como limite superior) | **R** | l. 214 ("*limite superior*", com as condições e o ritmo de rolagem) |
| REV-24 ("sem elevar o valor presente") | **R** | A expressão desapareceu; l. 214 reconhece a valorização da parcela prefixada |
| REV-25 (rótulo TFNP) | **R** | l. 144 |
| REV-26 (ciclos) | **R** | Níveis do primário e EC 95 na §5.2; os ciclos são declarados ilustração |
| REV-27 (componentes testados × não testados) | **R** | Tabela 1 (l. 99–120); H1 "não é uma previsão explícita" do ensaio (l. 94). Conferi as citações literais no ensaio ("dissociada da política fiscal…", "inicia imediatamente sua convergência…", "endividamento insustentável das famílias"): conferem |
| REV-28 (γ̂) | **R** | Resumo, §4.4 item 3, Limitação 3 e Conclusão tratam γ̂ como associação compatível com Fisher e com a regra de reação. Não há contagem de votos. Ver EIC2-2 |
| REV-29 (IC-Br) | **R** | SGS 29042 como base; 27574 na espec. 10; FEVD reescrita (l. 360), batendo com o resumo do SVAR |
| REV-30 (Cochrane) | **P** | O texto agora atribui ao ensaio o relato dos posts (l. 69), e a entrada do .bib diz "citados conforme Lara Resende (2026)". O URL continua genérico (`grumpy-economist.com`), não o de cada post |
| REV-31 (bibliografia e questões menores) | **R** | 45 entradas, todas citadas e nenhuma citação órfã; {Lara Resende} tratado; `\date` fixa; IPCA monitorado marcado como "Descritivo (Figura 1)"; o negrito no corpo caiu bastante |
| REV-32, 33, 34, 35, 36 (famílias) | **R** (breve) | l. 229 (construção, NT 55, safra); Tabela `tab:servico` com J, A, S, 29035, E e J/E sob o mesmo choque; "não se detecta transmissão significativa"; l. 223 (η_pos); "Fragilidade" ausente dos scripts |
| REV-23b (cenários de rolagem) | **P** | Há só a caracterização qualitativa (20% vencendo em 12 meses, prazo médio de 4,1 anos); sem simulação com cronograma |
| REV-03b, 14b, 15b (consider) | N (aceitável) | Não feitos; declarados como extensões (l. 617, 631) |
| REV-37, 38 (consider) | **R** | l. 580 (2021–2023, EE 80); Tabela de episódios |

**Síntese:** dos 26 itens `must_fix`, 25 estão resolvidos e um está parcialmente resolvido (REV-07). Entre os `should_fix`, três estão parcialmente resolvidos (REV-11, 22, 30), além de REV-23b. Nenhum item piorou.

---

## 3. Problemas novos

### EIC2-1 — O enquadramento "resultado negativo informativo" ainda é ambíguo sobre o que é informativo
- **Severidade**: maior (de posicionamento, não de correção)
- **Localização**: Introdução, parágrafo de contribuições (l. 73) e de resultados (l. 75); Conclusão (l. 627)
- **Evidência**: a contribuição 1 promete "tornamos o resultado nulo informativo". O que o artigo de fato mostra (§4.5, l. 439) é que o nulo **não** é informativo sobre H1: o MDE (0,42 por DP em h=24) supera o próprio efeito no regime moderado (−0,34 por DP), e a Limitação 2 diz que "nenhuma especificação mensal com essa amostra resolve esse limite". O que é informativo é outra coisa, que o texto não formula como tese: com surpresas mensais e cinco episódios de platô, os dados brasileiros de 2005–2026 **não sustentam afirmações em nenhuma das duas direções** do debate público. Isso vale tanto para quem invoca a perda de potência da Selic quanto para quem invoca a transmissão convencional. A contribuição 3 (aritmética fiscal) é um cálculo, não evidência, e está listada no mesmo plano das demais.
- **Correção sugerida**: reescrever a contribuição 1 como "delimitamos o que esses dados podem identificar": quantificar o poder, mostrar que a resposta depende de p, da medida de juros, do limiar e da especificação interagida, e concluir que nem a tese nem a sua negação têm apoio nessa evidência. Rebaixar a contribuição 3 a "observação analítica" ou integrá-la como corolário. Na Conclusão, uma frase explícita sobre a implicação para o debate (a evidência mensal agregada não arbitra a controvérsia) daria ao leitor o "o que aprendo".

### EIC2-2 — Síntese seletiva da grade de limiares: "γ̂¹² é estável" e omissão do limiar de 14%
- **Severidade**: menor
- **Localização**: §4.6, item 3 (l. 546); §4.5, parágrafo da grade (l. 472); Conclusão (l. 627, "resiste aos controles adicionais")
- **Evidência**: em `inferencia_regimes.txt` §G, γ̂¹² cai para +0,95 (t = 1,97) no limiar de 13%, +0,13 (t = 0,24) em 13,5% e −0,56 em 14%. Logo, não é "estável, exceto quando o regime é definido pelo juro real ex ante". A síntese da grade também omite que no limiar de 14% (31 meses) a diferença é **positiva e significativa** em h=12 (+3,17, p = 0,040) e em h=24 (+4,53, p = 0,001), o que favorece H1. Isso não muda a conclusão, porque o sup-Wald sob a nula não rejeita, mas o leitor merece saber.
- **Correção sugerida**: "γ̂¹² é estável em p e nas especificações do Painel A, mas desaparece para limiares acima de 13% e com o juro real ex ante". Mencionar o limiar de 14% com a ressalva sobre o número de meses.

### EIC2-3 — "p_Holm < 0,001 em todos os horizontes" para a taxa implícita
- **Severidade**: menor
- **Localização**: §4.7, item 1 (l. 575)
- **Evidência**: a Tabela `tab:servico` e `canal_familias.txt` dão p_Holm = 0,002 em h=3 e 0,007 em h=24.
- **Correção sugerida**: "p_Holm ≤ 0,007 em todos os horizontes".

### EIC2-4 — Resíduo do histórico de versões e atribuição incompleta na §2.2
- **Severidade**: menor
- **Localização**: §2.2, parágrafo após a Tabela 3 (l. 214)
- **Evidência**: "e não os 2,3% do PIB que se obtêm aplicando, em termos nominais e de imediato, um corte de 5,5 p.p. à metade da DBGG". Esse número era da versão anterior do próprio manuscrito (`aritmetica_fiscal.txt`: "Número da versão 3"). O ensaio fala em "cerca de 4% do PIB" sobre "80% do PIB". Para um leitor novo, os 2,3% não têm dono. Já os "4% a 5% do PIB após a rolagem" correspondem ao número do ensaio, mas não são atribuídos a ele. Há ainda um ponto final faltando ("DBGG Terceiro").
- **Correção sugerida**: suprimir os 2,3%, ou levá-los ao apêndice de versões. Atribuir explicitamente os "cerca de 4% do PIB" a Lara Resende (2026) e mostrar que eles correspondem à linha "todo o estoque refinanciado, ω = 0". Corrigir a pontuação.

### EIC2-5 — Anonimização preparada, mas não executada no material enviado
- **Severidade**: menor (procedimental, mas bloqueante numa submissão duplo-cega)
- **Localização**: l. 23 (`\anonimofalse`); PDF p. 1 (nome e URL `github.com/bonvenuto/...`); apêndice "Mudanças em relação às versões anteriores" (l. 650–653); pacote de replicação
- **Evidência**: o PDF compilado identifica o autor. Os arquivos de `resultados/` têm cabeçalhos "VERSÃO 4"; `aritmetica_fiscal.txt` traz "Número da versão 3"; `estimacao_svar_lara_resende.py` (l. 236) traz "Base v3". Esses rótulos revelam o histórico editorial mesmo com a chave ligada.
- **Correção sugerida**: compilar com `\anonimotrue` para a submissão e retirar os rótulos de versão do pacote (ou não anexá-lo até a aceitação). O apêndice de mudanças pertence à carta de resposta.

### EIC2-6 — Palavra-chave "dominância fiscal" promete o que o artigo diz não testar
- **Severidade**: menor
- **Localização**: palavras-chave PT/EN (l. 49, 62)
- **Evidência**: o artigo afirma que o canal fiscal "não é testado" (l. 149, resumo, Limitação 4), e nenhuma especificação contém variável fiscal.
- **Correção sugerida**: trocar por "interação monetária-fiscal" ou "regime de juros"; ou mantê-la, mas só se a §1.1 deixar claro que o tema é motivação.

### EIC2-7 — Pequenas imprecisões no resumo
- **Severidade**: menor
- **Localização**: resumo PT/EN (l. 46, 59)
- **Evidência**: (a) "magnitude maior que o próprio efeito estimado no regime moderado" só vale para h=24 (em h=12, β̂_mod é positivo). (b) γ̂ "não significativa sob bootstrap": p = 0,073 sob a nula e t = 1,93 no bootstrap de blocos, ou seja, marginal.
- **Correção sugerida**: "em 24 meses" e "não significativa a 5% sob bootstrap".

### EIC2-8 — Grade de sensibilidade fiscal fora do manuscrito
- **Severidade**: menor
- **Localização**: §2.2; `resultados/aritmetica_fiscal.txt` ("Grade de sensibilidade")
- **Evidência**: a grade x × Δi pedida em REV-22 foi calculada, mas não é apresentada nem citada no texto.
- **Correção sugerida**: incluí-la como painel da Tabela 3 ou em nota.

Não encontrei contradições entre tabelas e `resultados/` além das citadas. Conferi especificamente: Tabelas 2, 3, 4 (estado), 5 (robustez, Painéis A e B), `tab:nulo`, episódios, câmbio por regime, famílias e insumos/cenários fiscais.

---

## 4. Pontos fortes

1. **Reposicionamento completo e honesto.** Título, resumo e conclusão agora dizem o que os dados dizem. O resumo termina com "O canal da dívida pública pós-fixada não é testado". Isso raramente se vê.
2. **Tabela 1 (componentes × testado/não testado).** É a melhor solução possível para um artigo motivado por um ensaio de opinião: separa com precisão o que é testado, o que é tratado só aritmeticamente e o que fica fora. As citações literais do ensaio conferem com o original.
3. **Nulo quantificado.** Diferença, IC, MDE, LP interagida, sup-Wald sob a nula com reestimação do choque e do estado, tabela de episódios e testes confirmatórios declarados, com admissão de que não houve pré-registro. O leitor vê o que foi descartado e o que não foi.
4. **Aritmética fiscal em termos reais.** A Tabela 3 mostra, com insumos documentados, que o alívio fiscal depende do repasse do corte à inflação. É uma tensão interna da proposta, e o artigo a expõe sem tomar partido.
5. **Proporção.** O bloco teórico foi reduzido ao papel que tem; a §5.2 virou um parágrafo; as Limitações são específicas.
6. **Bibliografia e reprodutibilidade.** Todas as entradas são citadas, a safra é documentada, há ordem de execução dos scripts e as sementes estão fixadas.

---

## 5. Recomendação

**Minor Revision** — confiança **4**.

**Justificativa.** Os itens bloqueantes do meu assento (B1: enquadramento e alegações de política) estão resolvidos. Os itens de inferência e de dados (B2, B3), verificados no nível de existência e coerência, foram atendidos, e os números do resumo e da conclusão conferem com `resultados/`. Os oito problemas novos são de texto ou de procedimento e não exigem reestimação. O único que pesa na avaliação editorial é EIC2-1, que é de posicionamento: o artigo ganharia muito se dissesse com clareza que sua contribuição é delimitar o que a evidência mensal agregada pode arbitrar no debate. Antes de submeter, é obrigatório executar a anonimização (EIC2-5).

**Adequação.** Em português, com o escopo atual e uma contribuição empírica modesta mas limpa, o manuscrito é adequado a periódicos nacionais de campo (Economia Aplicada, Estudos Econômicos, RBE). Para um periódico internacional de campo, a contribuição, um nulo sem poder mais um canal das famílias quase mecânico, seria limítrofe sem identificação de alta frequência ou sem variáveis fiscais como estado, e o texto teria de ser vertido para o inglês.

**O que reduz a confiança.** Não reauditei a inferência (EWC, bootstrap sob a nula, sup-t), que é o foco de R1.
