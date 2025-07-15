# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %% trasaendo para transacoes as infos do cliente
# Obs.: IdCliente eh uma chave extrangeira
transacoes.merge(
    right=clientes, # OBS.: transacoes = esquerda, clientes = direita
    how='left', # como que fara a juncao, tipo ("soh infos que batem ou info dos dois completos")
    on=["IdCliente"], # qual criterio de juncao
    suffixes=["_Transacao", "_Cliente"]
)

# %%
df_1 = pd.DataFrame({
    "transacao": [1, 2, 3, 4, 5],
    "idCliente": [1, 2, 3, 2, 2],
    "valor": [10, 45, 32, 17, 87],
})

df_2 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nome": ["teo", "nah", "mah", "jose"],
})

df_1.merge(
    right=df_2, 
    left_on=["idCliente"], 
    right_on=["id"]
)