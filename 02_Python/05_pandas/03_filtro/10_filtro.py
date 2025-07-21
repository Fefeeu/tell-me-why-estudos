# %%
df_exemplo = pd.DataFrame(
    {
        "nome": ["Fefe", "Vini", "Bia"],
        "idade": [20 , 15, 50],
        "cidade": ["guaxupe", "itajuba", "sao paulo"]
    }
)

filtro = df_exemplo["idade"] >= 18
print(filtro, "\n")

df_exemplo_filtrado = df_exemplo[filtro]
df_exemplo_filtrado

# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")

# %% valores entre 50 e 100
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] <= 100)

df[filtro]


# %% valores iguais a 1 ou maiores que 100
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] > 100)

df[filtro]

# %%
filtro = ((df["QtdePontos"] < 50) | (df["QtdePontos"] > 100)) & (df["DtCriacao"] >= '2025-01-01')

df[filtro]