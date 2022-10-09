from ListaNaoOrdenada import *

def menu():
    print("---------------------------CANDIDATOS---------------------------")
    print("'ADD, <Nome_Candidato>' para adicionar candidato.")
    print("'FIRST' para ver informações sobre o primeiro candidato da fila.")
    print("'DEL' para remover o primeiro candidato da fila.")
    print("'SHOW' para mostrar a fila de todos os candidatos.")
    print("'SPIN', <Qntd_vezes> girar a fila, Qntd_vezes default: 1")
    print("'EXIT' finaliza o programa.")
    op = input("Operação: ").split()
    print()

    if len(op) == 1:
        opcao = op[0].upper()
        aux = None
    else:
        opcao = op[0].upper()
        aux = op[1]

    return opcao, aux


def remove_candidato():
    pass


def girar():
    pass


candidatos = ListaNaoOrdenada()
opcao = None

while opcao != 'EXIT':

    opcao, aux = menu()

    if opcao == 'ADD':
        candidatos.append(aux)
    elif opcao == 'FIRST':
        pass


print(candidatos)