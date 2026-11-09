# Juros altos tiram a força da política monetária? O que 20 anos de dados brasileiros conseguem (e não conseguem) dizer

*Um estudo empírico sobre a tese de André Lara Resende, com dados do Banco Central de 2005 a 2026*

**Imagem de capa sugerida:** `figuras/figura1_series_historicas.png` (Selic, inflação e comprometimento de renda das famílias, 2005–2026)

---

Em setembro, André Lara Resende publicou o ensaio *Eu Acuso: uma proposta para eliminar os juros absurdos*. A tese reacendeu um debate antigo: com juros tão altos por tanto tempo, a Selic ainda funciona como remédio contra a inflação, ou passou a pesar mais na dívida pública e no bolso das famílias do que nos preços?

Decidi testar uma parte dessa pergunta com dados. O resultado é menos espetacular do que qualquer um dos lados do debate gostaria, e acho que por isso mesmo vale a pena contar.

## A pergunta

Se a tese estiver certa, uma alta de juros deveria reduzir menos a inflação quando a Selic já está num patamar persistentemente alto do que quando está num nível moderado. Isso é o que os economistas chamam de **dependência de estado**: o efeito da política depende da situação em que ela é aplicada.

Para testar, usei 258 meses de dados públicos do Banco Central (março de 2005 a agosto de 2026). Separei as surpresas da Selic, a parte das decisões que não era explicada pela inflação, pela atividade, pelo câmbio e pelas commodities. Depois medi como a inflação respondeu a essas surpresas em dois regimes: o **platô de juros altos**, quando a média da Selic em 12 meses estava acima de 11,27% a.a., e o **regime moderado**.

## O que encontrei

**1. Não dá para dizer que a tese está certa, nem que está errada.**

Na especificação principal, a resposta da inflação não é estatisticamente diferente nos dois regimes. Mas o ponto importante é outro: o teste tem pouco poder. O Brasil teve só cinco episódios de platô desde 2005. Com tão poucos episódios, diferenças do tamanho do próprio efeito da política monetária passariam despercebidas na maior parte das vezes.

Algumas especificações chegam a apontar uma diferença no sentido previsto pela tese. Outras apontam no sentido oposto. Quando calibrei esses resultados com um bootstrap que simula como os testes se comportariam se não houvesse diferença nenhuma, nenhum deles se sustentou a 5%. A conclusão honesta é que **a evidência mensal agregada não arbitra essa controvérsia**.

**2. O efeito desinflacionário clássico aparece, mas é frágil.**

No regime moderado, uma alta de juros reduz a inflação acumulada em 24 meses. O resultado, porém, depende de escolhas técnicas, como o número de defasagens do modelo e a medida da taxa de juros usada (Selic média do mês ou meta do Copom).

**3. Juros altos andam junto com inflação mais alta, o que não prova muita coisa.**

Os meses de platô estão associados a inflação mais alta nos 12 meses seguintes. Isso é compatível com a ideia de que juros altos alimentam a inflação, mas é igualmente compatível com o óbvio: o Banco Central mantém os juros altos justamente quando a inflação está alta. A associação desaparece quando o regime é definido pelo juro real, e não pelo nominal.

**4. Nas famílias, o efeito é claro, mas modesto e convencional.**

Uma surpresa de alta na Selic eleva a parcela da renda das famílias comprometida com juros, cerca de 0,07 a 0,09 ponto percentual por surpresa típica, com pico entre 12 e 18 meses. O canal é a taxa média das dívidas, e não o aumento do endividamento. O efeito aparece em várias especificações diferentes, mas fica no limite da significância quando o teste é calibrado. Também não encontrei evidência firme de que surpresas de baixa aliviem o orçamento das famílias na mesma velocidade.

Isso confirma o que a teoria convencional já esperava: os juros chegam ao bolso das famílias. Não é evidência a favor nem contra a tese de que os juros altos tornam o endividamento insustentável.

## E a conta fiscal?

O ensaio estima que reduzir a Selic para cerca de 7,5% geraria uma economia fiscal de aproximadamente 4% do PIB ao ano. Refiz a aritmética em termos reais, com dados do Relatório Mensal da Dívida do Tesouro. Encontrei três pontos:

- **No primeiro ano**, com inflação estável, um corte gradual reduziria a razão dívida/PIB em 1,1 a 1,3 ponto percentual do PIB, porque só a parcela da dívida atrelada à Selic se beneficia de imediato.
- **Os 4% do PIB** correspondem ao cenário em que toda a dívida já foi rolada a 7,5%. É um teto, e a rolagem levaria anos: só 20% da dívida federal vence em 12 meses.
- **O alívio depende de quanto a inflação acompanha a queda dos juros.** Se ela cair metade do que os juros caem, o ganho fiscal do primeiro ano praticamente some. O ensaio supõe que a inflação é inercial e não reage à demanda, e nesse cenário o alívio existe. Mas essa hipótese é justamente a que está em disputa, e ela não foi testada aqui.

## O que fica

Três lições, para além do resultado em si:

1. **"Não encontrei efeito" é diferente de "não há efeito".** Reportar o poder do teste, ou seja, o tamanho do efeito que ele conseguiria detectar, deveria ser rotina em debates de política econômica.
2. **Com poucos episódios, a escolha de especificação pesa muito.** Encontrei resultados "significativos" a favor e contra a tese, dependendo de escolhas razoáveis. A calibração por bootstrap derrubou ambos.
3. **O debate sobre os juros no Brasil merece dados melhores.** Surpresas de alta frequência nos contratos futuros de DI, variáveis de risco fiscal e, sobretudo, uma mudança permanente do patamar de juros, que é o que o ensaio realmente propõe, são o que poderia responder à pergunta. As surpresas mensais que usei são marginais e transitórias.

O artigo completo traz a metodologia (VAR estrutural, projeções locais dependentes de estado e inferência robusta com bootstrap), todas as tabelas e as limitações. Os dados e o código de replicação, em Python, ficam disponíveis para quem quiser refazer ou contestar as contas.

Críticas e sugestões são muito bem-vindas, especialmente de quem trabalha com política monetária e dívida pública.

---

*Ângelo Augusto Bonvenuto é pesquisador independente. Este texto resume um working paper que ainda não passou por revisão em periódico. Todos os dados são públicos (Banco Central do Brasil e Tesouro Nacional).*

\#PolíticaMonetária #Economia #Selic #Inflação #DívidaPública #Econometria #Brasil

---

## Post curto para o feed (para divulgar o artigo)

> Juros altos tiram a força da política monetária?
>
> Testei uma parte da tese de André Lara Resende com 20 anos de dados do Banco Central. A resposta honesta: os dados não arbitram a controvérsia. O Brasil teve só cinco episódios de juros persistentemente altos desde 2005, poucos demais para detectar diferenças do tamanho do próprio efeito da Selic.
>
> O que os dados mostram com mais clareza:
> • a alta de juros chega ao bolso das famílias pela taxa média das dívidas, não por mais endividamento;
> • a economia fiscal de "4% do PIB" é um teto que depende de a inflação não cair junto com os juros, e essa é justamente a hipótese em disputa.
>
> Artigo completo, com metodologia e limitações, no link. Críticas são bem-vindas.
