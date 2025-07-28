# %% lista padrao

x = []

for i in range(1,100):
    x.append(i)

x

# %% lista com for

y = [num for num in range(1,100)]
y

# %% lista de funcao

def eh_par(x):
    return x % 2 ==0

z = [eh_par(num) for num in range(1,100)]
z

# %% lista com if

w = [num for num in range (1,100) if eh_par(num)]
w