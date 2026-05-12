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

    def remove(self, key):
        node_to_remove = self.find(key)
        if node_to_remove is None:
            return
        
        parent = node_to_remove.parent if node_to_remove.parent is not None else None
        
        #case 0: node to remove is the root
        if parent is None:
            if node_to_remove.left is None and node_to_remove.right is None:    #no children, the tree becomes empty
                self.root = None
                return
            elif node_to_remove.left is None or node_to_remove.right is None:   #one child, the child becomes the new root
                child = node_to_remove.left if node_to_remove.left else node_to_remove.right
                child.parent = None
                self.root = child
                return
            else:                                                               #two children, find the successor and replace the root with it
                succ = self.find_min(node_to_remove.right)
                node_to_remove.key = succ.key
                succ_parent = succ.parent
                child_subtree = self.detach_right(succ)
                if succ_parent.left == succ:
                    self.detach_left(succ_parent)
                    self.attach_left(succ_parent, child_subtree)
                else:
                    self.detach_right(succ_parent)
                    self.attach_right(succ_parent, child_subtree)
                return

        direction = "left" if parent.left == node_to_remove else "right"
        
        #case 1: node to remove has at most one child
        if node_to_remove.left is None or node_to_remove.right is None:
            child_subtree = self.detach_right(node_to_remove) if node_to_remove.left is None else self.detach_left(node_to_remove)
            if direction == "left":
                self.detach_left(parent)
                self.attach_left(parent, child_subtree)
            else:
                self.detach_right(parent)
                self.attach_right(parent, child_subtree)
            return

        #case 2: node to remove has two children
        else:
            succ = self.find_min(node_to_remove.right)
            node_to_remove.key = succ.key
            succ_parent = succ.parent
            child_subtree = self.detach_right(succ)
            if succ_parent.left == succ:
                self.detach_left(succ_parent)
                self.attach_left(succ_parent, child_subtree)
            else:
                self.detach_right(succ_parent)
                self.attach_right(succ_parent, child_subtree)
            return