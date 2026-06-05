# Class AVl Tree 
# Contains the implementation of AVL Tree and its operations
from .BST import BST


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

    def _balance_factor(self, node):
        return height(node.left) - height(node.right)

    def _rebalance(self, node):
        while node is not None:
            invalidate_height(node)
            balance = self._balance_factor(node)

            if balance > 1:
                if self._balance_factor(node.left) < 0:
                    self.rotate_left(node.left)
                self.rotate_right(node)
            elif balance < -1:
                if self._balance_factor(node.right) > 0:
                    self.rotate_right(node.right)
                self.rotate_left(node)

            node = node.parent

    def insert(self, node):
        super().insert(node)
        self._rebalance(node)


    def remove(self, node):
        parent = node.parent
        if node is not None and node.left is not None and node.right is not None:
            successor = self.nxt(node)
            if successor is not None:
                parent = successor.parent

        (a,b) = super().remove(node)
        self._rebalance(parent)
        return (a,b)
      
