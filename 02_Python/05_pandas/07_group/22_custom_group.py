# %%
import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head(10)

# %% METODO TIRADO DO CU QUE VAI SER CRIADO
def diff_amp(x:pd.Series):
    amplitude = x.max() - x.min()
    mean = x.mean()
    return np.sqrt((amplitude - mean) ** 2)

# %%
idades = [32, 44, 12, 54, 67, 32, 23, 34, 32, 12, 45, 43, 28, 73, 29]
idades = pd.Series(idades)
diff_amp(idades)

# %%
(transacoes.groupby(by=["IdCliente"])
            .agg({
                "IdTransacao": ['count'],
                "QtdePontos": ['sum', 'mean', diff_amp]
            })
)