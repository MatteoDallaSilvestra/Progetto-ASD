class TreeNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self

class BST():
    def __init__(self, root = None):
        self.root = root

    def attach_left(self, parent_node, child_node):
        if child_node is not None and parent_node is not None:
            parent_node.left = child_node
            child_node.parent = parent_node

    def attach_right(self, parent_node, child_node):
        if child_node is not None and parent_node is not None:
            parent_node.right = child_node
            child_node.parent = parent_node

    def detach_left(self, parent_node):
        detached_node = parent_node.left
        if detached_node is not None:
            parent_node.left = None
            detached_node.parent = None
        return detached_node

    def detach_right(self, parent_node):
        detached_node = parent_node.right
        if detached_node is not None:
            parent_node.right = None
            detached_node.parent = None
        return detached_node
    
    def __str__(self):
        if self.root == None:
            return "NULL "
        else:
            return f"{self.root.key} " + BST(self.root.left).__str__() + BST(self.root.right).__str__()
        
    def find(self, key):
        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                return current_node
            elif key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None
    
    def nxt(self, node):
        # Se riceve un intero (chiave), trova il nodo
        if isinstance(node, int):
            node = self.find(node)
        if node is None: return None
        
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        else:
            parent_node = node.parent
            while parent_node is not None and node == parent_node.right:
                node = parent_node
                parent_node = parent_node.parent
            return parent_node

    def prv(self, node):
        # Se riceve un intero (chiave), trova il nodo
        if isinstance(node, int):
            node = self.find(node)
        
        if node is None: return None

        if node.left is not None:
            node = node.left
            while node.right is not None:
                node = node.right
            return node
        else:
            parent_node = node.parent
            while parent_node is not None and node == parent_node.left:
                node = parent_node
                parent_node = parent_node.parent
            return parent_node

    def insert(self, node):

        if self.root is None:
            self.root = node
            return

        curr = self.root
        while True:
            if node.key < curr.key:
                if curr.left is None:
                    self.attach_left(curr, node)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    self.attach_right(curr, node)
                    break
                else:
                    curr = curr.right

    def remove(self, n):# rimozione nodo n da albero
        if n is None: # caso in cui il nodo sia nullo
            return
        if n.left is None or n.right is None: # controllo se uno dei due figli di n è nullo
            y = n # y diventa nodo da eliminare
        else:
            y = self.nxt(n)# lo sostituisco col suo successore
        if y.left is not None:# se il figlio sinistro non è nullo
            x = y.left #salvo figlio sinistro
        else:
            x = y.right #altrimenti salvo quello destro
        if x is not None: # controllo che x non sia nullo
            x.parent = y.parent # collego al genitore di y
        if y.parent is None: # se scopro che il genitore non è valido
            self.root = x # allora x deve diventare la root
        elif y == y.parent.left: #caso in cui y è il figlio sinistro
            y.parent.left = x
        else: # caso in cui y è il figlio destro
            y.parent.right = x
        if y != n: # caso in cui ho 2 figli
            n.key = y.key

    def rotate_right(self, node):
        if node is None or node.left is None: return
        
        x = self.detach_left(node)
        beta = self.detach_right(x)
        
        parent = node.parent
        if parent is None:
            self.root = x
        elif parent.left == node:
            self.detach_left(parent)
            self.attach_left(parent, x)
        else:
            self.detach_right(parent)
            self.attach_right(parent, x)
            
        self.attach_left(node, beta)
        self.attach_right(x, node)