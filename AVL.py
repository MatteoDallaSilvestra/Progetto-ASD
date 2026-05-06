# Class AVl Tree 
# Contains the implementation of AVL Tree and its operations
from AVLTreeNode import AVLTreeNode
from BinaryTree import BinaryTree

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
            node.calculate_height()
            node.calculate_bf()
            balance = node.bf

            if balance > 1 or balance < -1:
                if balance > 1:
                    if node.left.bf < 0:
                        self.rotate_left(node.left)
                    self.rotate_right(node)
                    
                    

                elif balance < -1:
                    if node.right.bf > 0:
                        self.rotate_right(node.right)
                    self.rotate_left(node)
            else:
                node = node.parent

            
                    

    