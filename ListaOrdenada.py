from Noh import *


class ListaOrdenada:
    def __init__(self):
        self.head = None
        self.tamanho = 0

    def __str__(self): 
      if self.is_empty() == True:
        return "->"
      return f'{self.head}'

    def is_empty(self): return self.head == None

    def add(self, item):
        atual = self.head
        anterior = None
        parar = False
        while atual != None and not parar:
            if atual.getData() > item:
                parar = True
            else:
                anterior = atual
                atual = atual.getNext()

        temp = Noh(item)
        if anterior == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(atual)
            anterior.setNext(temp)

        self.tamanho += 1

    def size(self):
        return self.tamanho

    def search(self, item):
        atual = self.head
        encontrou = False
        parar = False
        while atual != None and not encontrou and not parar:
            if atual.getData() == item:
                encontrou = True
            elif atual.getData() > item:
                parar = True
            else:
                atual = atual.getNext()

        return encontrou

    def index(self, item):
        atual = self.head
        cont = 0
        while atual != None:
            if atual.getData() == item:
                return cont
            else:
                cont += 1
                atual = atual.getNext()

        return "Item não encontrado"

    def remove(self, item):
        try:
            atual = self.head
            anterior = None
            encontrou = False
            while not encontrou:
                if atual.getData() == item:
                    encontrou = True
                else:
                    anterior = atual
                    atual = atual.getNext()

            if anterior == None:
                self.head = atual.getNext()
            else:
                anterior.setNext(atual.getNext())
            self.tamanho -= 1
        except:
            print("Item não encontrado")

    def pop(self, pos=None):
        if pos == None:
            pos = self.tamanho-1
        atual = self.head
        anterior = None
        cont = 0
        while atual != None:
            if cont == pos:
                result = atual.getData()
                if anterior!=None:
                  anterior.setNext(atual.getNext())
                else:
                  self.head = atual.getNext()
                self.tamanho -= 1
                return result
            else:
                cont += 1
                anterior = atual
                atual = atual.getNext()

        if self.is_empty() == True:
          return "A lista está vazia"  
        return "Posicao não encontrada"


if __name__ == "__main__":
    lista = ListaOrdenada()
    print(lista.is_empty())
    lista.add("3")
    lista.add("8")
    lista.add("5")
    lista.add("9")
    lista.add("1")
    print(lista)
    print(lista.search("5"))
    lista.remove("3")
    print(lista)
    print(lista.search("3"))
    lista.remove("3")
    print(lista.size())
    lista.add("3")
    lista.add("5")
    lista.add("4")
    lista.add("8")
    print(lista.size())
    lista.remove("3")
    lista.remove("8")
    lista.remove("3")
    print(lista)
    print("Tamanho: ", lista.size())
    print("index do 1: ", lista.index("1"))
    print("index do 5: ", lista.index("5"))
    print("index do 5: ", lista.index("9"))
    print("index do 10: ", lista.index("10"))
    print(lista.pop())
    print(lista.pop(4))
    print(lista.pop(3))
    print(lista.pop(2))
    print(lista.pop(1))
    print(lista.pop())
    print(lista.pop())
    print(lista)
