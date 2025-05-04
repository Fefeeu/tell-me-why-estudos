# %%%
dados_fefe = ["fefe", "calvo", 20, False, "Namorando", 1032.73]
dados_fefe
dados_fefe.append("extra")
dados_fefe

# %%
# TUPLAS NÃO SÃO NADA MAIS QUE LISTAS IMUTAVEIS

tupla_fefe = "fefe", "calvo", 20, False, "Namorando", 1032.73
# tupla_fefe = ("fefe", "calvo", 20, False, "Namorando", 1032.73)
tupla_fefe

# %%
# SE DENTRO DA TUPLA FOR MUTAVEL, É POSSIVEL MUTAR ESSE OBJETO EM EXPECIFICO
tupla_fefe = ([1, 2, 3, 4],"fefe", "calvo", 20, False, "Namorando", 1032.73)
print(tupla_fefe)
tupla_fefe[0].append(5)
tupla_fefe[0].append(6)
tupla_fefe[0].append(7)
print(tupla_fefe)