# %%
# DICIONARIOS SÃO PARES DE chave E valor

dados_fefe = {
    "nome":"Fefe", 
    "idade":20, 
    "filhos":False, 
    "salario":1038.1231,
    "formacao":["Don Inacio", "inatel"],
    "cargos":[
        {"nome": "aluno", "empresa":"inatel"},
        {"nome": "monitor", "empresa":"inatel"},
        {"nome": "bolcista", "empresa":"inatel"}
    ]
}   #  nas chaves só podem ser usadas string e int, E POR INCRIVEL QUE PAREÇA FLOAT

print(dados_fefe["cargos"][-1]["nome"])
print()

# %%
# AQUI ESTAMOS ADICIONANDO UMA CHAVE E UM VALOR NO DICIONARIO
dados_fefe["estado civil"] = "namorando"
print(dados_fefe["estado civil"])
print()


# %%
print(dados_fefe.keys())
print(dados_fefe.values())
print(dados_fefe.items())
print()


# %%

for i in dados_fefe:
    print(i, "->", dados_fefe[i])   # i RECEBE O VALOR DAS CHAVES

# %%
for item in dados_fefe.items():
    print(item)
# %%
for chave, valor in dados_fefe.items():
    print(chave, "->", valor)