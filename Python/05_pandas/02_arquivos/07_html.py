# %%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

dfs = pd.read_html(url)

print("numero de dataframes:",len(dfs))

# %%
df_uf = dfs[1]
print(df_uf)

df_uf.to_csv("07_wikipedia(copia).csv", sep=";", index=False)