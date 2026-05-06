# Represents a node of an AVL tree, which is a self-balancing binary search tree. It inherits from TreeNode and adds an attribute for the height of the node.

from TreeNode import TreeNode

class AVLTreeNode(TreeNode):
    def __init__(self, key, left = None, right = None, bf = 0, height = 1):
        super().__init__(key, left, right)
        self.bf = bf
        self.height = height
        self.parent = None
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self

    def calculate_height(self):
        height_left = self.left.height if self.left else 0
        height_right = self.right.height if self.right else 0
        self.height = 1 + max(height_left, height_right)
    
    def calculate_bf(self):
        height_left = self.left.height if self.left else 0
        height_right = self.right.height if self.right else 0
        self.bf = height_left - height_right