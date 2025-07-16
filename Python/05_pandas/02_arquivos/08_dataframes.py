# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")

df_clientes

# %% soh mostra as 5 primeiras linhas do dataframe
df_clientes.head()

# %% n numeros de colunas
df_clientes.head(10)

# %% o oposto do head
df_clientes.tail()

# %%
df_clientes.tail(10)

# %% valores aleatorios
df_clientes.sample()

# %%
df_clientes.sample(10)

# %%
df_clientes.shape

# %%
df_clientes.columns

# %% Obs: o stop nao esta incluso nos index
df_clientes.index

# %% Obs.: memory usage, eh uma estimativa do quanto de ram que esta usando
# Obs2.: formato de string
df_clientes.info()

# %% Obs.: agora o memory usage esta preciso
# CARAI EH MUITO DIFERENTE OS VALORES
df_clientes.info(memory_usage='deep')

# %% uma serie com o tipo de cada coluna
df_clientes.dtypes