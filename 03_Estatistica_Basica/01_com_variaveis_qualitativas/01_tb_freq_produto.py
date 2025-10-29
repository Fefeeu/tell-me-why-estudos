# %%
import pandas as pd

df = pd.read_csv("../data/points_tmw.csv", sep=";")
df.head()

# %% 2 opcoes
freq_produto = pd.DataFrame(pd.Series(df["descProduto"]).value_counts())
freq_produto
# %% 2 opcoes (o jeito que ta o codigo, eu to usando esse )
freq_produto = (df.groupby(["descProduto"])[["idTransacao"]]
                 .count())
freq_produto

# %% fazendo frequencia acumulada
freq_produto["Freq. Absoluta"] = freq_produto["idTransacao"]

freq_produto["Freq. Abs. Acum."] = freq_produto["Freq. Absoluta"].cumsum()

freq_produto["Freq. Relativa"] = freq_produto["Freq. Absoluta"] / freq_produto["Freq. Absoluta"].sum()

freq_produto["Freq. Rel. Acum."] = freq_produto["Freq. Relativa"].cumsum()

freq_produto
# %%
