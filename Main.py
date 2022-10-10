from FilaEncadeada import *


def menu():
    print('''\n---------------------------CANDIDATOS-----------------------------\n\n'Adicionar, <Nome_Candidato>' para adicionar candidato.\n'Primeiro' para ver informações sobre o primeiro candidato da fila.\n'Remover' para remover o primeiro candidato da fila.\n'Mostrar' para mostrar as informações de todos os candidatos.\n'Girar, <Qntd_vezes>' para girar a fila, valor padrão = 1.\n'Exit' para finalizar o programa.\n''')

    op = input("Operação: ").split()
    opcao = op[0].lower()

    if len(op) == 1:
        aux = None
    elif opcao == "primeiro" and len(op) > 1 or opcao == "mostrar" and len(op) > 1 or opcao == "remover" and len(op) > 1 or opcao == "exit" and len(op) > 1:
        aux = "case1"
    elif opcao == "adicionar" and len(op) > 2 or opcao == "girar" and len(op) > 2:
        aux = "case2"
    else:
        aux = op[1]

    return opcao, aux


candidatos = FilaEncadeada()

while True:

    try:
        opcao, aux = menu()

        if opcao == 'exit' and aux != "case1":
            print("\n   Finalizando o programa...\n")
            break

        elif opcao == 'adicionar' and aux != "case2":

            if aux != None and aux.isnumeric() == False:
                candidatos.enqueue(aux)
                print(f"\n   {aux} adicionado na fila!\n")

            else:
                print("\n   Digite um nome válido para o candidato, tente novamente!\n")

        elif opcao == 'primeiro' and aux != "case1":
            print(f'\n    Primeiro candidato da fila: {candidatos.first()}')

        elif opcao == 'remover' and aux != "case1":
            candidatos.dequeue()
            print('\n   Primeiro candidato removido da fila!\n')

        elif opcao == 'mostrar' and aux != "case1":

            if candidatos.size() > 0:
                print(candidatos)
            else:
                raise FilaVazia

        elif opcao == 'girar' and aux != "case2":

            if aux != None:
                for x in range(int(aux) % candidatos.size()):
                    candidatos.spin()
            else:
                candidatos.spin()

        elif aux == "case2":
            print(
                '\n   Para essa operação digite apenas uma instrução e um valor, tente novamente!\n')

        elif aux == "case1":
            print(
                '\n   Para essa operação digite apenas uma instrução, tente novamente!\n')

        else:
            raise IndexError

    except(IndexError):
        print("\n   Digite uma opção válida!\n")

    except(FilaVazia):
        print("\n   Não há fila de candidatos!\n")
