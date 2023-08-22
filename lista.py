class Item:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class LinkedList:
    def __init__(self):
        self.inicio = None
    
    def inserir(self, valor):
        novo_item = Item(valor)
        if self.inicio is None:
            self.inicio = novo_item
        else:
            aux = self.inicio
            
            while aux.next is not None:
                aux = aux.next
            aux.next = novo_item
        self.size += 1
    
    def is_empty(self):
        return self.inicio is not None
    
    def remover(self):
        
        if self.is_empty():
            raise Exception ('Lista vazia.')
        
        penultimo = None
        ultimo = self.inicio
        valor = None
        
        while ultimo is not None:
            penultimo = ultimo
            valor = ultimo.valor
            ultimo = ultimo.next
        penultimo.next = None
        self.size -= 1
        return valor
    
    
        
        
        
        
        
        
        