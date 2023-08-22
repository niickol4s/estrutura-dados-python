class Item:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        
class Fila:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size
    
    def mostrar(self):
        atual = self.first
        while atual is not None:
            print(atual.valor, end=' ')
            atual = atual.next
        print('')
        
    def peek(self):
        return self.first.next.valor
    
    def enqueue(self, valor):
        newValor = Item(valor)
        
        if self.isEmpty():
            self.first = newValor
            self.last = newValor
        else:
            self.last.next = newValor
            self.last = newValor
        self.size += 1
        
    def dequeue(self):
        if self.isEmpty():
            return None
        
        valorremovido = self.first.valor
        self.first = self.first.next
            
        if self.first is None:
            self.last = None
        self.size -= 1
        return valorremovido
            
    def __str__(self):
        s = ""
        aux = self.first
        while aux is not None:
            s += str(aux.valor) + " "
            aux = aux.next
        return s

        