class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_em_nivel_recursivo(valor, self.raiz)

    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)
    
    def mostrar_pos_ordem(self):
        if self.raiz is None:
            print('bt_pos_ordem vazia')
        else:
            self.mostrar_pos_ordem_recursivo(self.raiz)
    
    def mostrar_pos_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_pos_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pos_ordem_recursivo(no.direita)


bt_pos_ordem = ArvoreBinaria()

bt_pos_ordem.inserir_em_nivel(5)
bt_pos_ordem.inserir_em_nivel(3)
bt_pos_ordem.inserir_em_nivel(7)
bt_pos_ordem.inserir_em_nivel(2)
bt_pos_ordem.inserir_em_nivel(4)
bt_pos_ordem.inserir_em_nivel(6)
bt_pos_ordem.inserir_em_nivel(8)
bt_pos_ordem.mostrar_pos_ordem()
print()