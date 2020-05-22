from Biblio import *
import os
import time

def gerar_normal(maximo,quantidade):
    arquivo = open("input_normal.txt", "w")


    x = dist_normal(-maximo, maximo, quantidade)


    for i in x:
        arquivo.write(str(i) + "\n")

    arquivo.close()



def gerar_exponencial(n):
    arquivo = open("input_exponencial.txt", "w")

    x=dist_exponencial2(1234, n, 2, 6)

    for i in x:
        arquivo.write(str(i) + "\n")

    arquivo.close()


while True:
    os.system('cls')
    print(
    '''
    Trabalho feito pelo gustavo e joao

    Menu:
    [1] gerar distribuição normal
    [2] gerar distribuição exponencial
    [3] sair
    '''
    )

    entrada_menu = int(input("entre com o sua escolha: "))

    if entrada_menu == 1:
        os.system('cls')
        maximo = int(input("valor máximo: "))
        quantidade = int(input("quantidade de valores a gerar: "))
        gerar_normal(maximo, quantidade)
        print('Foi gerado um arquivo "input_normal.txt, \npressione enter para continuar"')
        input()

    elif entrada_menu == 2:
        os.system('cls')
        quantidade = int(input("quantidade de valores a gerar: "))
        gerar_exponencial(quantidade)
        print('Foi gerado um arquivo "input_exponencial.txt, \npressione enter para continuar"')
        input()

    elif entrada_menu == 3:
        break

    else:
        print("funcao invalida")
        input()