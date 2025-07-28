# %%
import pandas as pd
import sqlalchemy

# %%
engine = sqlalchemy.create_engine("sqlite:///../data/banco_de_dados/olist.db")

# PARA SABER AS TABELAS DO BANCO DE DADOS
# No terminal:
# cd <pasta-que-o-db-esta>
# sqlite3 <nome-arquivo-db>.db
# .tables

# %%

clientes = pd.read_sql_table(table_name="tb_customers", con=engine)
clientes.shape

# %%
clientes.head()

# %% MAIS CORRETO PARA NAO ESTOURAR NENHUM SERVIDOR
query = "SELECT * FROM tb_customers LIMIT 100"

df_100 = pd.read_sql_query(query, con=engine)

df_100
