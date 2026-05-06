# Class AVl Tree 
# Contains the implementation of AVL Tree and its operations
from AVLTreeNode import AVLTreeNode
from BinaryTree import BinaryTree

class AVL(BinaryTree):

    def __init__(self, root=None):
        super().__init__(root)
        if self.root:
            self.root.height = 1