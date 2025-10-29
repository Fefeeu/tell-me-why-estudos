# %%
import pandas as pd

df = pd.read_csv("../09_concat/25_homicidios_consolidados.csv", sep=";")

df.head(10)

# %% AS COLUNAS SE TORNARAO LINHA, OU SEJA O <nome-coluna> VAI SE TORNAR UMA PROPRIEDADE DA LINHA
# assim a tabela "guanha" a proriedade de ter uma quantidade de colunas definidas
# ou seja, se eu precisar add uma coluna, vai na verdade mudar o numero de linhas, aumentando assim
# sempre soh uma dimencao da tabela

df = df.set_index(["nome", "período"])
df_stack = df.stack()  # transforma em uma Serie
df_stack

# %% para transformar em DataFrame
df_stack = df_stack.reset_index()
df_stack.columns = ["nome", "periodo", "metrica", "valor"]
df_stack

# %% retornando para antes do stack()
# OBS.: O unstack() NAO EH MUITO USADO, O MAIS USADO EH pivo()
df_unstack = df_stack.set_index(["nome", "periodo", "metrica"]).unstack()
df_unstack = df_unstack.reset_index()

# %%
metricas = df_unstack.columns.droplevel(0)[2:].tolist()
df_unstack.columns = ["nome", "periodo"] + metricas
df_unstack