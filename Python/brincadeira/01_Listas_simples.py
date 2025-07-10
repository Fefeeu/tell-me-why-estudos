# %%

# ------------------ CONVERTE DE CELCIOS PARA FAHRENHEIT ------------------
temperaturas = [22.5, 30.0, 18.4, 27.1, 15.8]
fahrenheit = []

for temperatura in temperaturas:
    f = temperatura*(9/5)+32

    fahrenheit.append(f)
print(fahrenheit)


# %%

# ------------------ VERIFICA SE A IDADE ESTA ENTRE 0 E 120 ---------------
def verificaIdade(a):
    return (a <= 120 and a >= 0)

idades = [25, 30, 17, 42, 120, 33, 19, 200, 28]

for idade in idades:
    if not verificaIdade(idade):
        idades.remove(idade)
print(idades)


# %%

# ------------------ SUBISTITUI PELA MEDIA SE 0 ---------------------------
vendas = [150, 200, 0, 180, 0, 210]
contador = 0
soma = 0
for i in vendas:
    if i != 0:
        soma += i
        contador += 1

for i in range(len(vendas)):
    if vendas[i] == 0:
        vendas[i] = soma/contador
print(vendas)
