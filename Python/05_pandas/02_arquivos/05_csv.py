# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df

# %% salva adicionando mais uma coluna a do index
df.to_csv("05_clientes(copia).csv", sep=";")

# %% agora salva sem a coluna do index
df.to_csv("05_clientes(copia).csv", sep=";", index=False)

# %% Obs.: eh um arquivo binaria
df.to_parquet("05_clientes(copia).parquet", index=False)

df_2 = pd.read_parquet("05_clientes(copia).parquet")
df_2

# %% EXCEL, tbm binario

df.to_excel("05_clientes(copia).xlsx", index=False)
df_3 = pd.read_excel("05_clientes(copia).xlsx")

df_3