# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%
df.shape 

# %%
df.info(memory_usage='deep')

# %% renomear colunas
# a chave do dicionario eh o nome antigo, e o valor eh o nome novo
renamed_columns = {
    "IdTransacao": "id_da_transacao",
    "IdCliente": "id_do_cliente"
}

# cria um novo dataframe
df_renomeado = df.rename(columns=renamed_columns)

# renomea no proprio dataframe
# df_renomeado = df.rename(columns=renamed_columns, inplace=True)

# %% lendo somente 2 ou mais colunas
colunas = ["id_do_cliente", "QtdePontos"]

df_renomeado[colunas]

# %% organizando colunas
df_colunas_reorganizadas = df[["IdCliente", "QtdePontos", "DescSistemaOrigem", "DtCriacao", "IdTransacao"]]
df_colunas_reorganizadas

# %% reorganizando em ordem alfabetica
colunas_alfabetica = df.columns.tolist()
colunas_alfabetica.sort()
colunas_alfabetica

df_colunas_reorganizadas = df[colunas_alfabetica]
df_colunas_reorganizadas