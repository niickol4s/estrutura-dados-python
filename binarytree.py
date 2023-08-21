class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.value, self.value, self.right and self.right.value)

class tree:
    def __init__(self, root = None):
        self.raiz = Node(root)
    
    def insert(self, value, side):
        if side == 'E':
            self.root.left = Node(value)
        elif side == 'D':
            self.root.right = Node(value)
        else:
            raise ValueError('Lado não informado.')


