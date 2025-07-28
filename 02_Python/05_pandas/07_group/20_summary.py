# %% 
import pandas as pd

idades = [32, 44, 12, 54, 67, 32, 23, 34, 32, 12, 45, 43, 28, 73, 29]

idades = pd.Series(idades)

idades

idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe()

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head(10)

# %% quantidade de pessoas com a twitch
clientes["FlTwitch"].sum()

# %% porcentagem de pessoas com a twitch
clientes["FlTwitch"].mean()

# %% porcentagens das redes sociais
redes = ["FlEmail", "FlTwitch", "FlYouTube", "FlBlueSky", "FlInstagram"]
clientes[redes].mean()

# %% media soh de colunas numericas
filtro_object = clientes.dtypes == "object"

colunas_numericas = clientes.dtypes[~filtro_object].index.tolist()

clientes[colunas_numericas].mean()

# %%
clientes[colunas_numericas].describe()