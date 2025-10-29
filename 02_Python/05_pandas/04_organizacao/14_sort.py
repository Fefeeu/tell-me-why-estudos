# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %% ordenando serie quantidade de pontos

clientes["QtdePontos"].sort_values()

# %% ordenando um dataframe pela quantidade de pontos
# Obs.: retorna um dataframe novo
clientes.sort_values(by="QtdePontos", ascending=False) # ascending invert a ordem

# %% empate no salario, desempate pela idade
exemplo_clientes_empate = pd.DataFrame(
    {
        "nome": ["fefe", "vini", "bia", "chokito"],
        "idade": [20, 21, 22, 23],
        "salario": [2000, 1000, 2000, 3000]
    }
)

# primeiro ordena pelo sarario, depois pela idade
exemplo_clientes_empate.sort_values(by=["salario", "idade"], ascending=[False, True])