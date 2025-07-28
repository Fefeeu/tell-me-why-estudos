# %%
import pandas as pd

df = pd.read_excel("../../data/dados_cerveja_nota.xlsx")
df.head()

# %%
from sklearn import linear_model

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

predict = regrecao.predict(X.drop_duplicates())
predict

plt.plot(X['cerveja'], y, "o")
plt.grid(True)
plt.title("Relacao Cerveja vs Nota")
plt.xlabel("N° Cervejas")
plt.ylabel("Nota Tirada")

plt.plot(X.drop_duplicates()['cerveja'], predict)

plt.legend(['Observado', f'Y = {a:.3f} + {b:.3f}X'])

# %%
