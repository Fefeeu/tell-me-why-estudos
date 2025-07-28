# %% 06.04 - Quem teve mais transacao de streak
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
transacao_produto.head()

# %%
produtos = pd.read_csv("../data/produtos.csv", sep=";")
produtos

# %% CAMINHO MAIS BASICO
cliente_transacao_produto = transacoes.merge(
    transacao_produto, 
    on=["IdTransacao"]
)

cliente_transacao_produto = cliente_transacao_produto[["IdCliente", "IdTransacao", "IdProduto"]]

df_full = cliente_transacao_produto.merge(produtos, on="IdProduto")

df_full = df_full[df_full["DescProduto"] == "Presença Streak"]

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
                .count()
                .sort_values(ascending=False)
                .head(1)
)

# %% UMA MANEIRA MAIS AVANCADA, SOH DE EXEMPLO, E ELA EH MAIS PERFORMATICA
produtos = produtos[produtos["DescProduto"] == "Presença Streak"]

(transacoes.merge(transacao_produto, on="IdTransacao", how="left")
    .merge(produtos, on=["IdProduto"], how="right")
    .groupby(by=["IdCliente"])["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)