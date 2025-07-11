# %%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")

df

# %%
filtro = (df["IdProduto"] == 5) | (df["IdProduto"] == 11)

df[filtro]

# %%
filtro = df["IdProduto"].isin([5,11])
filtro

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
filtro = clientes["DtCriacao"].notnull()

clientes[filtro]

# %%
filtro_1 = clientes["DtCriacao"].notna()
filtro_2 = ~clientes["DtCriacao"].isna()
