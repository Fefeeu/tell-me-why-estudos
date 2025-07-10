from random import randint

def get_input() -> int:
    while True:
        try:
            x = int(input("entre com um numero entre 1 e 15: "))
        except ValueError as err:
            print("entre com um numero valido")
            continue

        if 1 <= x <= 15:
            return x
        print("numero fora do range")


def verifica_sorteio(valor_digitado:int, numero_sorteado:int) -> bool:
    if x == numero_sorteado:
        print("Parabens, voce acertou em", i+1, "tentativa(s)")
        return True

    elif x < numero_sorteado:
        print("o valor sorteado eh maior que o valor escolhido")
        return False
    
    elif x > numero_sorteado:
        print("o valor sorteado eh menor que o valor escolhido")
        return False

valor_sorteado = randint(1, 15)

print(valor_sorteado)

for i in range(3):
    x = get_input()
    
    if verifica_sorteio(valor_digitado=x, numero_sorteado=valor_sorteado):
        break

else: # esse else ocorre se nao houver um break no for
    print("Falha ao acertar o numero")