# %%
#============================ SAMPLE ============================
import pandas as pd

df = pd.read_csv("../data/abt_churn.csv")
df.head()
# %% Safras do out of time
oot = df[df['dtRef'] == df['dtRef'].max()].copy()

# %%
df_train = df[df['dtRef'] < df['dtRef'].max()].copy()

# %% Separando variaveis e target
features = df_train.columns[2:-1] # não pega a data(dia), nem o target
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
#============================ EXPLORE ===========================
X_train.isna().sum().sort_values(ascending=False) # verifica se ha dados faltantes

# %%
pd.set_option('display.max_rows', 80)
pd.set_option('display.max_columns', None)
df_analise = X_train.copy()
df_analise[target] = y_train
sumario = df_analise.groupby(by=target).agg(["mean", "median"]).T
sumario

# %%
sumario['diff_abs'] = sumario[0] - sumario[1]
sumario['diff_rel'] = sumario[0]/sumario[1]
sumario.sort_values(by=['diff_rel'], ascending=False)

# %%
from sklearn import tree
import matplotlib.pyplot as plt

arvore = tree.DecisionTreeClassifier(random_state=42, max_depth=5)
arvore.fit(X_train, y_train)

plt.figure(dpi=800, figsize=[4,4])
# verificando quais variaveis podem ser importantes para a analiza
tree.plot_tree(arvore, feature_names=X_train.columns,
         filled=True,
         class_names=[str(i) for i in arvore.classes_]
         )

# %% usando todos os ramos
arvore = tree.DecisionTreeClassifier(random_state=42, max_depth=None)
arvore.fit(X_train, y_train)
feature_importances = (pd.Series(arvore.feature_importances_, index=X_train.columns)
 .sort_values(ascending=False)
 .reset_index())

feature_importances['acum.'] = feature_importances[0].cumsum()
feature_importances # um exemplo seria pegar até 95%
feature_importances[feature_importances["acum."] < 0.96]

# %%
best_fetures = (feature_importances[feature_importances["acum."] < 0.96]['index']
                .tolist())
best_fetures

# %%
#============================ MODIFY ============================
from feature_engine import discretisation, encoding
from sklearn import pipeline

# Discretizar
tree_discretisation = discretisation.DecisionTreeDiscretiser(
    variables=best_fetures,
    regression=False,
    cv=3,
    bin_output="bin_number" # faz sair o numero do BIN, e isso é o nó da arvore que a observação caiu
    )
tree_discretisation.fit(X_train[best_fetures], y_train) # esta aprendendo 
X_train_transform = tree_discretisation.transform(X_train[best_fetures])
X_train_transform

# Onehot
onehot = encoding.OneHotEncoder(variables=best_fetures, ignore_format=True)
onehot.fit(X_train_transform, y_train)

# isso é feito, pois por serem valores numéricos, o modelo pode entender que são valores continuos (ou seja 3 é maior que 2), e não "niveis"
X_train_transform = onehot.transform(X_train_transform)
X_train_transform

# %%
# arvore_nova = tree.DecisionTreeClassifier(random_state=42)
# arvore_nova.fit(X_train_transform, y_train)

# (pd.Series(arvore_nova.feature_importances_, index=X_train_transform.columns)
#    .sort_values(ascending=False)
#    )

# %%
#============================ MODEL NAO APROFUNDADDO ============
from sklearn import linear_model
from sklearn import naive_bayes
from sklearn import ensemble

# model = linear_model.LogisticRegression(penalty=None, random_state=42, max_iter=100000)
# reg.fit(X_train_transform, y_train)
# model = naive_bayes.BernoulliNB()
# model = ensemble.RandomForestClassifier(random_state=42,
#                                         min_samples_leaf=20,
#                                         n_jobs=-1, # é o numero de nucleos que serão usados para rodas as N arvores (-1 = max)
#                                         n_estimators=500 # numero de arvores
#                                         )
model = ensemble.AdaBoostClassifier(random_state=42,
                                    n_estimators=500,
                                    learning_rate=0.01)


# pipeline automatiza o processo de transformação
model_pipeline = pipeline.Pipeline( 
    steps=[
        ("Discretizar", tree_discretisation),
        ("Onehot", onehot),
        ("Model", model),
    ]
)

model_pipeline.fit(X_train, y_train)



# %%
from sklearn import metrics

# y_train_predict = reg.predict(X_train_transform)
# y_train_proba = reg.predict_proba(X_train_transform)[:,1] #curva roc
y_train_predict = model_pipeline.predict(X_train)
y_train_proba = model_pipeline.predict_proba(X_train)[:,1]


acc_train = metrics.accuracy_score(y_train, y_train_predict)
auc_train = metrics.roc_auc_score(y_train, y_train_proba)
roc_train = metrics.roc_curve(y_train, y_train_proba)
print("Acurácia Treino: ", acc_train)
print("AUC Treino: ", auc_train)

# %%    
#============================ USANDO NO TESTE ===================
# X_test_transform = tree_discretisation.transform(X_test[best_fetures])
# X_test_transform = onehot.transform(X_test_transform)
# y_test_predict = reg.predict(X_test_transform)
# y_test_proba = reg.predict_proba(X_test_transform)[:,1] #curva roc
y_test_predict = model_pipeline.predict(X_test)
y_test_proba = model_pipeline.predict_proba(X_test)[:,1]


acc_test = metrics.accuracy_score(y_test, y_test_predict)
auc_test = metrics.roc_auc_score(y_test, y_test_proba)
roc_test = metrics.roc_curve(y_test, y_test_proba)
print("Acurácia Teste: ", acc_test)
print("AUC Teste: ", auc_test)

# %%    
#============================ USANDO NO Out Of Time =============
# oot_transform = tree_discretisation.transform(oot[best_fetures])
# oot_transform = onehot.transform(oot_transform)
# y_oot_predict = reg.predict(oot_transform)
# y_oot_proba = reg.predict_proba(oot_transform)[:,1] #curva roc

y_oot_predict = model_pipeline.predict(oot[features])
y_oot_proba = model_pipeline.predict_proba(oot[features])[:,1]

acc_oot = metrics.accuracy_score(oot[target], y_oot_predict)
auc_oot = metrics.roc_auc_score(oot[target], y_oot_proba)
roc_oot = metrics.roc_curve(oot[target], y_oot_proba)
print("Acurácia OOT: ", acc_oot)
print("AUC OOT: ", auc_oot)

# %%
plt.figure(dpi=400)
plt.plot(roc_train[0], roc_train[1])
plt.plot(roc_test[0], roc_test[1])
plt.plot(roc_oot[0], roc_oot[1])
plt.grid(True)
plt.title("Curva ROC")
plt.legend([
    f"Treino: {100*auc_train:.2f}",
    f"Teste: {100*auc_test:.2f}",
    f"Out-of-Time: {100*auc_oot:.2f}"
])
# %%
