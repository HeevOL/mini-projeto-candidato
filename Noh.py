class Noh:
    def __init__(self, valor):
        self._item = valor
        self._proximo = None

    def __str__(self):
        if self._proximo!=None:
            return f'{self._item} -> {self._proximo}'
        else:
            return f'{self._item}'

    def getData(self): return self._item

    def getNext(self): return self._proximo

    def setData(self, novo_valor): self._item = novo_valor

    def setNext(self, novo_proximo): self._proximo = novo_proximo


if __name__ == '__main__':
    valor = Noh("Jose")
    valor2 = Noh("Adrian")
    valor.setNext(valor2)
    print(valor)
    print(valor.getData())
    print(valor.getNext())
    print(valor2.getData())
    valor2.setNext("Torres")
    print(valor2.getNext())
