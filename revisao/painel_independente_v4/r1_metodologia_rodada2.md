# Relatório de Re-revisão: Metodologia (Revisor 1), 2ª rodada

- **Manuscrito**: "O Patamar dos Juros Altera a Transmissão da Política Monetária? Evidência de Projeções Locais Dependentes de Estado e do Comprometimento de Renda das Famílias no Brasil (2005–2026)"
- **Rodada**: 2ª (re-revisão). Não há carta de resposta: tudo foi conferido diretamente no `.tex`, nos scripts e nas saídas.
- **Data**: 2026-11-09
- **Régua**: a mesma da 1ª rodada (`rodada1/r1_metodologia.md`, W1–W12).
- **Status de calibração**: `NOT_CALIBRATED`; `criteria_binding_unavailable`.
- **Ponto cego declarado**: não avalio a plausibilidade institucional do Bloco fiscal nem a proposta de política.

---

## Resumo

A revisão é substantiva e, do ponto de vista metodológico, quase todos os itens do roteiro foram atendidos com reanálise real, não só com reescrita:
- o SVAR passou a ter dummies sazonais e IC-Br em US$ na base;
- há tabela da diferença entre regimes com IC (NW e EWC) e MDE;
- a LP totalmente interagida é reportada;
- há sensibilidade a p, primeiro estágio por regime, normalização e episódios;
- foram implementados EWC, bootstrap de blocos com banda sup-t, bootstrap recursivo sob a nula de linearidade (reestimando VAR, choque e estado), grade de limiares com sup-Wald e bootstrap de Kilian;
- a meta Selic (SGS 432) entra como robustez.

Reproduzi **byte a byte** todos os seis arquivos de `resultados/`, inclusive os dois bootstraps, a partir dos CSVs do pacote, sem rede.

A conclusão central ("H1 inconclusiva") é, a meu ver, a leitura correta. Mas o texto a justifica de modo incompleto. O bootstrap sob a nula que o artigo usa para relativizar os testes **não é aplicado à LP totalmente interagida**, justamente a única especificação que rejeita com folga (p=0,001). Fiz essa calibração (R1b-1). Restam ainda:
- uma afirmação incorreta sobre o alcance da reestimação com a meta Selic ("reestimamos tudo", que só vale para as LPs de estado);
- uma descrição seletiva da grade de limiares;
- algumas lacunas menores de inferência e de replicabilidade.

Nenhum desses pontos é crítico, e todos se corrigem com reestimação barata ou ajuste de texto.

**Recomendação: Minor Revision. Confiança: 4.**

---

## Verificação do roteiro (itens metodológicos e de inferência)

| ID | Status | Evidência |
|---|---|---|
| REV-02 (IC/MDE da diferença; "inconclusivo"; LP interagida) | **Parcial (quase resolvido)** | A Tabela `tab:nulo` traz a diferença, o IC 95% NW e EWC e o MDE por p.p. e por DP, h=3…24. Confere com `inferencia_regimes.txt` §A e com minha reimplementação independente do EWC (`r1b_checks2_output.txt`). "Não encontra apoio" não aparece mais no texto (0 ocorrências), e "inconclusivo" está no resumo, na §4.5 e na Conclusão. O Painel B traz a LP interagida com N e 98 regressores. **Falta**: (i) banda simultânea para a *diferença*, pois a sup-t da Fig. 5 é para β_alto e β_mod em nível; (ii) calibrar a LP interagida pelo mesmo bootstrap sob a nula (ver R1b-1). |
| REV-11 (1 DP como unidade) | **Resolvido (parcial nas Tabelas 4–6)** | O resumo e a Conclusão usam 1 DP, e a Tabela 3 tem coluna por DP. As Tabelas 4–6 seguem em +1 p.p., com fator de conversão na legenda. Aceitável. |
| REV-12 (sensibilidade a p; Holm consistente; rebaixar (i)) | **Resolvido** | O Painel B da Tabela `tab:robustez` reproduz minha checagem da 1ª rodada (β_mod^24 só significativo com p=6 e p=9). "Estável entre especificações" foi removido. Holm vale na família h=3…24 para todos os coeficientes de cabeçalho. Recalculei o Holm de β_mod^24: 0,0122×6 = 0,073. A LP com defasagens aumentadas não foi implementada, o que o texto declara. Rodei uma versão (7 defasagens, EP EHW): β_mod^24 = −1,97, p=0,087. Isso **reforça** a leitura "sugestiva, não robusta". |
| REV-13 (EWC/fixed-b; sup-t; bootstrap com reestimação; episódios; confirmatórios) | **Parcial (menor)** | EWC nas Tabelas 3 e 4 e na `tab:nulo`. Banda sup-t na Fig. 5. Bootstrap recursivo com reestimação do VAR, do choque e do estado. Tabela de episódios. Lista C1–C4 de testes confirmatórios, declarada *post hoc*, o que o texto reconhece. **Falta**: EWC na Tabela 5, que o critério de aceitação pedia ("Tabelas 4 e 5"); N por regime e horizonte só em `resultados/`, não no manuscrito. |
| REV-14 (primeiro estágio; normalização; placebo como diagnóstico) | **Resolvido** | §4.5, "Primeiro estágio e normalização". Os números conferem com §E (Selic h=24: +1,39 contra −1,40, p=0,018; razões e IC conferem). O placebo de h=0 é tratado como diagnóstico, também no texto da Tabela 6 (§5.1). A direção da normalização é reportada sem presunção. |
| REV-15 (meta Selic SGS 432 para LPs lineares, de estado e H2; F e Wald HAC) | **Parcial** | A meta Selic entra só nas LPs de estado (especificação 9). LP linear e H2 **não** foram reestimadas, embora o §3.2 diga "reestimamos tudo" (R1b-2). O F clássico (p=0,551) e o Wald HAC (p<0,001) são reportados juntos (resolve D6). "Não antecipado" saiu do resumo. Fiz a reestimação que faltava: H2 sobrevive (J^fam h=12 = +0,270 por p.p., p_NW=0,012, p_EWC=0,020; **+0,071 por DP**, quase igual à base). |
| REV-16 (SVAR com sazonais como base) | **Resolvido** | `comum.fit_var(seasonal=True)`. A Tabela 2, as Figs. 2–3 e a §4.2 foram refeitas. Pico em h=5 de +0,21 (+0,33 sem dummies), conferido. Portmanteau e autocorrelação residual reportados. O resumo distingue as especificações. |
| REV-17 (h=0 por construção; Holm sem h=0; "forte aderência") | **Resolvido** | §3.3 ("por construção; essa igualdade não é evidência"). Holm sem h=0. "Forte aderência" foi removido, e as divergências LP×SVAR estão descritas. |
| REV-18 (grade de limiares; sup-Wald bootstrap; estado não baseado na Selic) | **Parcial** | A Fig. 6 e o sup-Wald bootstrap (p=0,333 em h=12 e 0,128 em h=24) foram implementados e conferem. **Falta** um indicador de estado que não dependa da Selic: o juro real *ex ante* ainda é Selic menos Focus. A descrição da grade é seletiva, e o sup-Wald de h=24 é atingido num limiar com 22 meses de platô (R1b-3). |
| REV-19 (bootstrap Kilian; negrito) | **Resolvido** | Bandas de Kilian na Tabela 2 e na Fig. 2. O negrito segue o intervalo bootstrap. As quedas da inflação em h=18–24 deixaram de ser destacadas. |
| REV-20 (inconsistências numéricas) | **Resolvido** | "0,357", "abaixo de 0,01" e "quatro grandes" não aparecem mais (0 ocorrências). Cinco episódios estão listados. A convenção da FEVD está na legenda da Fig. 3. |
| REV-28 (γ̂ como associação) | **Resolvido** | γ̂ é tratado como associação de nível, compatível com Fisher e com a regra de reação. A especificação pelo juro real *ex ante* está destacada. "Mais estável" e "sete de oito" foram removidos. |
| REV-29 (IC-Br em US$) | **Resolvido** | SGS 29042 na base. A 27574 virou robustez (especificação 10; corr. dos choques 0,993). A FEVD reporta as duas versões. |
| REV-32 (parte inferencial: MA(2), h=0, safra) | **Resolvido** | NW com h+3, amostra trimestral não sobreposta, corte em 2023:12, discussão de h=0 e `data/safra_dados.txt`. A amostra trimestral enfraquece h≤12 (+0,19, p=0,43), e o texto reporta isso com franqueza. |
| REV-33/34 (parte metodológica: mesmo choque, decomposição, J−S) | **Resolvido** | `canal_familias.py` usa o choque-base para todas as séries. A identidade J+A=S foi verificada (erro máximo de 0,000). A taxa implícita J/E explica J. |
| REV-38 (`consider`: tabela de episódios) | **Resolvido** | Tabela `tab:episodios`, conferida com §F. |
| REV-14b, REV-15b (`consider`: identificação dependente de estado; HFI) | **Não feito (declarado)** | Listados como extensões na Limitação 1. Aceitável para itens `consider`. |

Nenhum item piorou.

---

## Replicação

**O que rodei.** Copiei `manuscrito/` para `replica/pkg/` e executei, na ordem do apêndice, `estimacao_svar_lara_resende.py`, `estimacao_local_projections.py`, `canal_familias.py`, `aritmetica_fiscal.py`, `estimacao_regime_juros_altos.py` e `inferencia_regimes.py`, sem acesso à rede. O SVAR agora roda offline a partir dos CSVs, o que atende à sugestão da 1ª rodada.

**Resultado.** Os seis arquivos de `resultados/` são **idênticos byte a byte** aos do pacote (`diff` vazio), inclusive os dois bootstraps de sementes fixas. O PDF confere com o `.tex` nos trechos amostrados.

**Números-chave (manuscrito contra reprodução contra checagem independente):**

| Quantidade | Manuscrito | Reprodução | Checagem independente (R1) |
|---|---|---|---|
| γ̂^12 | +1,61 (p_NW 0,003; EWC 0,013; Holm 0,019) | +1,606 (0,003; 0,013; 0,019) | EWC reimplementado com escores: t=+2,80, p=0,013 |
| γ̂^12, bootstrap sob a nula | p=0,073; q95 de \|t\| = 3,40 | idem | iid: p=0,080 (q95 3,20); wild: p=0,074 (q95 3,44) |
| β̂_mod^24 | −2,20 (NW 0,012; EWC 0,025; Holm 0,073; t de blocos −1,69) | idem | Holm recalculado: 0,073; EWC independente 0,025; defasagens aumentadas: −1,97 (p=0,087) |
| Diferença h=24 (base) | +1,60, IC NW [−0,28; +3,48], Wald 0,096 | idem | Wald bootstrap: iid p=0,254; wild p=0,254 (autor: 0,236) |
| MDE 80% h=12 / h=24 | 2,55 / 2,69 por p.p.; 0,40 / 0,42 por DP | idem | 2,802×EP NW: 2,55 / 2,69. Com EWC: 2,70 / **3,32** (0,52 por DP) |
| LP interagida h=24 | β_alto +1,69; β_mod −2,46; Wald NW 0,001, EWC 0,009 | idem | **Wald bootstrap sob a nula: iid p=0,097; wild p=0,090** (q95 da estatística: 14,0 (iid) e 13,1 (wild) contra χ²₁ = 3,84) |
| J^fam LP h=12 | +0,431 (NW 0,006; EWC 0,015; Holm 0,012); 0,067 por DP | idem | p ∈ {2,…,12}: +0,40 a +0,49; meta Selic: +0,270 (p 0,012), **0,071 por DP**; defasagens aumentadas: +0,480 (p 0,003) |
| Sensibilidade de β_mod^24 a p | p=2: −1,29 (0,136); p=12: −0,14 (0,908) | idem | coerente com a 1ª rodada (−1,23 e −0,49 sem sazonais) |
| sup-Wald (grade 9–14%) | p=0,333 (h=12), 0,128 (h=24) | idem | o sup de h=24 (11,37) é atingido no limiar de 14%, com 22 meses de platô na amostra h=24 (2006–07 e 2016–17) |
| Previsibilidade do choque | F=0,95 (p=0,55); Wald HAC p<0,001 | idem | — |
| F das sazonais "p < 10⁻¹¹" | texto, §3.2 | **não é gerado por nenhum script** | só com dummies: p=5×10⁻¹²; na equação do VAR(6): F=4,12, p=1,7×10⁻⁵ |

Scripts e saídas: `replica/r1b_checks.py` → `r1b_checks_output.txt` (bootstrap da LP interagida, meta Selic, LP com defasagens aumentadas); `r1b_checks2.py` → `r1b_checks2_output.txt` (EWC independente, MDE, Holm, episódios, limiar de 14%, assimetria de J em h=0); `r1b_checks3.py` → `r1b_checks3_output.txt` (F das sazonais).

### A leitura "H1 inconclusiva" é a correta?

Sim, com uma ressalva de argumentação. O manuscrito contrapõe a LP interagida (Wald p=0,001) ao bootstrap sob a nula, que "não rejeita". Mas o bootstrap do autor (`inferencia_regimes.py` §D) calcula a distribuição nula **apenas** das estatísticas da especificação-base. A rejeição da LP interagida nunca foi calibrada. Calibrei-a com o mesmo DGP linear do autor, com resíduos iid e, à parte, com wild bootstrap Rademacher. Sob a nula, a estatística de Wald da interagida em h=24 tem quantil de 95% de 14,0 (iid) e 13,1 (wild), contra 3,84 da χ²₁. A taxa de rejeição nominal a 5% é de **30–34%**, e o p-valor bootstrap da estatística observada (10,35) é **0,097 (iid) e 0,090 (wild)**. Em h=12, o p_boot é de 0,94. A rejeição "p=0,001" é, portanto, em grande parte um artefato de sobreparametrização com HAC: 98 regressores, N=228 e cerca de 4 episódios. Calibrada, ela é marginal (p≈0,09) e do mesmo tamanho que a da base em h=24 sob a mesma régua. Isso **sustenta** a leitura "inconclusiva", mas por uma razão que o texto não mostra.

Os demais elementos também apontam para "inconclusivo", e não para "contrário" ou "favorável":
- Na base, a diferença tem sinal **contrário** a H1 em h=12 (−1,05) e **favorável** em h=24 (+1,60). Nenhuma das duas é significativa.
- Na grade, a diferença em h=12 é negativa e significativa para limiares de 9% a 10% (contra H1). Em h=24, é positiva em toda a grade e significativa a 5% nos limiares de 11,5%, 12%, 13% e 14% (a favor de H1).
- Pela p-sensibilidade, a diferença em h=24 nunca é significativa com p ≠ 6 (Wald entre 0,197 e 0,905).
- O platô contribui, em h=24, com 105 observações de quatro episódios, e o mais longo (2006–09) pesa 44 delas. Qualquer rejeição isolada repousa em pouquíssima variação independente.

O texto deve trocar a frase-chave por uma afirmação calibrada: "a única rejeição forte vem de uma especificação cuja estatística, sob a nula linear, tem quantil de 95% de 14,0 (iid) e 13,1 (wild); com essa calibração, p ≈ 0,09–0,10". Mantida essa troca, a conclusão está certa.

---

## Problemas novos

### R1b-1 — A LP totalmente interagida não é calibrada pelo bootstrap sob a nula — **Maior**
- **Localização**: §4.5, "Especificação totalmente interagida" e "Bootstrap sob a nula..."; resumo ("produz diferença significativa"); Conclusão, 1º parágrafo; `inferencia_regimes.py` §B e §D.
- **Evidência**: o §D calcula `tg12`, `w12`, `w24` e os sup da especificação-base. O §B (98 regressores, N=228, NW com 25 defasagens) usa só valores críticos assintóticos. Com o mesmo DGP do autor, obtive: 

  | Estatística | Observado | p boot iid | p boot wild | q95 sob a nula (iid/wild) | Rejeição nominal a 5% sob a nula |
  |---|---|---|---|---|---|
  | Wald interagida h=24 | 10,35 | 0,097 | 0,090 | 14,0 / 13,1 | 30% / 34% |
  | Wald interagida h=12 | 0,02 | 0,943 | 0,933 | 12,9 / 12,8 | 27% / 25% |
  | Wald base h=24 | 2,77 | 0,254 | 0,254 | 6,8 / 7,1 | 15% / 17% |
  | \|t\| de γ^12 | 2,96 | 0,080 | 0,074 | 3,20 / 3,44 | 28% / 25% |

  (B=299 por esquema; `replica/r1b_checks_output.txt`.) Sob a nula linear, o teste NW da interagida rejeita em cerca de um terço das réplicas.
- **Por que importa**: o resumo e a Conclusão apresentam a rejeição interagida como evidência "de sinal favorável à hipótese" e o bootstrap como evidência de não significância, sem aplicar a mesma régua às duas. É exatamente o ponto em que a leitura de H1 se decide.
- **Correção**: incluir `wi12`/`wi24` no laço do bootstrap (custo marginal pequeno), reportar p_boot e quantis no Painel B da `tab:nulo` e no texto, e reescrever a frase do resumo de acordo com o resultado. Opcional: aplicar também à interagida a sensibilidade a p e à meta Selic.

### R1b-2 — "Reestimamos tudo com a meta Selic" é incorreto — **Menor**
- **Localização**: §3.2, 2º parágrafo ("Como alternativa de menor custo, reestimamos tudo com a meta Selic do último dia do mês (SGS 432)").
- **Evidência**: `build_system(policy='meta_selic')` só é chamado em `estimacao_regime_juros_altos.py` (especificação 9). `estimacao_local_projections.py` e `canal_familias.py` não usam a meta. REV-15 pedia LPs lineares, de estado e H2.
- **Correção**: reestimar a LP linear e H2 com a meta (minha checagem mostra que H2 sobrevive: +0,270 por p.p., p=0,012; 0,071 por DP) e reportar. Ou trocar "tudo" por "as LPs dependentes de estado".

### R1b-3 — Descrição seletiva da grade de limiares e trimming agressivo — **Menor**
- **Localização**: §4.5, "Bootstrap sob a nula de linearidade e grade de limiares"; Fig. 6.
- **Evidência** (`inferencia_regimes.txt` §G):
  - o texto diz que a diferença em h=24 "é positiva entre 9,5% e 13%, com p-valores pontuais entre 0,03 e 0,18". Mas ela é positiva em **toda** a grade, e no limiar de 14% vale +4,53 com **p=0,001**, o maior Wald da grade (11,37, que define o sup-Wald observado);
  - no mesmo limiar, a diferença em h=12 troca de sinal (+3,17, p=0,040);
  - o limiar de 14% corresponde ao quantil 0,87 da MM12, com 31 meses de platô (22 na amostra h=24, só de 2006–07 e 2016–17). Isso fica abaixo do trimming usual de 15% (Andrews, 1993; Hansen, 2000).
- **Correção**: descrever a grade inteira, restringir a grade aos quantis [0,15; 0,85] (ou reportar as duas versões) e refazer o sup-Wald bootstrap.

### R1b-4 — O bootstrap sob a nula reamostra resíduos iid, embora o próprio texto rejeite a ausência de autocorrelação residual — **Menor**
- **Localização**: §3.4, item 3; `inferencia_regimes.py` §D (`ids = rng.integers(0, len(U), T)`).
- **Evidência**: o Portmanteau rejeita a 12 e 24 defasagens (§4.1), e a amostra inclui a COVID. O bootstrap iid ignora a heterocedasticidade condicional e a dependência residual. Com wild bootstrap (Rademacher), obtive: os p-valores praticamente não mudam (γ^12: 0,074 contra 0,080 no iid; Wald base h=24: 0,254 nos dois; interagida h=24: 0,090 contra 0,097). A conclusão é robusta ao esquema, mas isso precisa ser mostrado no artigo. Observação adicional: em 3% (iid) a 7% (wild) das réplicas, a Selic simulada fica negativa em algum mês, porque o DGP linear quase não estacionário (raiz 0,9995) não respeita o limite inferior. Convém reportar isso ou descartar essas réplicas como sensibilidade.
- **Correção**: reportar uma variante wild ou de blocos de resíduos, ao menos para γ^12 e para os Wald confirmatórios, e mencionar a restrição.

### R1b-5 — Tabela 5 sem inferência robusta; N por regime e horizonte fora do manuscrito — **Menor**
- **Localização**: Tabela `tab:robustez`; §4.5, "Episódios".
- **Evidência**: as Tabelas 4 e 3 têm EWC, mas a Tabela 5 só traz NW. Ali está o argumento "2 de 22 Wald rejeitam, o que se espera por acaso", que ainda ignora a forte correlação entre esses testes. O N por regime e h (por exemplo, h=24: 105 no platô e 123 no regime moderado) só existe em `resultados/`.
- **Correção**: acrescentar o p EWC para β_mod^24 e para o Wald na Tabela 5; incluir uma linha de N_alto/N_mod na Tabela 4; retirar ou qualificar o argumento "por acaso".

### R1b-6 — MDE apresentado só com o EP Newey-West, que o próprio artigo considera otimista — **Menor**
- **Localização**: §4.5, "Poder e intervalo da diferença"; `tab:nulo`; resumo ("cerca de 0,4 p.p.").
- **Evidência**: `inferencia_regimes.txt` §A já calcula o MDE EWC: 2,70 em h=12 e **3,32** em h=24 (0,52 por DP), mas o manuscrito não o reporta. A redação do resumo ("diferenças de até cerca de 0,4 p.p. ... não seriam detectadas com 80% de poder") também inverte o conceito: o MDE é a menor diferença detectada com 80% de poder, e diferenças menores têm poder inferior a 80%.
- **Correção**: incluir a linha MDE EWC na `tab:nulo` e reescrever a frase ("diferenças menores que cerca de 0,4–0,5 p.p. por DP seriam detectadas com probabilidade inferior a 80%").

### R1b-7 — Assimetria de J^fam em h=0 sinaliza um termo em |choque|, não reportado — **Menor**
- **Localização**: §4.7, item 4; `canal_familias.txt`, robustez de H2, h=0.
- **Evidência**: em h=0, b⁺ = +0,144 (p=0,003) e b⁻ = −0,171 (p=0,001), com p_sim < 0,001. Como b⁻ multiplica valores negativos, **as duas surpresas elevam J no impacto**, horizonte em que o texto diz que a resposta é nula. Isso indica que a decomposição ± capta um efeito de magnitude (|choque|, volatilidade ou medição), e não assimetria de transmissão. A "rejeição da simetria a 10% entre 9 e 24 meses" deve ser lida com isso em mente.
- **Correção**: reportar h=0 da especificação assimétrica e incluir |choque| como regressor de controle, ou discutir o ponto.

### R1b-8 — Pequenas lacunas de replicabilidade — **Menor**
- O F das 11 sazonais "p < 10⁻¹¹" (§3.2) não sai de nenhum script. Reproduzi p=5×10⁻¹² só numa regressão da inflação em dummies sem defasagens. Na equação do VAR(6), p=1,7×10⁻⁵. O texto deve dizer qual é o teste, e o script deve gerá-lo.
- `data/safra_dados.txt` registra a data de extração de `base_macro_bcb.csv` como **texto fixo** no `coleta_series_complementares.py`, e não como data efetiva de um download. A data da base principal é declarada, não registrada. Convém gravar a data no momento da extração ou incluir um hash do arquivo.
- O apêndice ainda traz o URL do GitHub e a seção de mudanças com `\anonimofalse`. Não é ponto metodológico, mas convém registrar.

### Observação (sem ID): H2 na amostra trimestral
Na amostra trimestral não sobreposta, J^fam em h=12 vale +0,19 (p=0,43) e só é significativo em h=18 (+0,82, p=0,008). O texto já reporta isso. Ainda assim, convém que o resumo não fixe o "resultado mais robusto" em h=12 sem mencionar que o pico robusto está em 12–18 meses.

---

## Pontos fortes

1. **Reprodutibilidade exemplar.** Seis scripts, sementes fixas, execução offline e saídas idênticas byte a byte, incluindo os bootstraps. O código é modular (`comum.py`) e legível.
2. **Resposta séria à crítica de inferência.** EWC (cuja implementação conferi de forma independente), banda sup-t, bootstrap recursivo sob a nula com reestimação do VAR, do choque e do estado (o procedimento certo para regressor gerado e estado persistente) e sup-Wald na grade. Poucos artigos aplicados fazem isso.
3. **O nulo tornou-se informativo.** IC da diferença, MDE, LP interagida e a frase explícita "inconclusivo, e não uma rejeição". O texto evita a falácia da diferença de significâncias e já não lê ausência de evidência como evidência de ausência.
4. **Rebaixamento honesto do que não resistiu.** β_mod^24 virou "sugestivo, não robusto". γ̂ passou a ser associação de nível e é declarado não significativo sob bootstrap. O placebo de h=0 virou diagnóstico. A troca do IC-Br e o papel das sazonais estão documentados.
5. **H2 bem fundamentado.** Mesmo choque para J, A, S, S sem habitacional e E; decomposição pela taxa implícita; robustez à MA(2), à revisão da renda, a p e (na minha checagem) à meta Selic.
6. **Primeiro estágio e episódios.** A tabela de episódios e a normalização pela Selic acumulada dão ao leitor a medida exata do que a amostra pode identificar.

---

## Recomendação

**Minor Revision.** **Confiança: 4.** A área é central para mim e reproduzi tudo. Desconto um ponto porque não tenho acesso às séries originais além dos CSVs do pacote.

Os bloqueantes metodológicos da 1ª rodada (B2: poder, sensibilidade a p, HAC e invariância do choque) foram resolvidos. O que resta é calibrar a única rejeição forte (R1b-1), que pode reforçar ou matizar a leitura "inconclusiva" sem derrubá-la, e fazer correções de texto e de tabela (R1b-2 a R1b-8). Não vejo necessidade de nova rodada completa de revisão metodológica se R1b-1 a R1b-3 forem atendidos e conferidos pelo editor.

### Cinco questões mais importantes
1. **R1b-1**: submeter a LP interagida (Wald h=24, p=0,001) ao mesmo bootstrap sob a nula e reescrever o resumo e a Conclusão com o p calibrado.
2. **R1b-2 / REV-15**: a meta Selic só entrou nas LPs de estado. Reestimar a LP linear e H2, ou corrigir "reestimamos tudo".
3. **R1b-3**: descrever a grade inteira (limiar de 14%: p=0,001 em h=24, com 22 meses de platô) e aplicar trimming de 15% ao sup-Wald.
4. **R1b-4 / R1b-6**: bootstrap wild ou de blocos sob a nula e MDE EWC (3,32 em h=24) no manuscrito, com a redação do MDE corrigida.
5. **R1b-5 / REV-13**: EWC na Tabela 5, N por regime na Tabela 4 e retirada do argumento "2 de 22 por acaso".
