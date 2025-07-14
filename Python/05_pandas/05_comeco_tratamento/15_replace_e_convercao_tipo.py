# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

df.head()

# %%
df["QtdePontos"] # a serie eh do tipo int64 vulgo int

# %% convertendo
df["QtdePontos"].astype(float)

# %%
df["QtdePontos"] = df["QtdePontos"].astype(float)

df.head()

# %% convertendo datas
print(type(df["DtCriacao"][0]))

# df["DtCriacao"] = pd.to_datetime(df["DtCriacao"]) # rodar essa linha vai dar um erro por conta do formato da data

# %% o replace troca o valor antigo pelo novo, pelo esquema de dicionario
# {chave:valor} = {valor_antigo:valor_novo}

replace = {"2024-02-01 00:00:00 +0000 UTC": "2024-02-01 09:00:00 +0000 UTC"}

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))

# DEU PROBLEMA PQ O FORMATO TA OUTRO DIFERENTE DO datetime
