# %%
import pandas as pd

df_exemplo = pd.DataFrame(
    {
        "nome":["teo", "lara", "nana", "bia", "mah", "lara", "mah", "mah"],
        "sobrenome": ["calvo", "calvo", "ataide", "ataide", "ataide", "silva", "silva", "silva"]
    }
)

df_exemplo

# %% MANTEM A PRIMEIRA DUPLICATA
df_exemplo.drop_duplicates()

# %% MANTEM A ULTIMA DUPLICATA
df_exemplo.drop_duplicates(keep="last")

# %%
df_exemplo = pd.DataFrame(
    {
        "nome":["teo", "lara", "nana", "bia", "mah", "lara", "mah", "mah"],
        "sobrenome": ["calvo", "calvo", "ataide", "ataide", "ataide", "silva", "silva", "silva"],
        "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134]
    }
)

df_exemplo.drop_duplicates() # nao vai dropar nenhuma

# %% REMOVENDO DUPLICATAS POR COLUNA
df_exemplo.drop_duplicates(subset=["nome", "sobrenome"])

# %% exemplo: MANTENDO O MAIOR SALARIO
df_exemplo = (df_exemplo.sort_values("salario", ascending=False)
                        .drop_duplicates(subset=["nome", "sobrenome"]))

df_exemplo