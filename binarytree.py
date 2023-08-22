class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s <- %s <- %s <- %s -> %s -> %s -> %s' % (self.left.left and self.left.left.value, self.left.right and self.left.right.value, self.left and self.left.value, self.value, self.right and self.right.value, self.right.left and self.right.left.value, self.right.right and self.right.right.value)

class Tree:
    def __init__(self, root = None):
        self.root = Node(root)
    
    def insert(self, value):
        ## if self.root is None: Nesse caso, não é necessário verificação. A raíz já está vazia.
        self.root = Node(value)
        self._insert(value, self.root)
    
    def _insert(self, value, Node):
        if root.left is None:
            root.left = Node(value)
        elif root.right is None:
            root.right = Node(value)
        else:
            if root.left.right is None:
                self._insert(value, root.left)
            
            self._insert(value, root.right)

## Percurso em ordem de níveis 

tree = Tree()
root = Node(3)
root.left = Node(4)
root.right = Node(9)

root.left.left = Node(8)
root.left.right = Node(1)

root.right.left = Node(5)
root.right.right = Node(3)

print(root)
