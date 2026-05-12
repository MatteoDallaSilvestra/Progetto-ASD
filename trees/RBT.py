#Class RBT, for Red-Black Tree
#Contains the implementation of Red-Black Tree and its operations
from .RBTreeNode import RBTreeNode
from .BinaryTree import BinaryTree

class RBT(BinaryTree):

    def __init__(self, root=None):
        super().__init__(root)
        if self.root:
            self.root.color = 'black'

    def insert(self, key):
        new_node = RBTreeNode(key)
        self.rb_insert(new_node)

    def rb_insert(self, z):

        y = None
        x = self.root
        
        # Ricerca BST standard per trovare la posizione di inserimento
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
                
        # Aggancio del nodo z al padre y
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
            
        # Inizializzazione delle foglie e del colore
        z.left = None
        z.right = None
        z.color = 'red'
        
        # Ripristino delle proprietà Red-Black
        self.rb_insert_fixup(z)


    def rb_insert_fixup(self, z):

        while z.parent is not None and z.parent.color == 'red':
            # PARTE A: Il padre di z è un figlio sinistro
            if z.parent.parent is not None and z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # zio
                
                # CASO SFORTUNATO: Zio è ROSSO
                if y is not None and y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                    
                else:
                    # CASO QUASI FORTUNATO: Zio è NERO e z è "interno" (triangolo)
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(z)
                    
                    # CASO FORTUNATO: Zio è NERO e z è "esterno" (linea)
                    z.parent.color = 'black'
                    if z.parent.parent is not None:
                        z.parent.parent.color = 'red'
                        self.rotate_right(z.parent.parent)
                    
            # PARTE B: Il padre di z è un figlio destro (Simmetrico)
            elif z.parent.parent is not None:
                y = z.parent.parent.left
                
                # CASO SFORTUNATO
                if y is not None and y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                    
                else:
                    # CASO QUASI FORTUNATO
                    if z == z.parent.left:
                        z = z.parent
                        self.rotate_right(z)
                    
                    # CASO FORTUNATO
                    z.parent.color = 'black'
                    if z.parent.parent is not None:
                        z.parent.parent.color = 'red'
                        self.rotate_left(z.parent.parent)

        #la radice deve essere sempre NERA
        self.root.color = 'black'

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
            if node is None:
                return
        if node.right is not None:
            self.print_tree(node.right, level + 1)
            
        color_label = "(R)" if node.color == 'red' else "(B)"
        print(' ' * 4 * level + '-> ' + str(node.key) + ' ' + color_label)
        
        if node.left is not None:
            self.print_tree(node.left, level + 1)