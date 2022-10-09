from Noh import *


class ListaNaoOrdenada:
    def __init__(self):
        self.head = None
        self.tamanho = 0
        # self.tail = Noh(self.head)

    def __str__(self): return f'{self.head}'

    def is_empty(self): return self.head == None

    def add(self, item):
        temp = Noh(item)
        temp.setNext(self.head)
        self.head = temp
        self.tamanho += 1
        # if self.tamanho == 0:
        #     self.tail.setData(self.head)
        # elif self.tamanho == 1:
        #     self.tail.setData(item)

    def size(self):
        return self.tamanho

    def search(self, item):
        atual = self.head
        encontrou = False
        while atual != None and not encontrou:
            if atual.getData() == item:
                encontrou = True
            else:
                atual = atual.getNext()

        return encontrou

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

    # def append(self, item):  # append O(n)
    #     temp = Noh(item)
    #     atual = self.head
    #     count = 0
    #     while count != self.tamanho-1:
    #         atual = atual.getNext()
    #         count += 1

    #     atual.setNext(temp)
    #     self.tail = temp
    #     self.tamanho += 1

    # def appendTest(self, item):  # Tentativa de append O(1)
    #     temp = Noh(item)
    #     ultimo = Noh(self.tail.getData())
    #     ultimo.setNext(temp)
    #     self.tail = temp


if __name__ == "__main__":
    lista = ListaNaoOrdenada()
    print(lista.is_empty())
    lista.add("Jose")
    lista.add("Adrian")
    lista.add("Torres")
    lista.add("Dos")
    lista.add("Santos")
    print(lista)
    print(lista.search("Adrian"))
    lista.remove("Adrian")
    print(lista)
    print(lista.search("Adrian"))
    lista.remove("Adrian")
    print(lista.size())
    lista.add("Adrian")
    lista.add("Jose")
    lista.add("Santos")
    lista.add("Torres")
    print(lista.size())
    lista.remove("Adrian")
    lista.remove("Torres")
    lista.remove("Adrian")
    print(lista.size())
