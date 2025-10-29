# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes.head(10)

# %% somar pontos por cliente
transacoes.groupby(by=["IdCliente"])["QtdePontos"].count()

# %% contando quantidade de transacoes
transacoes.groupby(by=["IdCliente"])["IdTransacao"].count()

# %%
transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count()

# %% mais de uma estatistica
# Obs1.: pode ser agg, ou, agregate
# Obs2.: as_index=False, diz que o by=["IdCliente"], nao eh o index, assim criando um index numerico padrao
summary = transacoes.groupby(by=["IdCliente"], as_index=False).agg(
    {
        "IdTransacao":['count'],
        "QtdePontos":['sum', 'mean']
    }
)

summary

# %% um dataframe de MultiIndex
# DE A CORDO COM O TEO: "EH CHATO PRA CARALHO"
summary.columns

# %%
summary["QtdePontos"]

# %%
summary[[("QtdePontos", "mean")]]

# %% PARA TRABALHAR COM ISSO, O TEO PREFERE CHUMBAR OS NOMES DO JEITO QUE ELE QUER
summary.columns = ["idCliente", "quantidadeDeTransacoes", "totalPontos", "avgPontos"]
summary