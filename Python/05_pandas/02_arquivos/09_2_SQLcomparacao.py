# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %% SELECT * FORM df
df

# %% SELECT dCliente FROM df
df[["IdCliente"]]

# %% SELECT * FROM df LIMIT 5
df.head(5)

# %% SELECT IdCliente, QtdePontos FROM df LIMIT 5
df[["IdCliente", "QtdePontos"]].head(5)

# %% SELECT IdCliente, IdTransacao, QtdePontos
# FROM df
# LIMIT 5
