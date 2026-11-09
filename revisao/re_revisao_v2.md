# Re-revisão (2ª rodada) — Verificação da Versão Revisada

**Manuscrito (v2):** *Patamar de Juros, Dívida Pós-Fixada e Fragilidade Financeira das Famílias: Formalização Analítica e Evidência de Projeções Locais Dependentes de Estado para o Brasil (2005–2026)* — 24 páginas
**Base de comparação:** versão de 18 páginas revisada na 1ª rodada ([revisao_por_pares.md](revisao_por_pares.md))
**Data:** 09/11/2026 · **Modo:** `re-review` · **Status de calibração:** `NOT_CALIBRATED`

> **Proveniência e limites.**
> - A verificação foi feita por um único modelo (Claude Opus 5.5), no mesmo contexto da 1ª rodada, contra o texto da v2. Os "assentos" do painel não são independentes.
> - Não recebi carta de resposta aos revisores: cada item foi verificado diretamente no manuscrito.
> - O protocolo formal de re-revisão em três etapas, com verificadores automáticos, não foi executado.
> - Verifiquei na API do BCB os códigos SGS 11428, 29033, 3696 e 433, e consultei o link do repositório de replicação.

---

## Decisão: Revisão Maior (mais leve que a anterior)

A v2 é uma revisão séria e, em boa parte, bem-sucedida. **Dos 8 itens obrigatórios, 5 foram resolvidos e 3 foram parcialmente resolvidos.** Entre os resolvidos:
- código SGS corrigido;
- choque normalizado;
- modelo fechado;
- FEVD reinterpretada;
- literatura e episódios históricos incluídos.

Além disso, as novas tabelas permitem verificar as afirmações do artigo — e é justamente essa transparência que revela o problema que sobra:

**O resumo e a conclusão continuam afirmando mais do que as Tabelas 4 e 5 da própria v2 sustentam.** Três exemplos:
- O teste de Wald nunca rejeita β_alto = β_mod.
- Choques de aperto, isolados, nunca são significativos no platô.
- O efeito de β_alto desaparece com dummies sazonais e de COVID.
- O resumo diz que γ^h é robusto ao regime por juro real *ex ante*, mas não é, de h = 6 a h = 18.

Corrigir isso exige uma reestimação simples (sazonalidade na especificação-base) e a reescrita do resumo, da seção 4.5, da seção 5.1 e da conclusão. Mas a reescrita muda a mensagem principal do artigo; por isso a decisão continua sendo Revisão Maior, e não Menor. **Se os itens abaixo forem tratados, a próxima rodada tem boa chance de ser Revisão Menor ou Aceite.**

---

## Matriz de rastreabilidade — itens obrigatórios da 1ª rodada

| Item | Pedido | Status | Evidência na v2 |
|---|---|---|---|
| R1 | Estimar efeitos assimétricos (alta × corte) no platô | **Parcial** | Feito: β⁺_alto e β⁻_alto separados, com teste de simetria (Tab. 4, Fig. 5b). A simetria não é mais imposta. **Mas a interpretação extrapola:** ver N1 e N4. |
| R2 | Reportar γ^h; testar β_alto = β_mod; robustez de limiar e endogeneidade | **Parcial** | Feito: γ^h reportado, Wald reportado, Tab. 5 com 6 especificações (Focus, IPCA cheio, juro real *ex ante*, limiares de 10% e 12%, dummies). **Mas os resultados desses testes não chegaram ao resumo nem à conclusão:** ver N1, N2 e N3. |
| R3 | Formalização fechada; corrigir π* = i* − g e o limiar "2g" | **Resolvido** | IS com renda financeira (Eq. 2), expectativas fiscais (Eq. 5), paridade com risco (Eq. 6) e derivada total (Eq. 7) com condições explícitas de sinal. π* = i* − r* com r* = g + ρ(b*), agora coerente com os dados (π* ≈ 4,5–5%). A condição correta ī > g_nom aparece na Eq. (4). Restam questões menores (ver N8). |
| R4 | Reinterpretar a FEVD e o *price puzzle*; câmbio e expectativas no VAR | **Resolvido** | PTAX incluída no VAR; especificação com Focus reduz o *puzzle* à metade (§4.2); §4.3 cita corretamente McLeay & Tenreyro; "choques próprios" no lugar de "inércia". |
| R5 | Corrigir o código SGS da inflação livre | **Resolvido** | SGS 11428 em todo o texto. Conferi na API: 11428, 29033 (juros; ≈ 9,5% em 2025), 3696 (PTAX ≈ 5,8) e 433 (IPCA cheio) batem com as descrições. |
| R6 | Definir e normalizar o choque das LPs | **Resolvido** | Eq. (12): Shock = P₅₅·e, com P₅₅ = 0,1731; SVAR e LP em +1 p.p.; a Fig. 4(d) confirma o impacto unitário nas duas. |
| R7 | Alinhar o resumo e a conclusão à significância | **Parcial** | Melhorou muito ("associam-se", p-valores explícitos, "não é estatisticamente diferente de zero"). **Mas sobram afirmações contraditas pelas tabelas:** ver N1, N2 e N3. Não há correção para múltiplos horizontes (a limitação 2 menciona o tamanho amostral, não a multiplicidade). |
| R8 | Literatura antecedente e contrária; ciclos 2011–13 e 2016–18 | **Resolvido** | §1.1 cobre Loyo, Blanchard, Favero & Giavazzi, Arida et al., Uribe, García-Schmidt & Woodford, Sims, Nakamura & Steinsson e McLeay & Tenreyro, e discute os dois ciclos de corte. §5.1 confronta a tese com Blanchard. |

### Itens sugeridos da 1ª rodada

| Item | Status | Nota |
|---|---|---|
| S1 VAR em níveis (SSW 1990); método das bandas | Resolvido | §4.1 cita SSW; bandas assintóticas declaradas; AIC/FPE/BIC/HQ reportados |
| S2 Sazonalidade, COVID, estabilidade | **Parcial** | Dummies só como robustez (Tab. 5, espec. 6), e ali β_alto perde significância — ver N2. Sem teste de quebra estrutural. |
| S3 Conta do alívio fiscal | Resolvido | 2,27% do PIB imediato; 4,0–4,5% após rolagem |
| S4 Precisão fiscal | Resolvido | DBGG × DLSP; 5,3%/5,7% como taxa relativa e +4,4 p.p. do PIB |
| S5 S_t: juros × amortização | **Parcial** | Passou a usar J^fam (SGS 29033), com Eq. (9) explicitando taxa fixa × pós-fixada. **Mas os resultados com o serviço total (29034), listado como "Robustez" na Tab. 1, não são reportados** — ver N6. |
| S6 Pico de S_t | Resolvido | Pico em h = 12 coerente com a Tab. 2 |
| S7 CFMN: viabilidade legal e contingências | Resolvido | §5.2: LC 179/2021, CMN, cláusulas de escape, efeitos distributivos |
| S8 Fontes primárias em vez de Substack | **Parcial** | Ver N7 |
| S9 Conferência bibliográfica | Resolvido em grande parte | Cochrane (2011) → JPE 119(3) e Céspedes et al. → RBE 62(2) corrigidos. Resta Resende (2017) — ver N7. |
| S10 Limitações e dados/código | **Parcial** | §5.3 criada. **O repositório citado retorna 404** — ver N5. |
| S11 Forma | Resolvido em grande parte | Novo título, filiação e siglas definidas |

---

## Problemas novos ou remanescentes

### N1 — A hipótese H₁ é apresentada como confirmada, mas os testes da v2 não a confirmam
**Severidade: Maior (bloqueante)** · Fontes: R1, DA

O que as Tabelas 4 e 5 mostram:
- **O Wald de β_alto = β_mod nunca rejeita** (p entre 0,124 e 0,759 em todos os horizontes; Tab. 4). O texto reconhece isso em §4.5 (item 1), mas o resumo, a conclusão (item 2: "Assimetria de Regime na Eficácia Desinflacionária") e a §5.1 tratam a diferença entre regimes como estabelecida.
- **Choques de aperto, isolados, nunca são significativos no platô.** β⁺_alto tem p ≥ 0,68 em todos os horizontes, com estimativas pontuais negativas em h = 0, 9, 12, 18 e 24 (Tab. 4). O β_alto positivo é identificado sobretudo pelas surpresas negativas, como a própria §4.5 (item 3) admite. Mesmo assim, o resumo diz que **"choques de aperto associam-se a acréscimos na inflação acumulada"**, e a H₁ diz que "choques adicionais [de aperto]… associam-se a pressões positivas sobre os preços".
- **O Wald de simetria β⁺ = β⁻ também nunca rejeita** (p entre 0,24 e 0,80). Portanto, não há evidência de que altas e cortes tenham efeitos diferentes no platô.

**Âncora:** `table: Tabela 4 — colunas "Wald" (p ≥ 0,124), "Alta no Platô β⁺" (p ≥ 0,678), "Wald Simetria" (p ≥ 0,243)`

**Requisito:** reescrever o resumo (b), a H₁, a §5.1 e a conclusão (item 2) de modo fiel aos testes. Uma formulação defensável seria: "no regime moderado, o aperto reduz a inflação acumulada em 24 meses; no platô, não se detecta efeito desinflacionário, e as estimativas de curto prazo são positivas, mas a diferença entre regimes e entre altas e cortes não é estatisticamente significativa".

### N2 — O β_alto positivo não sobrevive às dummies sazonais e de COVID
**Severidade: Maior (bloqueante)** · Fonte: R1

Na especificação 6 da Tab. 5, β_alto perde significância em todos os horizontes (h = 3: p = 0,331; h = 6: p = 0,353). A inflação de itens livres (11428) é mensal e **não dessazonalizada**. Logo, a especificação com dummies sazonais deveria ser a **base**, não um teste de robustez. O texto da §4.6 resume os testes dizendo que "confirmam" os resultados e omite que a espec. 6 anula β_alto (γ^h sobrevive).

**Âncora:** `table: Tabela 5, espec. 6 — β_alto: +0,337 (0,331); +0,487 (0,353)`

**Requisito:**
- Adotar dummies sazonais na especificação principal (ou usar a série dessazonalizada).
- Separar o efeito das dummies sazonais e da dummy de COVID, para saber qual delas elimina o resultado.
- Reapresentar as Tab. 4 e 5 a partir dessa base.
- Se β_alto deixar de ser significativo, o achado principal passa a ser γ^h, e o texto deve dizer isso.

### N3 — O resumo afirma uma robustez de γ^h que a Tab. 5 não mostra
**Severidade: Maior** · Fontes: R1, EIC

O resumo diz que γ^h "permanec[e] robusto ao controle por expectativas Focus 12 meses e ao juro real *ex ante*". Mas, na espec. 3 (regime por juro real *ex ante*), γ^h só é significativo em h = 3 (p = 0,035). Em h = 6, 9, 12 e 24, os p-valores são 0,105; 0,133; 0,123; 0,560. A §4.6 diz "praticamente todas as especificações", o que é aceitável, mas o resumo cita justamente a exceção como confirmação.

**Âncora:** `table: Tabela 5, espec. 3 — γ^h (p): 0,105; 0,133; 0,123; 0,560`

**Requisito:** corrigir o resumo; mencionar a espec. 3 como a exceção na §4.6.

### N4 — Os "cortes não antecipados de −1 p.p." são resíduos negativos, não cortes
**Severidade: Maior** · Fontes: DA, R1

Shock⁻ = min(Shock, 0) inclui **qualquer** resíduo negativo da equação da Selic: N₊ + N₋ = 63 + 59 = 122, ou seja, praticamente todos os meses do platô. Isso abrange meses em que o Copom **subiu** a Selic menos do que a regra previa. Além disso, um resíduo típico tem desvio-padrão de 0,17 p.p. (P₅₅), de modo que "−1 p.p." é uma extrapolação de cerca de 6 desvios-padrão. Mesmo assim, a conclusão (item 3) diz que "cortes não antecipados da Selic a partir do platô alto associaram-se historicamente a recuos na inflação". A evidência para isso é um único horizonte significativo a 5% (h = 6, p = 0,027), com simetria não rejeitada. E o último parágrafo extrapola para "a redução gradual e coordenada da Selic… sem comprometer o controle inflacionário", que é uma mudança de regime de cerca de 6,5 p.p. — o próprio artigo reconhece, na §5.2, a crítica de Lucas a esse tipo de extrapolação.

**Âncora:** `text: §6 item 3 "cortes não antecipados da Selic a partir do platô alto associaram-se historicamente a recuos na inflação acumulada"`

**Requisito:**
- Chamar β⁻ de "surpresas negativas da Selic", não de "cortes".
- Reportar quantos desses meses tiveram, de fato, variação negativa da Selic.
- Interpretar os coeficientes para um choque de 1 desvio-padrão (≈ 0,17 p.p.), além do normalizado.
- Na conclusão, separar o que foi estimado (surpresas marginais) da proposta de política (mudança de regime), em vez de apresentar a segunda como consequência da primeira.

### N5 — Repositório de replicação inacessível
**Severidade: Maior para fins de submissão** · Fontes: EIC, R1

O artigo afirma que dados, scripts e logs estão "integralmente disponíveis no repositório público" `https://github.com/bonvenuto/artigo-politica-monetaria`. Em 09/11/2026, esse endereço retornou **HTTP 404**: ou o repositório é privado, ou ainda não existe, ou o endereço está errado.

**Âncora:** `text: §5.3 item 3; nota de rodapé da p. 1`

**Requisito:** tornar o repositório público antes de submeter, ou ajustar a declaração.

### N6 — A troca da variável de fragilidade não é acompanhada dos resultados da variável original
**Severidade: Maior** · Fontes: R3, DA

A v1 usava o serviço total da dívida (29034). A v2 passou ao comprometimento só com juros (29033). A troca é metodologicamente justificada — foi pedida na 1ª rodada. Mas a Tab. 1 lista 29034 como "Robustez", e esses resultados não aparecem em nenhuma tabela. Como a variável original tinha resultados fracos, um revisor vai querer ver ambas lado a lado, para afastar a suspeita de busca pela especificação favorável.

Há também uma questão de interpretação: a H₂, do jeito que está formulada ("elevações da Selic produzem aumento na parcela da renda comprometida com juros"), é quase mecânica. A ligação com "fragilidade financeira minskyana" exigiria indicadores de inadimplência, uso de rotativo ou renegociação.

**Âncora:** `dataset: Tabela 1 — S_t^fam, SGS 29034, papel "Robustez (juros + amort.)"; sem resultados correspondentes nas Tab. 2–5`

**Requisito:** reportar as IRFs e LPs com 29034 (em apêndice basta); moderar o rótulo "fragilidade" ou acrescentar um indicador de inadimplência (por exemplo, inadimplência das famílias no SGS).

### N7 — Descrição das fontes não arbitradas
**Severidade: Menor** · Fontes: R2, EIC

Na v1, Resende (2026) e Cochrane (2026) eram identificados como posts de Substack, com URL. Na v2, aparecem como "Ensaio Técnico" e "Hoover Institution Essay", sem URL. Se o veículo mudou, ótimo. Se não, a referência deve descrever o veículo real e trazer URL e data de acesso: rotular um post de blog como ensaio técnico ou institucional seria visto como problema por um editor.

Resende (2017), "Debate Macroeconômico Brasileiro (Ensaios em Consenso e Contrassenso)", não corresponde a nenhuma obra que eu conheça. O livro de Lara Resende de 2017 que conheço é *Juros, moeda e ortodoxia* (Portfolio-Penguin). Confira a referência.

### N8 — Questões menores de formalização e apresentação
**Severidade: Menor** · Fontes: R2, R1
- **Choque de notação:** θ é ao mesmo tempo o parâmetro de Calvo (em φ = (1−θ)(1−βθ)/θ·…) e a sensibilidade fiscal das expectativas (Eq. 5). β é ao mesmo tempo o peso da Curva de Phillips híbrida (Eq. 1) e o fator de desconto em φ.
- **Eq. (7):** é uma derivada parcial de impacto que trata E_t[y_{t+1}] como dado; não é a solução de equilíbrio do sistema. Vale dizer isso. Uma calibração ilustrativa de θ, ρ′ e κ mostrando de que lado da condição o Brasil estaria fortaleceria muito a §2.
- **§5.1, item 1:** controlar pelas defasagens da PTAX **não** elimina o canal cambial pós-choque — o câmbio continua livre para responder ao choque ao longo do horizonte. Para discriminar Blanchard de Lara Resende, estime a resposta da PTAX (e, se possível, do CDS/EMBI) **por regime**, com a mesma LP dependente de estado.
- **Fig. 5:** usa IC de 90%, enquanto o texto julga significância a 5%. Uniformize, ou declare explicitamente.
- **§1, item 2:** cita McLeay & Tenreyro como se apoiassem a Curva de Phillips achatada. A §4.3 os cita corretamente (o achatamento da forma reduzida não implica κ = 0); alinhe a §1 a ela.
- **Filiação:** abaixo do nome aparece "Grupo de Pesquisa em Macroeconomia Aplicada…", e no rodapé, "Pesquisador Independente". Uniformize.
- **Autoavaliação:** expressões como "leitura rigorosa e matizada" (§4.5) e "devidamente calibradas" (§6) devem ser deixadas para o leitor julgar.

---

## O que melhorou de forma inequívoca (para registrar)

- **Título e registro:** neutros, centrados no problema e não no autor. Hipóteses H₁ e H₂ explícitas e falseáveis.
- **Literatura (§1.1):** o artigo agora dialoga com os antecedentes e com os críticos, e a §5.1 coloca Lara Resende e Blanchard lado a lado.
- **Normalização e comparação SVAR × LP:** agora corretas e verificáveis.
- **Bateria de robustez (Tab. 5):** completa — exatamente o que um revisor de método pede. O problema não é a bateria, e sim como seus resultados são resumidos.
- **Achados mais sólidos da v2:**
  1. o aperto é desinflacionário no regime moderado (−1,92 p.p. em 24 meses, p = 0,009; robusto nas espec. 1, 3, 4 e 5);
  2. γ^h é positivo em h = 9–12 em 5 de 6 especificações;
  3. o comprometimento de renda com juros responde à Selic no SVAR e nas LPs.

  Esses três achados, apresentados com honestidade, sustentam um artigo publicável.
- **§5.2:** a proposta de política agora traz salvaguardas, cláusulas de escape e efeitos distributivos.

---

## Roteiro da 3ª versão (ordem de origem, não ordem de trabalho)

- [ ] N1 — `must_fix`: reescrever resumo (b), H₁, §5.1 e conclusão (item 2) de acordo com os testes de Wald e com β⁺/β⁻
- [ ] N2 — `must_fix`: especificação-base com dummies sazonais; separar sazonalidade e COVID; reapresentar Tab. 4 e 5
- [ ] N3 — `must_fix`: corrigir a afirmação de robustez de γ^h ao juro real *ex ante* no resumo
- [ ] N4 — `must_fix`: renomear "cortes" para "surpresas negativas"; contar os cortes efetivos; separar a evidência marginal da proposta de política na conclusão
- [ ] N5 — `must_fix`: tornar o repositório acessível
- [ ] N6 — `should_fix`: reportar os resultados com 29034; moderar "fragilidade" ou acrescentar inadimplência
- [ ] N7 — `should_fix`: descrever corretamente os veículos de Resende (2026), Cochrane (2026) e Resende (2017)
- [ ] N8 — `consider`: notação θ/β; natureza da Eq. (7); calibração ilustrativa; PTAX por regime; IC de 90% × 5%; §1 item 2; filiação
- [ ] R7 (remanescente) — `should_fix`: inferência com múltiplos horizontes (bandas simultâneas ou correção)
