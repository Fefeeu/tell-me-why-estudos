# %%
import pandas as pd

df_geral = pd.read_csv("../data/ipea/homicidios.csv", sep=";")

df_geral = df_geral.rename(columns={"valor":"homicidios"})

df_geral.head()

# %%
df_negros = pd.read_csv("../data/ipea/homicidios-negros.csv", sep=";")

df_negros = df_negros.rename(columns={"valor": "homicidios-negros"})

df_negros

# %%
df_geral = df_geral.set_index(["nome", "período"])
df_negros = df_negros.set_index(["nome", "período"])

# %%
pd.concat([df_geral, df_negros], axis=1)

###############################################################################################################################################

# %%
import pandas as pd
import os

def read_file(nome_arquivo:str):
    df = (pd.read_csv(F"../data/ipea/{nome_arquivo}.csv", sep=";")
            .rename(columns={"valor": nome_arquivo})
            .set_index(["nome", "período"])
            .drop(["cod"], axis=1)
        )
    return df
    
arquivos_homicidios = os.listdir("../data/ipea")

dfs = []
for arquivo_homicidio in arquivos_homicidios:
    file_name = arquivo_homicidio.split(".")[0]
    dfs.append(read_file(file_name))

df_full = (pd.concat(dfs, axis=1)
           .reset_index()
           .sort_values(["período", "nome"]))

df_full.to_csv("25_homicidios_consolidados.csv", index=False, sep=";")

df_full