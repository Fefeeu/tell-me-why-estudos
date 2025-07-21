# %%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=";")

df.head()

# %% produtos nas linhas e criando nova coluna

df["Pontos_100"] = df["QtdePontos"] + 100

df.head()

# %% operacao entre series

df["email_ou_twitch"] = df["FlEmail"] + df["FlTwitch"]

df["email_e_twitch"] = df["FlEmail"] * df["FlTwitch"]

df.head()

# %%
filtro_email_e_twitch = (df["FlEmail"] == 1) & (df["FlTwitch"] == 1)

df[filtro_email_e_twitch] 

# %%
df["log_pontos"] = np.log(df["QtdePontos"] + 1)

# %% usando matplotlib
import matplotlib.pyplot as plt

plt.hist(df["log_pontos"])
plt.grid(True)
plt.show()