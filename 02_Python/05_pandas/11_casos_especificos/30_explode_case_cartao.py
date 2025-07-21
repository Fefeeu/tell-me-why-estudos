# %%
import pandas as pd

df = pd.read_csv("30_dados_cartao.csv", sep=";")

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])
df["valorParcela"] = df["vlVenda"] / df["qtParcelas"]

# %%
df["vlParcelaUnica"] = df.apply(lambda row: [row["valorParcela"]] * row["qtParcelas"], axis=1)
df.explode("vlParcelaUnica")

# %% um melhor obs.: nao ta fazendo exatamente a mesma coisa
import pandas as pd

df = pd.read_csv("30_dados_cartao.csv", sep=";")

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])
df["valorParcela"] = df["vlVenda"] / df["qtParcelas"]

df["ordemParcela"] = df.apply(lambda row: [i for i in range(row["qtParcelas"])], axis=1)
df_explode = df.explode("ordemParcela")

def calcDtParcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])
    dt = f"{dt.year}-{dt.month}"
    return dt

df_explode["dtParcela"] = df_explode.apply(calcDtParcela, axis=1)
df_explode

# %% qualculo do que deve ser pago em cada mes por cada cliente
(df_explode.groupby(by=["idCliente", "dtParcela"])
            ["valorParcela"].sum()
            .reset_index()
 )