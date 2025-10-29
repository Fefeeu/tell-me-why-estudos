# %%
import pandas as pd 
import sqlalchemy

df = pd.read_csv("../data/points_tmw - dados origem.csv")
df.head()

engine = sqlalchemy.create_engine("sqlite:///../data/tmw.db")

df.to_sql("points", engine, if_exists="replace", index=False)   

# %%