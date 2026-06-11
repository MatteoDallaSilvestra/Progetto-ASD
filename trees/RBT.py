#Class RBT, for Red-Black Tree
#Contains the implementation of Red-Black Tree and its operations

from .BST import TreeNode, BST

def color(node):
    # Ogni nodo che non esiste (None) deve essere considerato NERO
        return getattr(node, "color", "black") if node is not None else "black"

class RBTree (BST):

    def __init__(self, root=None):
        super().__init__(root)
        if self.root:
            self.root.color = 'black'


    def insert(self, node):
        
        if isinstance(node, int):
            node = TreeNode(node)

        y = None
        x = self.root
        
        # Ricerca BST standard per trovare la posizione di inserimento (foglia)
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
                
        # Aggancio del nodo al padre y
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
            
        # Inizializzazione delle foglie e del colore
        node.left = None
        node.right = None
        node.color = 'red' #inizialmente colorato di rosso
        
        # Ripristino delle proprietà Red-Black
        self.rb_insert_fixup(node)


    def rb_insert_fixup(self, x):

        while color(x.parent) == "red":
            y = x.parent
            z = y.parent
            
            # PARTE A: Il padre di z è un figlio sinistro
            if y == z.left:
                u = z.right  # zio
                
                # CASO SFORTUNATO: Zio è ROSSO
                if color(u) == 'red':
                    y.color = 'black'
                    if u is not None: u.color = "black"
                    z.color = "red"
                    x = z
                    
                else:
                    # CASO QUASI FORTUNATO: Zio è NERO e z è "interno" (triangolo)
                    if x == y.right:
                        x = y
                        self.rotate_left(x)
                        y = x.parent
                        z = y.parent
                    
                    # CASO FORTUNATO: Zio è NERO e z è "esterno" (linea)
                    y.color = "black"
                    z.color = "red"
                    self.rotate_right(z)
                    
            # PARTE B: Il padre di z è un figlio destro (Simmetrico)
            else:
                u = z.left
                
                # CASO SFORTUNATO
                if color(u) == "red":
                    y.color = "black"
                    if u is not None: u.color = "black"
                    z.color = "red"
                    x = z
                    
                else:
                    # CASO QUASI FORTUNATO
                    if x == y.left:
                        x = y
                        self.rotate_right(x)
                        y = x.parent
                        z = y.parent
                    
                    # CASO FORTUNATO
                    y.color = "black"
                    z.color = "red"
                    self.rotate_left(z)

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
        

    def remove(self, node):

        if isinstance(node, int):
            node = self.find(node)

        if node is None:
            return

        # Tengo traccia del colore originale del nodo che viene effettivamente rimosso
        # o spostato, per capire se violiamo le proprietà Red-Black
        z = node
        y = z
        y_original_color = color(y)
        
        # Le variabili x e p (parent) servono per capire da dove partire per il fixup
        x = None
        p = None


        # x sarà il nodo che prende il posto di quello rimosso
        if z.left is None:
            x = z.right
            p = z.parent
            self.replace_node(z, z.right)
        elif z.right is None:
            x = z.left
            p = z.parent
            self.replace_node(z, z.left)
        else:
            # Caso con due figli: si cerca il successore (il minimo nel sottoalbero destro)
            y = self.nxt(z)
            y_original_color = color(y)
            x = y.right
            
            if y.parent == z:
                p = y
            else:
                p = y.parent
                self.replace_node(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.replace_node(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = color(z)

        # le altezze potrebbero essere sballate
        if y_original_color == "black":
            self.remove_fixup(x, p)
        
        return (None, None)

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


    def remove_fixup(self, x, p):
        while x != self.root and color(x) == 'black':
            
            if x == p.left:
                f = p.right
                # CASO ANTIPATICO: Il fratello è rosso
                if color(f) == "red":
                    if f is not None: f.color = "black"
                    p.color = "red"
                    self.rotate_left(p)
                    f = p.right
                
                # CASO SFORTUNATO: Il fratello è nero e ha entrambi i figli neri
                if color(f.left if f else None) == "black" and color(f.right if f else None) == "black":
                    #in un RBT i nodi mancanti sono considerati foglie nere
                    if f is not None: f.color = "red"
                    x = p
                    p = x.parent
                else:
                    # CASO QUASI FORTUNATO: Il fratello è nero, figlio sinistro rosso, figlio destro nero
                    if color(f.right if f else None) == "black":
                        if f and f.left: f.left.color = "black"
                        if f: f.color = "red"
                        self.rotate_right(f)
                        f = p.right
                    
                    # CASO FORTUNATO: Il fratello è nero e il figlio destro è rosso
                    if f is not None: f.color = color(p)
                    p.color = "black"
                    if f and f.right: f.right.color = "black"
                    self.rotate_left(p)
                    x = self.root
            else:

                f = p.left

                # Speculare a sopra (x è figlio destro)
                if color(f) == "red":
                    if f is not None: f.color = "black"
                    p.color = "red"
                    self.rotate_right(p)
                    f = p.left
                    
                if color(f.right if f else None) == "black" and color(f.left if f else None) == "black":
                    if f is not None: f.color = "red"
                    x = p
                    p = x.parent
                else:
                    if color(f.left if f else None) == "black":
                        if f and f.right: f.right.color = "black"
                        if f: f.color = "red"
                        self.rotate_left(f)
                        f = p.left
                    
                    if f is not None: f.color = color(p)
                    p.color = "black"
                    if f and f.left: f.left.color = "black"
                    self.rotate_right(p)
                    x = self.root

        if x is not None:
            x.color = "black"