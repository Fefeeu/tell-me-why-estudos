# Projeto Churn
**Churn**, em português "taxa de cancelamento" ou "taxa de rotatividade", é uma métrica que mede a percentagem de clientes que deixaram de utilizar um produto ou serviço numa empresa num determinado período. Este indicador é crucial, especialmente em modelos de negócio recorrentes, como assinaturas e contratos contínuos, pois afeta diretamente o faturamento e o crescimento da empresa. Uma taxa de churn baixa é um sinal positivo, indicando que a empresa tem uma boa capacidade de reter os seus clientes. 


## SEMMA
O SEMMA é uma metodologia criada pela própria SAS Institute para orientar projetos de mineração de dados (Data Mining).

![](00_imagens/metodologia_SEMMA.png)
- **Amostragem** *sample*:

    Esta etapa envolve a escolha de um subconjunto do conjunto de dados de volume apropriado a partir de um vasto conjunto de dados fornecido para a construção do modelo. O objetivo desta etapa inicial do processo é identificar variáveis ou fatores (dependentes e independentes) que influenciam o processo. As informações coletadas são então classificadas em categorias de preparação e validação.

- **Exploração** *explore*:

    Durante esta etapa, são realizadas análises univariadas e multivariadas para estudar as relações interconectadas entre os elementos dos dados e identificar lacunas nos dados. Enquanto a análise multivariada estuda a relação entre as variáveis, a univariada analisa cada fator individualmente para compreender sua participação no conjunto. Todos os fatores de influência que podem influenciar o resultado do estudo são analisados, com forte dependência da visualização de dados.

- **Modificação** *modify*:

    Nesta etapa, as lições aprendidas na fase de exploração a partir dos dados coletados na fase de amostragem são derivadas com a aplicação da lógica de negócios. Em outras palavras, os dados são analisados e limpos, sendo então passados para a etapa de modelagem e explorados caso necessitem de refinamento e transformação.

- **Modelo** *model*:

    Com as variáveis refinadas e os dados limpos, a etapa de modelagem aplica uma variedade de técnicas de mineração de dados para produzir um modelo projetado de como esses dados alcançam o resultado final desejado do processo.

- **Avaliar** *assess*:

    Nesta etapa final do SEMMA, o modelo é avaliado quanto à sua utilidade e confiabilidade para o tópico estudado. Os dados agora podem ser testados e usados para estimar a eficácia do seu desempenho.

## Sample

![](00_imagens\exemplo_sample.png)

### Out of Time
Essa é uma parte não fixa da tabela, onde ela é uma parte da tebela que é separada pela(s) ultima(s) ***safra(s)***, exemplo: se for separado de 1 em 1 mês, então será usado um ou mais safras dos meses mais para frente.

E essa parte vai servir para verificar a estabilidade do modelo. Porem isso é algo mais usando quando se possui muitos dados, já que se existirem poucas amostras, essa verificação ira "roubar" parte dos dados do treinamento do modelo.

### Under e Over Samplim

![](00_imagens\over_under_samplim.png)

#### Under Samplim:
Reduz o tamanho da classe majoritária (a que tem mais exemplos) para equilibrar com a minoritária.

Exemplo: Se você tem 10.000 transações “não fraude” e 1.000 “fraude”, pode reduzir a classe “não fraude” para 1.000 exemplos → ficando 1.000 x 1.000.

#### Over Samplim:
Aumenta o tamanho da classe minoritária (a que tem menos exemplos), replicando ou gerando novos dados.

Exemplo: Se você tem 10.000 “não fraude” e 1.000 “fraude”, pode duplicar/gerar novas amostras da classe “fraude” até chegar também em 10.000 → ficando 10.000 x 10.000.

## Explore
É o momento da metodologia em que fazemos uma analise de seleção do que será análizado. **Exemplo:** Uma análise descritiva, Análise Bivariana, *Indendificação de Missings/NaN*

## Modify
É fazer uma transformação na tabela. *No sklearn é a parte de [Processing](https://scikit-learn.org/stable/modules/preprocessing.html)*

### Padronização Dos Dados
É ideal que haja uma padronização na escala dos dados, antes deles serem usados nos modelos. Aqui usaremos a **Padronização pela Normal** ![](00_imagens\formula_padronizacao.png)

### Imputação de Missing
#### Ex: Falta Tempo Pra Voltar
*"Vai faltar dado se essa pessoa nunca voltar"*

Uma tratamento que pode ser feito em relação a isso, é pegar a maior data de volta que tivemos.

#### Ex: Pontos Gastos Na Terça-feira
*"Vai faltar dados se essa pessoa nunca comprou nada terça-feira*

Um tratamento adequado para isso é trocar esse valor para 0

#### Ex: Data de Nascimento/Idade
Esse é um caso mais complicado, já que a idade pode estar interferindo, e não tem algo que possa ser feito de forma direta, como escolher o minimo, maximo, media, mediana, etc. Não é possível ter certeza, já que justamente a idade sair desses valores pode ser um motivo para esse resultado.

Então uma coisa que pode ser feita para tratar esses dados seria criar um modelo de predição com as lihas que possuimos a idade, e tentar prever qual ida
de provavelmente aquela linha teria.

[Texto do Téo Calvo sobre isso](https://teobcalvo.wordpress.com/2017/12/16/machine-learning-para-imputacao-de-missings)

### Binning
É quando se possui uma váriavel **continua** e a transformamos em **faixas**
#### Ex: Idades
X = 13, 24, 32, 58, 64, ...

Podemos separar por faixas simples:
F(x) = [16-25], [26-35], [36-45], [46-55], [56-65], ...

Podemos também separar essas faixas por um meio dinamico:
Exemplo: usando uma arvore binaria com a variavel resposta, para assim que ela separe da "melhor maneira" os bins. Alguns são contra essa idéia por usarmos a variavel resposta para fazer uma "predição" porem, como isso é feito com uma base de treinameto, a utilização dela nas outras bases (Teste e OOT) em geral não cria um problema

#### Variáveis de Classificação Ex: Escolaridade
Vamos supor que exista essas escoláridades:
|Sigla|Escolaridade|
|-----|------------|
|S|Superior|
|SI|Superior Incompleto|
|M|Medio|
|MI|Medio Incompleto|
|F|Fundamental|
|FI|Fundamental Incompleto|

E que possuimos uma tabela com uma coluna de escolaridade, o que fariamos para trartar isso seria usar o ***OneHot encoding*** Transformando Cada Nivel em uma váriavel separada:
| Nome    | Escolaridade | E_F | E_M | E_MI | E_S |
| ------- | ------------ | --- | --- | ---- | --- |
| Ana     | S            | 0   | 0   | 0    | 1   |
| Carlos  | M            | 0   | 1   | 0    | 0   |
| Beatriz | M            | 0   | 1   | 0    | 0   |
| João    | F            | 1   | 0   | 0    | 0   |
| Maria   | S            | 0   | 0   | 0    | 1   |
| Pedro   | MI           | 0   | 0   | 1    | 0   |
| Lucas   | M            | 0   | 1   | 0    | 0   |
| Júlia   | S            | 0   | 0   | 0    | 1   |

Mas qual o problema disso? Pode acontecer de isso se tornar uma tabela gigante. Para solucionar isso temos outra possibilidade, que é usar o ***Mean encoder***. Que se basea em fazer uma média da váriavel resposta de Cada Nível, e substituir os Nìveis por essa Média:

| Escolaridade | Média_Nota |
| ------------ | ---------- |
| F            | 4.0        |
| M            | 6.0        |
| MI           | 7.0        |
| S            | 9.0        |

| Nome    | Escolaridade |
| ------- | ------------ |
| Ana     | 0,90         |
| Carlos  | 0,60         |
| Beatriz | 0,60         |
| João    | 0,40         |
| Maria   | 0,90         |
| Pedro   | 0,70         |
| Lucas   | 0,60         |
| Júlia   | 0,90         |

Por ultimo podemos também usar o ***OneHot encoding*** porem, agrupar os níveis. Como exemplo: "Em vez de separa cada estado, Vamos agrupa-los em regiões: sul, sudeste, etc."