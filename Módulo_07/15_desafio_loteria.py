
import random

n_sorteio = random.randint(1,15)

def get_input():

    while True:
        try:
            n_usuario = int(input("Entre com um número de 1-15: "))
        
        except ValueError as err:
            print("Entre com um número válido!")
            continue

        if 1 <= n_usuario <= 15:
            return n_usuario
        
        print("Número informado não esta entre 1-15!") 

def check_number(sorteio, usuario):

    if usuario == sorteio:
        print("Parabéns você ganhou na loteria!")
        return True
    
    elif usuario > sorteio:
        print("Número muito alto. Tente novamente!")
        return False

    else:
        print("Número muito baixo. Tente novamente!")    
        return False

for tentativa in range(3):
    
    n_usuario = get_input()

    if check_number(sorteio=n_sorteio, usuario=n_usuario):
        break

else:
    print("Esgotaram suas tentativas!")