from Noh import *

class ListaVazia(Exception): pass


class OutOfRange(Exception): pass


class ListaNaoOrdenada:
    def __init__(self):
        self.head = None
        self.tamanho = 0
        self.tail = Noh(self.head)


    def __str__(self): return f'{self.head}'


    def is_empty(self): return self.head == None


    def size(self): return self.tamanho


    def add(self,item):
        temp = Noh(item)
        temp.setNext(self.head)
        self.head = temp
        self.tamanho += 1
        if self.tamanho <= 1:
            self.tail = temp        


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
        try:
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
                self.tamanho -= 1
        except:
            print("Item não encontrado")


    def append(self, item): # append O(1)
        temp = Noh(item)        
        self.tail.setNext(temp)             
        self.tail = temp
        self.tamanho += 1
        if self.tamanho <= 1:
            self.head = temp  

    
    def insert(self, item, pos): #insert O(n)
        temp = Noh(item)
        atual = self.head
        count = 2

        if pos == 1:
            self.add(item)
        elif pos == self.tamanho+1:
            self.append(item)
        elif pos > self.tamanho+1 or pos < 1:
            if self.is_empty():
                raise OutOfRange(f'Posição fora do limite. Apenas a posição 1 está disponível.')
            else:
                raise OutOfRange(f"Posição fora do limite. Disponíveis: 1 à {self.tamanho+1}")
        else:
            while count != pos:
                atual = atual.getNext()
                count += 1

            temp.setNext(atual.getNext())
            atual.setNext(temp)
            self.tamanho += 1
    

    def pop(self): # pop O(1)
        if self.is_empty():
            raise ListaVazia('A lista está vazia')
        else:
            removido = self.head.getData()
            self.head = self.head.getNext()
            self.tamanho -= 1
            return removido


if __name__ == "__main__":
    lista = ListaNaoOrdenada()

    lista.append(1)
    print(lista)
    lista.append(2)
    print(lista)
    lista.append(3)  
    print(lista)
    lista.append(4)
    lista.append(5)
    lista.insert(6, 6)
    print(lista)
    lista.append(7)
    print(lista)    
    lista.pop()
    print(lista)
    lista.pop()
    print(lista)
    lista.pop()
    print(lista)