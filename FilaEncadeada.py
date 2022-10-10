from ListaNaoOrdenada import *


class FilaVazia(Exception):
    pass


class FilaEncadeada:
    def __init__(self):
        self._dados = ListaNaoOrdenada()
        self._tamanho = 0

    def __len__(self):
        return self._tamanho

    def size(self):
        return self._tamanho

    def is_empty(self):
        return self._tamanho == 0

    def first(self):
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        return self._dados.primeiro()

    def enqueue(self, item):
        # if self._tamanho == self._dados.size():
        #     self._altera_tamanho(2 * self._dados.size())
        self._dados.append(item)
        self._tamanho += 1

    def dequeue(self):
        if self.is_empty():
            raise FilaVazia('A Fila está vazia')
        # if 0 < self._tamanho <= (self._dados.size() // 4):
        #     self._altera_tamanho(self._dados.size() // 2)
        result = self._dados.primeiro()
        self._dados.remove_primeiro()
        self._tamanho -= 1
        return result
    
    def spin(self, vezes=1):
        self.enqueue(self.dequeue())

    def show(self):
        print(self)

    def __str__(self):
        posicao = 0
        result = "\nFila de espera dos candidatos:\n"
        for k in range(self._tamanho):
            result += f'\n    {posicao+1}º: {self._dados.acessar(posicao)}'
            posicao = (1 + posicao)
        return result


if __name__ == "__main__":
    fila = FilaEncadeada()
    print(fila.size())
    print(fila.is_empty())
    fila.enqueue(10)
    fila.enqueue(15)
    fila.enqueue(20)
    fila.enqueue(25)
    fila.enqueue(30)
    fila.enqueue(35)
    fila.enqueue(40)
    fila.enqueue(45)
    fila.enqueue(50)
    fila.enqueue(55)
    fila.dequeue()
    fila.enqueue(60)
    print(fila)
    print(fila.size())
    print(fila.is_empty())
    print(fila.first())
    print(fila)
    fila.spin()
    print(fila)
    fila.spin(5)
    print(fila)