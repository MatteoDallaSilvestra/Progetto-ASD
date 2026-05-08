#Class BST 
#Contains the implementation of Binary Search Tree and its operations

from .TreeNode import TreeNode
from .BinaryTree import BinaryTree

class BST(BinaryTree):
    def __init__(self, root = None):
        super().__init__(root)

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            while True:
                if key < curr.key:
                    if curr.left is None:
                        self.attach_left(curr, new_node)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        self.attach_right(curr, new_node)
                        break
                    else:
                        curr = curr.right