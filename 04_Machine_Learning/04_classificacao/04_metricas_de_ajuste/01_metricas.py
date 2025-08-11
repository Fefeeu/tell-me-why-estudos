# %%
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1YQBQ3bu1TCmgrRch1gzW5O4Jgc8huzUSr7VUkxg0KIw/export?gid=283387421&format=csv"

df = pd.read_csv(url)
df.head()

# %%
df = df.replace({"Sim":1, "Não":0})
df.head()

# %%    ELE SUBISTITUI CADA LINHA REPETIDA POR UMA COLUNA BOLEANA
pd.get_dummies(df[['Como conheceu o Téo Me Why?']])

# %%
num_vars = [
    'Curte games?',
    'Curte futebol?',
    'Curte livros?',
    'Curte jogos de tabuleiro?',
    'Curte jogos de fórmula 1?',
    'Curte jogos de MMA?',
    'Idade'
]

dummy_vars = [
    'Como conheceu o Téo Me Why?',
    'Quantos cursos acompanhou do Téo Me Why?',
    'Estado que mora atualmente',
    'Área de Formação',
    'Tempo que atua na área de dados',
    'Posição da cadeira (senioridade)'
]

df_analise = pd.get_dummies(df[dummy_vars]).astype(int)
df_analise[num_vars] = df[num_vars]
df_analise

# %%
df_analise["pessoa feliz"] = df['Você se considera uma pessoa feliz?'].copy()
df_analise

# %%
feature = df_analise.columns[:-1]
feature

# %%

X = df_analise[feature]
y = df_analise['pessoa feliz']

from sklearn import tree
from sklearn import naive_bayes
from sklearn import linear_model

arvore = tree.DecisionTreeClassifier(random_state=42,
                                     min_samples_leaf=5) # na minha folha final deve ter no minimo 5 amostras

arvore.fit(X, y)

naive = naive_bayes.GaussianNB()
naive.fit(X, y)

reg = linear_model.LogisticRegression(penalty=None, fit_intercept=True)
reg.fit(X, y)


# %%

arvore_predic = arvore.predict(X)
arvore_predic

# %%
df_predict = df_analise[['pessoa feliz']].copy()

df_predict['predict_arvora (o que a arvore espera)'] = arvore_predic
df_predict['predict_naive'] = naive.predict(X)
df_predict['predict_reg'] = reg.predict(X)

df_predict

# %%

df_predict['proba_arvore'] = arvore.predict_proba(X)[:,1]
df_predict['proba_naive'] = naive.predict_proba(X)[:,1]
df_predict['proba_reg'] = reg.predict_proba(X)[:,1]

df_predict


# %% Acurácia
float((df_predict['pessoa feliz'] == df_predict['predict_arvora (o que a arvore espera)']).mean())

# %% MATRIZ DE CONFISÃO
pd.crosstab(df_predict['pessoa feliz'], df_predict['predict_arvora (o que a arvore espera)'])

# %%
df_predict.to_csv("01_predict.csv", sep=';', index=False)

# %%
from sklearn import metrics

acc_arvore = metrics.accuracy_score(y_true=df_predict['pessoa feliz'], y_pred=df_predict['predict_arvora (o que a arvore espera)'])
precisao_arvore = metrics.precision_score(y_true=df_predict['pessoa feliz'], y_pred=df_predict['predict_arvora (o que a arvore espera)'])
recall_arvore = metrics.recall_score(y_true=df_predict['pessoa feliz'], y_pred=df_predict['predict_arvora (o que a arvore espera)'])
# NÃO TEM ESPECIFICIDADE ?
roc_arvore = metrics.roc_curve(y_true=df_predict['pessoa feliz'], y_score=df_predict['proba_arvore'])
aoc_arvore = metrics.roc_auc_score(y_true=df_predict['pessoa feliz'], y_score=df_predict['proba_arvore'])
aoc_arvore

acc_naive = metrics.accuracy_score(y_true=df_predict['pessoa feliz'], y_pred=df_predict['predict_naive'])
precisao_naive = metrics.precision_score(y_true=df_predict['pessoa feliz'], y_pred=df_predict['predict_naive'])
recall_naive = metrics.recall_score(y_true=df_predict['pessoa feliz'], y_pred=df_predict['predict_naive'])
roc_naive = metrics.roc_curve(y_true=df_predict['pessoa feliz'], y_score=df_predict['proba_naive'])
aoc_naive = metrics.roc_auc_score(y_true=df_predict['pessoa feliz'], y_score=df_predict['proba_naive'])
aoc_naive

acc_reg = metrics.accuracy_score(y_true=df_predict['pessoa feliz'], y_pred=df_predict['predict_reg'])
precisao_reg = metrics.precision_score(y_true=df_predict['pessoa feliz'], y_pred=df_predict['predict_reg'])
recall_reg = metrics.recall_score(y_true=df_predict['pessoa feliz'], y_pred=df_predict['predict_reg'])
roc_reg = metrics.roc_curve(y_true=df_predict['pessoa feliz'], y_score=df_predict['proba_reg'])
aoc_reg = metrics.roc_auc_score(y_true=df_predict['pessoa feliz'], y_score=df_predict['proba_reg'])
aoc_reg

# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400)

plt.plot(roc_arvore[0], roc_arvore[1], 'o-')
plt.plot(roc_naive[0], roc_naive[1])
plt.plot(roc_reg[0], roc_reg[1])
plt.grid(True)
plt.title("ROC Curve")
plt.xlabel("(1 - Especificidade)")
plt.ylabel("Recall")

plt.legend([f"Arvore: {aoc_arvore:.2f}",
            f"Naive: {aoc_naive:.2f}",
            f"Reg: {aoc_reg:.2f}"])

# %%
plt.hist(df_predict['proba_arvore'])
# %%

pd.Series({"model":reg, "features":feature}).to_pickle("01_model_feliz.pkl")
# %%
df_analise.columns
# %%
