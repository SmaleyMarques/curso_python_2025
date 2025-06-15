# %%
# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

# %%
# Fase 1

numero_sorteio = 7 # Número inserido manualmente

numero_usuario = int(input("Entre com um número entre 1 e 15: "))

if numero_sorteio == numero_usuario:
    print("Parabéns! Você se tornou milionário")

elif numero_usuario > numero_sorteio:
    print("Número muito alto. Tente um número menor!")

else:
    print("Número muito baixo. Tente um número menor!")

# %%
# Fase 2 

numero_sorteio = 7 # Número inserido manualmente

numero_usuario = int(input("Entre com um número entre 1 e 15: "))

for i in range(3):

    if numero_sorteio == numero_usuario:
        print("Parabéns! Você se tornou milionário")

    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor!")

    else:
        print("Número muito baixo. Tente um número menor!")

# %%
# Fase 3 

numero_sorteio = 7 # Número inserido manualmente

numero_usuario = int(input("Entre com um número entre 1 e 15: "))

for i in range(3):

    if numero_sorteio == numero_usuario:
        print("Parabéns! Você se tornou milionário")
        break

    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor!")

    else:
        print("Número muito baixo. Tente um número menor!")
else:
    print("Suas tentativas acabaram!")

# %%
# Fase 4 

numero_sorteio = 7 # Número inserido manualmente

for i in range(3):
    
    numero_usuario = int(input("Entre com um número entre 1 e 15: "))
    if not 1 <= numero_usuario <= 15:
        continue

    if numero_sorteio == numero_usuario:
        print("Parabéns! Você se tornou milionário")
        break

    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor!")

    else:
        print("Número muito baixo. Tente um número menor!")
else:
    print("Suas tentativas acabaram!")

# %%
# Fase 5 

numero_sorteio = 7 # Número inserido manualmente

for i in range(3):
    
    while True:
        numero_usuario = int(input("Entre com um número entre 1 e 15: "))
        if not 1 <= numero_usuario <= 15:
            break

    if numero_sorteio == numero_usuario:
        print("Parabéns! Você se tornou milionário")
        break

    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor!")

    else:
        print("Número muito baixo. Tente um número menor!")
else:
    print("Suas tentativas acabaram!")

# %%
# Fase 6 

numero_sorteio = 7 # Número inserido manualmente

for i in range(3):
    
    while True:
        try:
            numero_usuario = int(input("Entre com um número entre 1 e 15: "))
            
        except ValueError as e:
            print("Valor inválido!")
            continue

        if 1 <= numero_usuario <= 15:
            break

        print("Valor inválido! o Valor deve ser entre 1 e 15.")

    if numero_sorteio == numero_usuario:
        print("Parabéns! Você se tornou milionário")
        break

    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor!")

    else:
        print("Número muito baixo. Tente um número menor!")
else:
    print("Suas tentativas acabaram!")

# %%
# Fase 7 

numero_sorteio = 7 # Número inserido manualmente

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número entre 1 e 15: "))
            
        except ValueError as e:
            print("Valor inválido!")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Valor inválido! o Valor deve ser entre 1 e 15.")

for i in range(3):
    
    numero_usuario = get_input()

    if numero_sorteio == numero_usuario:
        print("Parabéns! Você se tornou milionário")
        break

    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor!")

    else:
        print("Número muito baixo. Tente um número menor!")
else:
    print("Suas tentativas acabaram!")

# %%
# Fase 8

import random 

numero_sorteio = random.randint(1,15)

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número entre 1 e 15: "))
            
        except ValueError as e:
            print("Valor inválido!")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Valor inválido! o Valor deve ser entre 1 e 15.")

for i in range(3):
    
    numero_usuario = get_input()

    if numero_sorteio == numero_usuario:
        print("Parabéns! Você se tornou milionário")
        break

    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor!")

    else:
        print("Número muito baixo. Tente um número menor!")
else:
    print("Suas tentativas acabaram!")

# %%
# Fase 8

import random 

numero_sorteio = random.randint(1,15)

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número entre 1 e 15: "))
            
        except ValueError as e:
            print("Valor inválido!")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Valor inválido! o Valor deve ser entre 1 e 15.")

def check_numbers(sorteio, usuario):

    if sorteio == usuario:
        print("Parabéns! Você se tornou milionário")
        return True

    elif usuario > sorteio:
        print("Número muito alto. Tente um número menor!")
        return False
    else:
        print("Número muito baixo. Tente um número menor!")
        return False
    
for i in range(3):
    
    numero_usuario = get_input()

    if check_numbers(sorteio=numero_sorteio,usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram!")