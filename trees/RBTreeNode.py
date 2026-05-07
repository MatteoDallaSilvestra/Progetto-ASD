# Represent a node of a Red-Black Tree, which is a special kind of binary search tree. It contains information about the node's key, its color (red or black), its left and right children, and its parent.
from .TreeNode import TreeNode


class RBTreeNode(TreeNode):
    def __init__(self, key, color = 'red', left = None, right = None):
        super().__init__(key, left, right)
        self.color = color
        self.parent = None
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self