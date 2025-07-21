# %% 05.05 - Selecionando a primeira transacao diaria de cada cliente
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

def rejex_data(date:str):
    new_date = date.split(" ")[0]
    return new_date

transacoes = transacoes.sort_values("DtCriacao")

transacoes["data"] = transacoes["DtCriacao"].apply(rejex_data)

transacoes = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])

transacoes

# %%
 