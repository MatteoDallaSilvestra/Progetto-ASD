#Class RBT, for Red-Black Tree
#Contains the implementation of Red-Black Tree and its operations

from .BST import  BST

def color(node):
    # Ogni nodo che non esiste (None) deve essere considerato NERO
        return getattr(node, "color", "black") if node is not None else "black"

class RBTree (BST):

    def __init__(self, root=None):
        super().__init__(root)
        if self.root:
            self.root.color = 'black'


    def insert(self, node):

        node.color = 'red'
        
        #DELEGATO al BST
        super().insert(node)
        
        # 3. Ripristino delle proprietà Red-Black
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
            return None

        if node.left is None or node.right is None:
            y = node
        else:
            y = self.nxt(node)

        # 2. Salvato lo stato ORIGINALE prima che il BST lo modifichi
        y_original_color = color(y)
        x = y.left if y.left is not None else y.right
        p = y.parent
        

        is_left_child = (y == p.left) if p else False

        # 3. DELEGATO al BST
        res = super().remove(node)

        # 4. Ripristino RBT usando lo stato salvato
        if y_original_color == "black":
            self.remove_fixup(x, p, is_left_child)

        return res


    def remove_fixup(self, x, p, is_left=None):
        while x != self.root and color(x) == 'black':
            
            left_side = is_left if is_left is not None else (x == p.left)
            is_left = None # Resettiamo per le iterazioni successive

            if left_side:
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