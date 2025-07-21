# %%
import pandas as pd

df = pd.read_csv("../09_concat/25_homicidios_consolidados.csv", sep=";")
df.head(10)

# %%
df_stack = (df.set_index(["nome", "período"])
   .stack()
   .reset_index()
 )

df_stack.columns = ["nome", "periodo", "metrica", "valor"]

df_stack

# %%
(df_stack.pivot_table(values="valor", 
                     index=["nome", "periodo"], 
                     columns="metrica")
         .reset_index())

# %% esta sendo feita a media na linha <nome>, nesse caso, eu sumo com a coluna <periodo>
df_stack.pivot_table(values="valor",
                     index=["nome"],
                     columns="metrica",
                     aggfunc="mean")