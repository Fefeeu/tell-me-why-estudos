# %%
import pandas as pd

df = pd.read_excel("../data/dados_cerveja_nota.xlsx")
df.head()

# %%
from sklearn import linear_model
from sklearn import tree

X = df[['cerveja']] # X maiusculo sempre é uma matriz (dataframe)
y = df['nota']      # y minusculo sempre é um vetor (séries)

# %%
#########################################################################


    # ISSO AQUI É O APRENDIZADO DE MAQUINA

regrecao = linear_model.LinearRegression()
regrecao.fit(X=X, y=y)




#########################################################################

# %%
a, b = regrecao.intercept_, regrecao.coef_[0]
print(f'Y = {a} + {b}X')

# %%
import matplotlib.pyplot as plt

predict_reg = regrecao.predict(X.drop_duplicates())

arvore_full = tree.DecisionTreeRegressor(random_state=42)
arvore_full.fit(X, y)
predict_arvore_full = arvore_full.predict(X.drop_duplicates())

max_depth = 2
# O NUMERO DE MEDIAS É = 2^max_depth ISSO PARA UMA ARVORE SIMÉTRIA

arvore_d2 = tree.DecisionTreeRegressor(random_state=42, max_depth=max_depth)
arvore_d2.fit(X, y)
predict_arvore_d2 = arvore_d2.predict(X.drop_duplicates())

plt.plot(X['cerveja'], y, "o")
plt.grid(True)
plt.title("Relacao Cerveja vs Nota")
plt.xlabel("N° Cervejas")
plt.ylabel("Nota Tirada")

plt.plot(X.drop_duplicates()['cerveja'], predict_reg, color='red')

plt.plot(X.drop_duplicates()['cerveja'], predict_arvore_full, color='green')

plt.plot(X.drop_duplicates()['cerveja'], predict_arvore_d2, color='magenta')

plt.legend(['Observado', 
            f'Y = {a:.3f} + {b:.3f}X',
            'Arvore Full',
            f'Arvore Depth = {max_depth}'
            ])

# %%

# SE QUISER VER, MUDE O max_depth
plt.figure(dpi=400)

tree.plot_tree(arvore_d2,
               feature_names=["cerveja"],
               filled=True)
# %%
