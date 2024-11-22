import os

def limpar_tela():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

historico = []
while True:
    print("Este é um software de calculos matemáticos, abaixo é o menu que exibe as opções para escolha de equação.")
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão interira")
    print("5 - Divisão com resto")
    print("6 - Equação Quadrática")
    print("7 - Histórico")
    print("0 - Sair do Programa")
    print()

    menu = int(input("Escolha a opção que deseja: "))

    if menu == 1:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result = x + y
       print("O resultado é: ",result)
       historico.append(f"Soma: {x} + {y} = {result}")

    elif menu == 2:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result = x - y
       print("O resultado é: ",result)
       historico.append(f"Subtração: {x} - {y} = {result}")

    elif menu == 3:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result = x * y
       print("O resultado é: ",result)
       historico.append(f"Subtração: {x} * {y} = {result}")

    elif menu == 4:
       x = int(input("Qual o primeiro N: "))
       y = int(input("Qual o segundo N: "))
       result = x / y
       print("O resultado é: ",result)
       historico.append(f"Divisão: {x} / {y} = {result}")
       if x or y == 0:
        print("Divisão por Zero não permitida.")