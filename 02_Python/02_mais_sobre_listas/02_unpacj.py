# %% trocando valores
A = 1
B = 5
print(A,B)

A, B = B, A

print(A, B)

# %% pegando valoes especificos
a, b, *resto = 1, 2, 3, 4, 5, 6

print(a,b,resto)

# %% abrindo
def soma(a, b, c, d, e):
    return a+b+c+d+e

values = [1,2,3,4,5]

soma(*values)
