class Item:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def inserir(self, valor):
        novoValor = Item(valor)
        novoValor.next = self.top
        self.top = novoValor
        self.size += 1
        
    def remover(self):
        if self.is_empty():
            raise IndexError('Pilha vazia.')
        valor = self.top.valor
        self.top = self.top.next
        self.size -= 1
        return valor
    
    def _topo(self):
        if self.is_empty():
            raise IndexError('Pilha vazia.')
        return self.top.valor
    
    def mostrar(self):
        if self.top == None:
            print('Pilha vazia.')
        
        s = ''
        p = self.top
        
        while p:
            s += str(p.valor) + '\n'
            p = p.next
        return s