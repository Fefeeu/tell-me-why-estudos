# %%
numeros = [1, 3, 5, 7, 9, 11]   # obs.: a lista não é do tipo int
print(numeros)
for numero in numeros:
    print(numero, end=" ")

# %%
fefe = ["fefe", "calvo", 20, False, "Namorando", 1032.73]
for info in fefe:
    print(type(info), ": ", info, end=" ||| ", sep="")
print()
for i in range(len(fefe)):
    print(fefe[i], end=" ")