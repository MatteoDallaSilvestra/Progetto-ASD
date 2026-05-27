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

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if key < current_node.key:
                if current_node.left is None:
                    self.attach_left(current_node, new_node)
                    break
                current_node = current_node.left
            else:
                if current_node.right is None:
                    self.attach_right(current_node, new_node)
                    break
                current_node = current_node.right

        def rebalance(node):
            while node is not None:
                invalidate_height(node)
                balance = height(node.left) - height(node.right)

                if balance > 1:
                    if height(node.left.left) >= height(node.left.right):
                        self.rotate_right(node)
                    else:
                        self.rotate_left(node.left)
                        self.rotate_right(node)
                elif balance < -1:
                    if height(node.right.right) >= height(node.right.left):
                        self.rotate_left(node)
                    else:
                        self.rotate_right(node.right)
                        self.rotate_left(node)

                node = node.parent

        rebalance(new_node.parent)

    def remove(self, key):
        node_to_remove = self.find(key)
        if node_to_remove is None:
            return

        start_node = node_to_remove.parent
        if node_to_remove.left is not None and node_to_remove.right is not None:
            successor = self.nxt(node_to_remove.right)
            start_node = successor.parent if successor.parent is not None else node_to_remove

        super().remove(key)

        if start_node is None:
            start_node = self.root

        def rebalance(node):
            while node is not None:
                invalidate_height(node)
                balance = height(node.left) - height(node.right)

                if balance > 1:
                    if height(node.left.left) >= height(node.left.right):
                        self.rotate_right(node)
                    else:
                        self.rotate_left(node.left)
                        self.rotate_right(node)
                elif balance < -1:
                    if height(node.right.right) >= height(node.right.left):
                        self.rotate_left(node)
                    else:
                        self.rotate_right(node.right)
                        self.rotate_left(node)

                node = node.parent

        rebalance(start_node)
