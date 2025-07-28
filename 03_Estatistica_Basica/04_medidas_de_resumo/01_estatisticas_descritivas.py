# %%
import pandas as pd

df = pd.read_csv("../data/points_tmw.csv", sep=";")
df.head()

# %%
print("Estatisticas de Posicao Para Transacoes:")

media = df["qtdPontos"].mean()
print("Media:", media)

minimo = df["qtdPontos"].min()
print("Minimo:", minimo)

quartil_1 = df["qtdPontos"].quantile(0.25)
print("1o Quartil:", quartil_1)

mediana = df["qtdPontos"].median()
print("Mediana:", mediana)

quartil_3 = df["qtdPontos"].quantile(0.75)
print("3o Quartil:", quartil_3)

maximo  = df["qtdPontos"].max()
print("Maximo:", maximo)

variancia = df["qtdPontos"].var() # por padrao n-1
print("variancia:", variancia)

desvio_padrao = df["qtdPontos"].std()
print("Desvio Padrao:", desvio_padrao)

amplitude = maximo-minimo
print("Amplitude:", amplitude)

# %%
df["qtdPontos"].describe()

# %%
print("\n#####################################################\n")

# %%

usuario = (df.groupby(["idUsuario"]).agg(
        {
            "idTransacao": "count",
            "qtdPontos": "sum"
        }
    )
             .reset_index()
)

usuario

# %%

sumario = usuario[["idTransacao", "qtdPontos"]].describe()

print(sumario.to_string())