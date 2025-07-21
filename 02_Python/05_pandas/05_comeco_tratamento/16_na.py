# %%
import pandas as pd

clientes = pd.read_csv("16_clientes_NaN.csv", sep=";")

clientes.head(20)

# %% 1 opicao: ACABAR COM TODOS OS NA

clientes = clientes.dropna() # retira todos que tem pelo menos 1 na
# clientes.dropna(how="any")

clientes

# %% 2 opcao: ACABAR SOH COM AS LINHAS QUE SAO INTEIRAS NA
clientes.dropna(how="all")

# %%

df_exemplo = pd.DataFrame(
    {
        "nome": ["fefe", None, "bia", "chokito", None],
        "idade": [20, None, 22, None, None],
        "salario": [2000, 1000, None, 3000, None]
    }
)

print(df_exemplo)
print()

print(df_exemplo.dropna())
print()

print(df_exemplo.dropna(how="all"))
print()

# %%
df_exemplo = pd.DataFrame(
    {
        "nome": ["fefe", None, "bia", "chokito", None],
        "idade": [20, None, 22, None, None],
        "salario": [2000, 1000, None, 3000, None]
    }
)

df_exemplo.dropna(how="all", subset=["idade", "nome"]) # os 2 tem que ser Nan
# %%
df_exemplo.dropna(how="any", subset=["idade", "nome"])

# %% 3 opcao: COMPLETAR COM VALORES

df_exemplo = pd.DataFrame(
    {
        "nome": ["fefe", None, "bia", "chokito", None],
        "idade": [20, None, 22, None, None],
        "salario": [2000, 1000, None, 3000, None]
    }
)

df_exemplo["idade"] = df_exemplo["idade"].fillna(0)

df_exemplo