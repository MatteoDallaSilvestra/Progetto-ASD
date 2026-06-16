# Class AVl Tree 
# Contains the implementation of AVL Tree and its operations
from .BST import BST


def height(node):
    if node == None:
        return 0
    if getattr(node, "height", None) is None:
        node.height = 1 + max(height(node.left), height(node.right))
    return node.height

def invalidate_height(node):
    while node != None:
        node.height = None
        node = node.parent


class AVL(BST):
    def __init__(self, root = None):
        super().__init__(root)

    def balance_factor(self, node):
        if node.left is None and node.right is None:
            return 0
        return height(node.left) - height(node.right)
    
    def rotate_left(self, node):
        right_child = node.right
        super().rotate_left(node)

        if node is not None:
            node.height = None
        if right_child is not None:
            right_child.height = None

    def rotate_right(self, node):
        left_child = node.left
        super().rotate_right(node)

        if node is not None:
            node.height = None
        if left_child is not None:
            left_child.height = None

    def rebalance(self, node):
        invalidate_height(node)

        while node is not None:
            parent = node.parent
            balance = self.balance_factor(node)

            if balance > 1:
                if self.balance_factor(node.left) < 0:
                    self.rotate_left(node.left)
                self.rotate_right(node)
                invalidate_height(parent if parent is not None else self.root)
    
            elif balance < -1:
                if self.balance_factor(node.right) > 0:
                    self.rotate_right(node.right)
                self.rotate_left(node)
                invalidate_height(parent if parent is not None else self.root)

            node = parent

    def insert(self, node):
        super().insert(node)
        self.rebalance(node)


    def remove(self, node):
        
        if node is None:
            return (None, None)
        

        has_two_children = node.left is not None and node.right is not None
        
        if not has_two_children:
            physical_deleted_node = node
        else:            
            physical_deleted_node = self.nxt(node)

        rebalance_start_node = physical_deleted_node.parent


        (a,b) = super().remove(node)

        if has_two_children and node is not None:
            invalidate_height(node)
            
        
        if rebalance_start_node is not None:
            self.rebalance(rebalance_start_node)
        elif self.root is not None:
            self.rebalance(self.root)


        return (a,b)