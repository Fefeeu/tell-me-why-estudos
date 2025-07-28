# %%
import pandas as pd

df = pd.read_excel("../data/dados_frutas.xlsx")
df

# %%
from sklearn import tree

arvore = tree.DecisionTreeClassifier(random_state=42)
# random_state é a seed do RNG
# %%
y = df["Fruta"]

caracteristicas = ['Arredondada', 'Suculenta', 'Vermelha', 'Doce']
X = df[caracteristicas]

# %%

# ISSO AQUI QUE É MACHINE LEARNING

# fit = ajuste
arvore.fit(X, y)

# %%        'Arredondada', 'Suculenta', 'Vermelha', 'Doce'
arvore.predict([[0,0,0,0]])

# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(arvore,
               feature_names=caracteristicas,
               class_names=arvore.classes_,
               filled=True)

# %%
probabilidade = arvore.predict_proba([[1,1,1,1]])[0]
pd.Series(probabilidade, index=arvore.classes_)
# %%
