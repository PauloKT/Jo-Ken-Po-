import os
import time
import random

print("Bem vindo ao Jo-Ken-Po!")
time.sleep(2)
os.system('cls')

# 1 = pedra, 2 = papel, 3 tesoura
choices = [1, 2, 3]

while True:
    print("="*2,"-"*3,"MENU","-"*3,"="*2)
    print(" ")
    print("[1] Iniciar Jogo")
    print("[2] Fechar jogo")
    escolha=int(input("Faça sua escolha: "))
    print(" ")
    print("="*3,"-"*3,"  ","-"*3,"="*3)
    os.system('cls')

    if escolha == 2:
        print("Obrigado por jogar!")
        break
    elif escolha == 1:
        while True:
            print("Escolha uma das opções")
            print("[1] Pedra")
            print("[2] Papel")
            print("[3] Tesoura")
            print("[4] Voltar ao menu")
            print(' ')
            opções = int(input("Escolha: "))
            print(" ")

            if opções == 4:
                os.system('cls')
                break

            computerChoice = random.choice(choices)

            if opções == computerChoice:
                print("Empate!")
            elif (opções == 1 and computerChoice == 3) or \
                (opções == 2 and computerChoice == 1) or \
                (opções == 3 and computerChoice == 2):
                print("Você ganhou!")
            else:
                print("Você perdeu!")

            print(" ")
            print(f"Você escolheu: {opções}")
            print(f"O computador escolheu: {computerChoice}")

            time.sleep(2)
            os.system('cls')

    
    else:
        print("Escolha invalida! Tente novamente")
        continue
