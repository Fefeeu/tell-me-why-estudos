# %%

nome_arquivo = "historia.txt"



# %%
# sobreescrevendo
txt = "escrevendo um arquivo qualquer, sobreescrevendo ele"
with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)

# %%
# adicionando
txt = "\nescrevendo um arquivo qualquer, adicionando a ele"
with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)