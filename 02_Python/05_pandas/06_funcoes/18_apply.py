# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head(10)

# %% PEGANDO A ULTIMA PARTE DO ID

def get_last_id(id:str):
    return id.split("-")[-1]

# %%
get_last_id("0097ab76-4637-4ece-8ebc-ab6abd61d662")

# %%
clientes["IdCliente"].apply(get_last_id)