# Conferência numérica do manuscrito (v5)

Escopo: `manuscrito/artigo_svar_lara_resende.tex` (670 linhas) contra `manuscrito/resultados/*.txt`, `scripts/` e `data/`. Conferência célula a célula das Tabelas 1 a 12 e das Tabelas de insumos fiscais; frase a frase dos resumos PT/EN, §1, §2.2, §3, §4.1-4.7, §5, conclusão e Apêndice B. Verificação complementar por varredura automática (todo número decimal do .tex com ≥ 2 casas procurado, com o mesmo arredondamento, nas saídas) e por reexecução parcial de `comum.py` (estado de platô a 14%, J/E, superávit primário). Os scripts com bootstrap não foram reexecutados.

## (a) Discrepâncias

| Linha .tex | Trecho | Valor no texto | Valor na saída (arquivo:linha) | Classificação | Correção sugerida |
|---|---|---|---|---|---|
| 492 | "a diferença entre as razões tem intervalo de ... em 12 meses e ... em 24 meses" (§4.5, Primeiro estágio) | 12 m: [-0,30; +0,07]; 24 m: [-1,08; +1,68] | `inferencia_regimes.txt:49` 12 m: [-0.375; +0.069]; `:50` 24 m: [-1.749; +1.056] | **erro** (3 dos 4 limites; só o +0,07 confere) | Trocar por [-0,38; +0,07] em 12 meses e [-1,75; +1,06] em 24 meses. A conclusão ("não altera, em nenhuma direção") continua válida. |
| 556 | "a inflação acumulada cai 0,14 p.p. em 24 meses por 1 p.p. (p = 0,012; p_Holm = 0,071)" | "inflação acumulada" | `canal_familias.txt:213` (-0.1379, p 0.012, Holm 0.071). A variável dependente é `ipca_livres` em nível em t+h (% a.m.), sem soma: `canal_familias.py:133-134`, `lp(y,...)` com `y.shift(-h)`. Os acumulados só existem nas LPs de estado (`comum.py:cum`). | **descrição incorreta** | Escrever "a inflação mensal de itens livres em t+24 cai 0,14 p.p. (% a.m.) por 1 p.p." ou comparar com o -0,289 da Tabela 6. Não pôr lado a lado com o β_mod^24 = -2,20, que é acumulado. |
| 402 | "a LP atinge o pico mais tarde (+0,57 p.p. em h = 18 ...)" | pico em h = 18 | `comparacao_svar_vs_lp.txt:153`: pico da LP de J^fam em **h = 19**, +0,5851 | descrição incorreta (leve; vale na grade reportada) | "... +0,57 p.p. em h = 18 (pico de +0,585 em h = 19, fora da tabela)". |
| 178 (Tab. insumos) × 252 (Tab. séries) × 286 | SGS 4189 chamada de "Selic (média do mês)", "Selic acumulada no mês, anualizada" e "média mensal da Selic diária" | três descrições | `aritmetica_fiscal.txt:7` e `estimacao_*`: só "SGS 4189" | descrição inconsistente (leve, não numérica) | Padronizar com a descrição oficial da série (acumulada no mês, anualizada, base 252) em 178, 252 e 286. |
| 160 | "O ensaio de 2026 cita uma taxa de cerca de 5,7% ao ano, que corresponde ao diferencial ī - g_nom ... com o custo médio de junho" | 5,7% e "custo médio de junho" | nenhuma saída traz o custo médio de junho; `aritmetica_fiscal.txt:11` só tem set/2026 (12,63%) | **sem fonte**. Não derivável do pacote: 12,63 - 7,22 = 5,41; 5,7 exigiria custo de ≈ 12,9%. | Citar o valor de junho (RMD) em `aritmetica_fiscal.py` ou na Tabela de insumos, ou remover a frase. |
| 221 | "(cerca de 5% com Selic de 7,5%, contra IPCA de 4,22% ...)" | 5% | 4,22% confere (`aritmetica_fiscal.txt:9`). O 5% (= 7,5% - crescimento real) usa um crescimento real que não está nas saídas. | **sem fonte** (parcial; parece vir do ensaio) | Dar a fonte (ensaio, p. X) ou o crescimento real assumido (7,5 - 2,5). |
| 586 | "A taxa implícita J/E sobe 6,4% em 12 meses" | 6,4% | `canal_familias.txt:57`: 100 ln(J/E) = +6,442, ou seja, pontos log (6,65% em variação percentual exata) | arredondamento/unidade inconsistente (leve) | Dizer "6,4 pontos log (≈ 6,7%)" ou "6,4 log-pontos". Mesmo para "1,0% por 1 DP" (1,0052 log-pontos). |
| 619 | "apreciação de 14,8% em 12 meses" | 14,8% | `regime_juros_altos_lp.txt:134`: -14,766 em 100×ln PTAX (apreciação percentual exata: 13,7%) | arredondamento/unidade inconsistente (leve) | "queda de 14,8 log-pontos (≈ 13,7%)". |
| 439 | "nenhum β_alto ... é significativo (p_NW ≥ 0,27)" | 0,27 | `regime_juros_altos_lp.txt:11`: mínimo 0,268 (h = 18) | arredondamento (trivial) | "p_NW ≥ 0,268" ou "> 0,26". |
| 75 | "associa-se a inflação acumulada mais alta em 9 a 12 meses" | 9 a 12 | `regime_juros_altos_lp.txt:11`: γ^18 também tem p_NW = 0,041 (Holm 0,162; EWC 0,074) | observação (leve; coerente com o uso de Holm/EWC) | Opcional: "em 9 a 12 meses (e, sem ajuste, em 18)". |

Observação sobre o item 402: a conferência foi feita sobre a grade reportada; a afirmação só é falsa se lida como máximo sobre h = 0..24.

### Números "sem saída direta", mas deriváveis e conferidos

| Linha | Valor | Conta |
|---|---|---|
| 183 | R$ 4,84 tri / R$ 13,40 tri | 9382,95 × 0,5160 = 4841,5 bi; PIB 13402,0 (`aritmetica_fiscal.txt:13`) |
| 221 | "cerca de 45% da DPF" | 21,14 + 23,59 = 44,73% |
| 284 | "cerca de seis desvios-padrão" | 1 / 0,156 = 6,4 |
| 309 | ν = 15 | ⌊0,4 × 252^(2/3)⌋ = ⌊15,96⌋ = 15; 14 em h = 24 (T = 228), confere com `inferencia_regimes.txt:22` |
| 438, 446, 465, 489 | conversões "por 1 DP" | β × 0,156: -2,201 → -0,343; 2,69 → 0,420 etc.; meta Selic 0,2697 × 0,2636 = 0,0711 (`canal_familias.txt:202`). Todas conferem. |
| 479 | 3,84 | quantil 95% de χ²(1) |
| 483 | "31 meses (22 na amostra de h = 24, nos episódios de 2006-2007 e 2016-2017)" | Reexecutado com `comum.py` (limiar 14,0): 31 meses; 22 no h = 24; episódios 2006:03-2007:04 e 2016:06-2017:01. A saída só traz o 31 (`inferencia_regimes.txt:133`). |
| 586 | "J/E médio de 21%" | média amostral = 21,3% (dados); só a série 2005/2021/ago-2026 está na saída (`canal_familias.txt:244`) |
| 623 | superávit 3,5% → 2,1% (ago/2011 a out/2012); déficits 1,4% a 2,9% (2016-2018) | `base_complementar_bcb.csv`, SGS 5793: -3,53 (2011-08), -2,07 (2012-10); janela out/2016 a mar/2018: mín. 1,42, máx. 2,87. Confere (a janela do ciclo de cortes precisa ser dita no texto; em 2016-2018 completos a faixa é 1,13 a 3,04). |

Sugestão: gravar esses números derivados em uma saída (por exemplo, `inferencia_regimes.txt` e `aritmetica_fiscal.txt`) para que a cadeia fique rastreável.

## (b) Contagens

Estimativa de valores numéricos conferidos: cerca de 1.250. Distribuição aproximada: Tabela 2 (insumos), 16; Tabela 3 (cenários), 36; Tabela 4 (séries), 14 códigos; Tabela 5 (SVAR), 84; Tabela 6 (SVAR × LP), 91; Tabela 7 (estado), 170; Tabela 8 (nulo), 100; Tabela 9 (episódios), 45; Tabela 10 (robustez), 300; Tabela 11 (famílias), 108; Tabela 12 (câmbio), 35; texto corrido e resumos, 250 aproximadamente.

| Classe | Ocorrências |
|---|---|
| Conferem (diretas ou deriváveis, incluindo arredondamento padrão) | ≈ 1.235 |
| **Erro** | 1 ocorrência (linha 492; 3 limites numéricos errados) |
| **Descrição incorreta** | 3 (556 "acumulada"; 402 pico em h = 18 vs 19, leve; 178/252/286 descrição de SGS 4189, leve) |
| **Sem fonte** | 2 (160 "5,7% ... custo médio de junho"; 221 "cerca de 5%") |
| Arredondamento/unidade inconsistente | 4 (586, 619 pontos log vs %; 439; 75, leves) |

### Consistência interna e contagens verificadas (todas conferem)

- Resumo × corpo × conclusão: 0,07 p.p. por DP em 12 meses (0,0673), ≈ 0,4 p.p. por DP de MDE (0,398 a 0,420), p = 0,093/0,092 do γ^12 sob a nula, p = 0,057 da meta Selic, limiar de 14%, 1,1 a 1,3 p.p. e ≈ 4% do PIB. Sem divergência.
- "4 de 11 limiares" (p_Wald24 < 0,05: 11,5%, 12%, 13%, 14%): confere. "10 de 11" (dif12 < 0): confere. "9 de 11" (γ^12 com t > 1,96): confere (`inferencia_regimes.txt:134`). dif24 > 0 em 11 de 11: confere.
- "2 de 22 testes de Wald do Painel A" (NW: spec. 6 em h = 12, p = 0,033; spec. 7 em h = 24, p = 0,029) e "um pelo EWC" (spec. 6, h = 12, 0,040): confere. A saída `regime_juros_altos_lp.txt:124-126` conta 2 de 60 (NW) e 2 de 60 (EWC) em 10 especificações × 6 horizontes. O segundo EWC é a especificação 6 em h = 3 (0,037), fora do recorte h = 12/24 do texto. Sem conflito.
- Frequências sob a nula: 25% (0,253 iid; 0,249 wild) e 16% (0,159 iid; 0,143 wild; o texto cita só o iid) conferem. Réplicas com Selic negativa: 4,1% e 4,4%.
- Tabelas 8 e 11 reproduzem o bloco "COM defasagens da própria variável" de `canal_familias.txt`, e não o "só controles do sistema". O texto da §4.7 usa o MDE do bloco "só controles do sistema" (1,13 e 0,76), e isso está declarado na saída (`:225`). Confere.
- Seções referenciadas (4.4, 4.5, 4.6, 4.7, 2.2, 3.1) existem e apontam para o conteúdo correto.
- Os números das Tabelas 5 a 12 e das tabelas fiscais coincidem com as saídas até o arredondamento (bolds de significância coerentes com p < 0,05 NW; Holm e EWC nas células corretas).
