# %%
import pandas as pd

df = pd.read_parquet("../data/dados_clones.parquet")
df.head()

# %%
df.columns

# %%
df['General Jedi encarregado'].unique()
# %%

target = "Status "
#features = ['Massa(em kilos)', 'Estatura(cm)', 'General Jedi encarregado']
features = ['Massa(em kilos)', 'Estatura(cm)']

X = df[features]
y = df[target]

# %%
from sklearn import tree

# x = x.replace({
#     'Yoda':1,
#     'Shaak Ti':2,
#     'Obi-Wan Kenobi':3,
#     'Aayla Secura':4,
#     'Mace Windu':5
# })

model = tree.DecisionTreeClassifier()
model.fit(X=X, y=y)

# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400)
tree.plot_tree(model,
               feature_names=features,
               class_names=model.classes_,
               filled=True,
               max_depth=3)
# %%
