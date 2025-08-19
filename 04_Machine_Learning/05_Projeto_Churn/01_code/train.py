# %%
import pandas as pd

df = pd.read_csv("../data/abt_churn.csv")
df.head()

# %% Safras do out of time
oot = df[df['dtRef'] == df['dtRef'].max()].copy

# %%
df_train = df[df['dtRef'] < df['dtRef'].max()].copy()

# %% Separando variaveis e target
features = df_train.columns[2:-1] # não pega a data, nem o target
target = "flagChurn"

X, y = df_train[features], df_train[target]

# %%
from sklearn import model_selection

# Separação sem Extratificação
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, 
                                                                    random_state=42, 
                                                                    test_size=0.2
                                                                    )

# %%
print("Verificação se as amostras são parecidas")
print("Taxa variável resposta Geral:", y.mean())
print("Taxa variável resposta Treino:", y_train.mean())
print("Taxa variável resposta: Teste", y_test.mean())

# %%

# Separação com Estratificação
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, 
                                                                    random_state=42, 
                                                                    test_size=0.2,
                                                                    stratify=y
                                                                    )
# Separação com Estratificação faz com que a proporção entre as respostas fique melhor
# Porem Estratificação é custoso, então pode não ser bem usada dependendo do caso
print("Verificação se as amostras são parecidas")
print("Taxa variável resposta Geral:", y.mean())
print("Taxa variável resposta Treino:", y_train.mean())
print("Taxa variável resposta: Teste", y_test.mean())

# %%
