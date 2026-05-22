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
        

    def remove(self, value):
        # ricerca del nodo da rimuovere
        z = self.find(value)
        if z is None:
            return

        # Tengo traccia del colore originale del nodo che viene effettivamente rimosso
        # o spostato, per capire se violiamo le proprietà Red-Black
        y = z
        y_original_color = y.color
        
        # x sarà il nodo che prende il posto di quello rimosso
        if z.left is None:
            x = z.right
            self.replace_node(z, z.right)
        elif z.right is None:
            x = z.left
            self.replace_node(z, z.left)
        else:
            # Caso con due figli: si cerca il successore (il minimo nel sottoalbero destro)
            y = self.find_min(z.right)
            y_original_color = y.color
            x = y.right
            
            if y.parent != z:
                self.replace_node(y, y.right)
                y.right = z.right
                y.right.parent = y
                
            self.replace_node(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'black':
            # Se x esiste è ora Double-Black
            self.delete_fix(x if x else z.parent) 

    def replace_node(self, u, v):
        #Sostituisce il sottoalbero con radice u con quello con radice v
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def find_min(self, node):
        #Trova il nodo con il valore minimo partendo da node
        while node.left:
            node = node.left
        return node

    def delete_fix(self, x):
        # Logica di ribilanciamento per mantenere le proprietà Red-Black
        while x and x != self.root and x.color == 'black':
            if x == x.parent.left:
                sibling = x.parent.right
                # CASO ANTIPATICO: Il fratello è rosso
                if sibling and sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(x.parent)
                    sibling = x.parent.right
                
                # CASO SFORTUNATO: Il fratello è nero e ha entrambi i figli neri
                if (not sibling.left or sibling.left.color == 'black') and (not sibling.right or sibling.right.color == 'black'):
                    #in un RBT i nodi mancanti sono considerati foglie nere
                    sibling.color = 'red'
                    x = x.parent
                else:
                    # CASO QUASI FORTUNATO: Il fratello è nero, figlio sinistro rosso, figlio destro nero
                    if not sibling.right or sibling.right.color == 'black':
                        if sibling.left: sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.rotate_right(sibling)
                        sibling = x.parent.right
                    
                    # CASO FORTUNATO: Il fratello è nero e il figlio destro è rosso
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.right: sibling.right.color = 'black'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                # Speculare a sopra (x è figlio destro)
                sibling = x.parent.left
                if sibling and sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(x.parent)
                    sibling = x.parent.left
                    
                if (not sibling.left or sibling.left.color == 'black') and (not sibling.right or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if not sibling.left or sibling.left.color == 'black':
                        if sibling.right: sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.rotate_left(sibling)
                        sibling = x.parent.left
                    
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.left: sibling.left.color = 'black'
                    self.rotate_right(x.parent)
                    x = self.root
        if x:
            x.color = 'black'