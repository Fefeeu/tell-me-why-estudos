# %%
import pandas as pd

df_01 = pd.DataFrame({
    "cliente": [1, 2, 3, 4, 5],
    "nome": ["teo", "jose", "nah", "mah", "lah"]
})

df_02 = pd.DataFrame({
    "cliente": [6, 7, 8],
    "nome": ["kozato", "laura", "dan"],
    "idade": [32, 29, 31]
})

df_03 = pd.DataFrame(
    {
        "idade": [32, 32, 19, 54, 33]
    }
)

# %% JUNTANDO COM LINHAS
pd.concat([df_01, df_02])

# %%
pd.concat([df_01, df_02], ignore_index=True)

# %%
pd.concat([df_01, df_03])

# %% JUNTANDO COM COLUNAS
pd.concat([df_01, df_03], axis=1)

# %% DA A MESMA COISA QUE O DE CIMA, JA QUE ELE USA O index PARA FAZER A CONCATENACAO
df_03 = df_03.sort_values(by='idade')
pd.concat([df_01, df_03], axis=1)

# %% assim eh se eu nao quiser que seja pelo index, mas sim pela "ordem"
df_03 = df_03.sort_values(by='idade').reset_index()
pd.concat([df_01, df_03], axis=1)
