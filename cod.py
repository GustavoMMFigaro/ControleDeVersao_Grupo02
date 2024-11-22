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