# %%
nome_arquivo = "historia.txt"

# abre o arquivo em formato de leitura 
open_file = open(nome_arquivo)

# le os dados do arquivo
conteudo = open_file.read()
print(conteudo)

# fecha o arquivo
open_file.close()

# %%

# METODO MAIS CORRETO

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
print(conteudo)

# esse metodo eh melhor pois nao eh preciso do metodo close()