# Represents a node of an AVL tree, which is a self-balancing binary search tree. It inherits from TreeNode and adds an attribute for the height of the node.

from TreeNode import TreeNode

class AVLTreeNode(TreeNode):
    def __init__(self, key, left = None, right = None):
        super().__init__(key, left, right)
        self.height = 1
        self.parent = None
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self