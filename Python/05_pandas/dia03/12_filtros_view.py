# %%
# quando criamos uma tabela com o filtro (exemplo: clientes_0) o que estamos
# fazendo na verdade eh criando uma variavel que aponta somente para as linhas
# correspondentes do filtro em questao, ou seja
# SOH EXISTE UMA TABELA, E A "tabela nova", SOH APONTA PARA A TABELA QUE JA EXISTE

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

filtro = clientes["QtdePontos"] == 0

clientes_0 = clientes[filtro]

# vai receber um aviso, pois eh a maneira "incorreta"
clientes_0["coluna_ extra"] = 1

clientes_0

# %%
filtro = clientes["QtdePontos"] == 0

clientes_0 = clientes[filtro].copy()

clientes_0["coluna_extra"] = 1

clientes_0