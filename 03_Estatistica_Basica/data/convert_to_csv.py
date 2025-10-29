# %%
import pandas as pd

df = pd.read_excel("points_tmw.xlsx")
df.to_csv("points_tmw.csv", index=False, sep=";")