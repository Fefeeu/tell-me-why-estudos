# %%
import pandas as pd 
import sqlalchemy

with open("27_2etl.sql") as open_file:
    query = open_file.read()

print(query)

# %%
engine = sqlalchemy.create_engine("sqlite:///../data/banco_de_dados/olist.db")

df = pd.read_sql_query(query, con=engine) 

df

# %% precisa entender isso ainda nao
from sklearn import cluster

kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[["totalRevenue", "qtSalles"]])

df["cluster"] = kmean.labels_
df

# %%
df.to_sql(
    "sellers_cluster", 
    con=engine,
    if_exists="replace", 
    index=False
)