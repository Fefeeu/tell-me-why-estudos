# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

series_idades = pd.Series(idades)

# %%

# os indices de uma series funcionam como as chaves de um dicionario
series_idades[0]

# %%

series_idades = series_idades.sort_values()
print(series_idades)
print()

# iloc, significa agora que eu estou tratando de posicao e nao mais de index
print(series_idades.iloc[0])
print()

print(series_idades.iloc[:3])

# %%

idades = [
    20, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

index = [
    "FEFE", "Vini", "Bia", "Mile", "Tales",
    "Mathias", "Chokito", "FEFE", "Joao Paulo", "Pedro Dias",
    "Maria Laura", "Maria Rita", "Komuna", "John", "FEFE"
]

series_idades = pd.Series(idades, index=index)

print(series_idades)
print()

# OBS.: series_idades["FEFE"] = series_idades.loc["FEFE"]
# loc  = navegar nos index
# iloc = navegar nas posicoes 
print(series_idades.loc["FEFE"])
print()

print(series_idades.iloc[0])