# %%

arquivo = "data.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()


# strip: remove o que foi pedido
# split: transforma em uma lista com separacao no que foi pedido, removendo esse indicador
chaves = lines[0].strip("\n").split(";")
print(chaves)

dados = dict()

for chave in chaves:
    dados[chave] = []

# comeca na posicao 1 e ternmina na ultima
for line in lines[1:]:
    valores = line.strip("\n").split(";")
    for i in range(len(chaves)):
        dados[chaves[i]].append(valores[i])

dados