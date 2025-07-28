# %%1:25
import pandas as pd

df = pd.read_csv("../data/points_tmw.csv", sep=";")
df.head()

usuarios = (df.groupby(by="idUsuario").agg(
                {
                    "qtdPontos": "sum"
                }
            ).reset_index()
        )

usuarios

# %%
from scipy.stats import t as t_student

def intervalo(sample, alpha = 0.05): # pq eh 5% de confianca
    n = len(sample)
    x_barra = sample.mean()
    s = sample.std()
    t = t_student.ppf((1 - alpha/2), n-1) # 0,975 pq eh 5% de confianca ou seja 2,5% para cada lado

    limite_inf = x_barra - t * (s / (n ** 0.5))
    limite_sup = x_barra + t * (s / (n ** 0.5))

    return float(x_barra), float(s), float(limite_inf), float(limite_sup)

stats = []
for i in range(100):
    n = 100
    sample = usuarios["qtdPontos"].sample(n) # 100 amostras aleatorias
    stats.append(intervalo(sample=sample))

stats = pd.DataFrame(stats, columns=["media", "desvio", "inferior", "superior"])

stats["VerdadeiroValorMedia"] = usuarios["qtdPontos"].mean()

stats["check"] = (stats["VerdadeiroValorMedia"] > stats["inferior"]) & (stats["VerdadeiroValorMedia"] < stats["superior"])

float(stats["check"].mean())

# %%
import matplotlib.pyplot as plt

for i in range(50):
    data = stats.iloc[i]
    color = 'green' if data["check"] else 'red'
    plt.plot(data[['inferior', 'superior']], [i,i], 'o--', color=color, alpha=0.5)

plt.vlines(data['VerdadeiroValorMedia'].max(), -1, i+1, color='black', alpha=0.5)
plt.xlabel("Valor Esperado")
plt.ylabel("Intervalos de Confiança")
plt.grid()
plt.show()