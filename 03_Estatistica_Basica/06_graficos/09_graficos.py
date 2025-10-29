# %%
import pandas as pd
import matplotlib.pyplot as plt
# TEM VARIAS BIBLIOTECAS DE GRAFICO LEGAIS, COMO:
# - matplotlib
# - seaborn
# - bokeh (graficos interativos ?)

import seaborn as sns

df = pd.read_csv("../data/points_tmw.csv", sep=";")
df.head()

# %%

group_produto = (df.groupby(["descProduto"])["idTransacao"]
                  .count()
                  .reset_index()
                  .sort_values(by="idTransacao")
)

plt.bar(group_produto["descProduto"], group_produto["idTransacao"])
plt.show()

# %%
sns.barplot(group_produto, y="descProduto", x="idTransacao")
plt.xlabel("Quantidade de Transacoes")
plt.ylabel("Produto")
plt.title("FREQUENCIA DE PRODUTOS")

plt.savefig('09_zgrafico_produtos', 
            bbox_inches='tight',  # Impede corte dos elementos
            dpi=300,  # Aumenta a resolução
            pad_inches=0.5)  # Espaço extra ao redor

# %%
df["DataTransacao"] = pd.to_datetime(df["dtTransacao"]).dt.date

group_data = df.groupby("DataTransacao").agg(
    {
        "qtdPontos": "sum",
        "idTransacao": "count"
    }
).reset_index()

group_data = group_data.sort_values(by="DataTransacao")

plt.figure(figsize=(8,6))
plt.plot(group_data["DataTransacao"], group_data["idTransacao"])
plt.ylabel("Quantidade Transacoes")
plt.title("Serie Historica de Transacoes")

# %%
plt.hist(group_data["qtdPontos"], bins=18, density=False)
plt.xlabel("Pontos")
plt.show()

# %% 
plt.boxplot(group_data["qtdPontos"])
plt.title("Box-Plot")
plt.ylabel("Pontos")

# %% boxplot que nao vai dizer nada
plt.boxplot(df["qtdPontos"])
plt.title("Box-Plot")
plt.ylabel("Pontos")

# %% diz mais para gente
group_pontos = (df.groupby(by="qtdPontos")
                  .count()
                  .reset_index())
sns.barplot(group_pontos, x="qtdPontos", y="idTransacao")
plt.show()

# %% associacao
sns.scatterplot(group_data, x="qtdPontos", y="idTransacao")
