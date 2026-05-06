#Class RBT, for Red-Black Tree
#Contains the implementation of Red-Black Tree and its operations
from RBTreeNode import RBTreeNode
from BinaryTree import BinaryTree

class RBT(BinaryTree):

    def __init__(self, root=None):
        super().__init__(root)
        if self.root:
            self.root.color = 'black'
        