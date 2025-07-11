# %% calculando media e variancia por meio de listas

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

media = sum(idades)/len(idades)

diffs = 0
for i in idades:
    diffs += (i-media)**2

variancia = diffs / (len(idades) - 1)

# %% usando series
import pandas as pd

series_idades = pd.Series(idades) # criando uma serie vazia

# os valores dentro de uma serie sempre serao 1 soh
print(series_idades)

# %% estatisticas por series

media_idades = series_idades.mean()

var_idades = series_idades.var()

summary_idades = series_idades.describe()

summary_idades