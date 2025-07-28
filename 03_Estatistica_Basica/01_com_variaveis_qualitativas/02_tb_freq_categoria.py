# %%
import pandas as pd 

df = pd.read_csv("../data/points_tmw - dados origem.csv")
df.head()

# %%
tabela_categoria = (df.groupby(by=["descCategoriaProduto"])[["idTransacao"]]
                      .count()
                      .rename(columns={"idTransacao": "Freq. Abs."}))

tabela_categoria["Freq. Abs. Acum."] = tabela_categoria["Freq. Abs."].cumsum()
tabela_categoria["Freq. Rel."] = tabela_categoria["Freq. Abs."] / tabela_categoria["Freq. Abs."].sum()
tabela_categoria["Freq. Rel. Acum."] = tabela_categoria["Freq. Rel."].cumsum()

tabela_categoria