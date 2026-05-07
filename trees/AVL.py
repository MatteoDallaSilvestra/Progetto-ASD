# Class AVl Tree 
# Contains the implementation of AVL Tree and its operations
from .AVLTreeNode import AVLTreeNode
from .BinaryTree import BinaryTree

class AVL(BinaryTree):

    def __init__(self, root=None):
        super().__init__(root)

    def insert(self, key):
        new_node = AVLTreeNode(key)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            while True:
                if key < curr.key:
                    if curr.left is None:
                        curr.left = new_node
                        new_node.parent = curr
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = new_node
                        new_node.parent = curr
                        break
                    else:
                        curr = curr.right
        self.rebalance(new_node)
    
    def rebalance(self, node):
        while node is not None:
            # Save parent before rotations change the structure and node.parent
            parent = node.parent

            node.calculate_height()
            node.calculate_bf()
            balance = node.bf

            if balance > 1: # Left heavy
                if node.left.bf < 0: # Left-Right case
                    self.rotate_left(node.left)
                self.rotate_right(node)
            elif balance < -1: # Right heavy
                if node.right.bf > 0: # Right-Left case
                    self.rotate_right(node.right)
                self.rotate_left(node)
            
            # Move up to the original parent to continue checking
            node = parent

    def remove(self, key):
        node_to_remove = self.find(key)
        if node_to_remove is None:
            return
        
        if node_to_remove.left is not None and node_to_remove.right is not None:
            successor = self.find_min(node_to_remove.right)
            node_to_remove.key = successor.key
            node_to_remove = successor
        
        child = node_to_remove.left if node_to_remove.left else node_to_remove.right
        parent = node_to_remove.parent

        if child is not None:
            child.parent = parent
        
        if parent is None:
            self.root = child
        elif parent.left == node_to_remove:
            parent.left = child
        else:
            parent.right = child
        
        self.rebalance(parent)

            
                    

    