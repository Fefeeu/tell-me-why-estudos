
# %%
import pandas as pd

idades = [
    20, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

nomes = [
    "FEFE", "Vini", "Bia", "Mile", "Tales",
    "Mathias", "Chokito", "FEFE", "Joao Paulo", "Pedro Dias",
    "Maria Laura", "Maria Rita", "Komuna", "John", "FEFE"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

dataframe = pd.DataFrame()

dataframe["idades"] = series_idades
dataframe["nomes"] = series_nomes

# %%
dataframe["nomes"]

# %%
dataframe.iloc[0] # retorna uma serie com os index sendo o nome da coluna

# %%
print(dataframe.iloc[0]["nomes"])
print(dataframe.iloc[0]["idades"])