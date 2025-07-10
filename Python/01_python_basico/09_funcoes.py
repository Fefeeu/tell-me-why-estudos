# %%

def ola_mundo(x):
    olaMundoString = ""
    for _ in range(x):
        olaMundoString += "ola mundo "
    return olaMundoString


# com essas definicoes de tipo, nao forca nada, ou seja eu ainda posso mandar uma string
def juros_compostos(valorInicial:int, taxa:float, anos:int)->float:

    # essa string server para documentar a funcao, PASSE O MAUSE EM CIMA DA FUNCAO
    """Juros compostos serve para acalcular o valor que vai estar no banco depois de um tempo em anos.

    valorInicial:
        um numero inteiro, que representa o valor inicial do investimento

    taxa:
        um numero float, em porcentagem decimal, que representa o quanto vai lucrar por ano
    
    anos:
        um numero inteiro, que representa a quantidade de anos que o valor vai ficar rendendo
    """
    return valorInicial * (1 + taxa)**anos


# args eh soh uma convencao, poderia ser *nomeQualquer

# args EH UMA TUPLA
def funcao_com_args(a:float, b:float, *args) -> float:
    valores = [a, b] + list(args)
    soma = 0
    for valor in valores:
        soma += valor
    return soma


# kwargs EH UM DICIONARIO
def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for tipo in kwargs:
        print(tipo, kwargs[tipo])
        imposto += preco * kwargs[tipo]
    return imposto

# %%
texto = ola_mundo(10)
print(texto)

# %% 
print(juros_compostos(taxa=0.12, valorInicial=1000, anos=10))

# %%
a = float(input("entre com um numero: "))
b = float(input("entre com um numero: "))
c = float(input("entre com um numero: "))
d = float(input("entre com um numero: "))
e = float(input("entre com um numero: "))

resultadoIncompleto = funcao_com_args(a,b)

resultado = funcao_com_args(a,b,c,d,e)

print(resultadoIncompleto, resultado)

# %%

impostos_gerais = {
    "loja": 0.01,
    "nacional": 0.005,
    "comercial": 0.001
}

valor_imposto = calc_imposto(100, 0.03, municipio=0.01, estado=0.2, **impostos_gerais)

print("valor a ser pago:", valor_imposto)