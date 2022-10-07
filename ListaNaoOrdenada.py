from Noh import *

class ListaNaoOrdenada:
    def __init__(self): #construtor
        self.head = None
        self.tamanho = 0
        self.tail = Noh(self.head)
    

    def __str__(self): return f'{self.head}'


    def is_empty(self): return self.head == None


    def add(self,item):
        temp = Noh(item)
        temp.setNext(self.head)
        self.head = temp
        self.tamanho += 1
        if self.tamanho == 0:
            self.tail.setData(self.head)
        elif self.tamanho == 1:
            self.tail.setData(item)


    def size(self):
        # atual = self.head
        # contador = 0
        # while atual != None:
        #     contador = contador + 1
        #     atual = atual.getNext()
        # return contador
        return self.tamanho

    
    def search(self,item):
        atual = self.head #atual == temp
        encontrou = False
        while atual != None and not encontrou:
            if atual.getData() == item:
                encontrou = True
            else:
                atual = atual.getNext()

        return encontrou

    def remove(self,item):
        atual = self.head
        anterior = None
        encontrou = False
        while not encontrou: #percorre a lista
            if atual.getData() == item:
                encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()

        if anterior == None:
            self.head = atual.getNext()
        else:
            anterior.setNext(atual.getNext())
    

    def append(self, item): #append O(n)
        temp = Noh(item)
        atual = self.head
        count = 0
        while count != self.tamanho-1:
            atual = atual.getNext()
            count += 1

        atual.setNext(temp)
        self.tail = temp
        self.tamanho += 1

    
    def appendTest(self, item): # Tentativa de append O(1)
        temp = Noh(item)
        ultimo = Noh(self.tail.getData())
        ultimo.setNext(temp)
        self.tail = temp


if __name__ == "__main__":

    lista = ListaNaoOrdenada()
    print(lista.tail)
    lista.add(30)
    print(lista.tail)
    print(lista)
    lista.add(60)
    print(lista.tail)
    print(lista)
    lista.add(90)
    print(lista.tail)
    print(lista)
    lista.append(120)
    print(lista.size())
    print(lista.tail)
    print(lista)