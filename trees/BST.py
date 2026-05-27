#Class BST 
#Contains the implementation of Binary Search Tree and its operations


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

    


class BST():
    def __init__(self, root = None):
        self.root = root

    def attach_left(self, parent_node, child_node):
        if child_node is not None and parent_node is not None:
            parent_node.left = child_node
            child_node.parent = parent_node

    def attach_right(self, parent_node, child_node):
        if child_node is not None and parent_node is not None:
            parent_node.right = child_node
            child_node.parent = parent_node

    def detach_left(self, parent_node):
        detached_node = parent_node.left
        if detached_node is not None:
            parent_node.left = None
            detached_node.parent = None
        return detached_node

    def detach_right(self, parent_node):
        detached_node = parent_node.right
        if detached_node is not None:
            parent_node.right = None
            detached_node.parent = None
        return detached_node
    
    def __str__(self):
        if self.root == None:
            return "NULL "
        else:
            return f"{self.root.key} " + BST(self.root.left).__str__() + BST(self.root.right).__str__()
        
    
    def find(self, key):
        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                return current_node
            elif key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None
    
    def nxt(self, node):
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        else:
            parent_node = node.parent
            while parent_node is not None and node == parent_node.right:
                node = parent_node
                parent_node = parent_node.parent
            return parent_node
        

    def prv(self, node):
        if node.left is not None:
            node = node.left
            while node.right is not None:
                node = node.right
            return node
        else:
            parent_node = node.parent
            while parent_node is not None and node == parent_node.left:
                node = parent_node
                parent_node = parent_node.parent
            return parent_node
    

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
                succ = self.nxt(node_to_remove.right)
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
            succ = self.nxt(node_to_remove.right)
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
        
    def rotate_left(self, node):
        right_subtree = BST()
        beta = BST()

        if node == self.root:
            right_subtree.root = self.detach_right(node)
            if right_subtree.root is not None:
                beta.root = right_subtree.detach_left(right_subtree.root)
            if beta.root is not None:
                self.attach_right(node, beta.root)
            self.attach_left(right_subtree.root, node)    
            self.root = right_subtree.root
        else:
            parent_node = node.parent
            if parent_node.left == node:
                right_subtree.root = self.detach_right(node)
                if right_subtree.root is not None:
                    beta.root = right_subtree.detach_left(right_subtree.root)
                if beta.root is not None:
                    self.attach_right(node, beta.root)
                self.attach_left(right_subtree.root, node)    
                self.attach_left(parent_node, right_subtree.root)
            else:
                right_subtree.root = self.detach_right(node)
                if right_subtree.root is not None:
                    beta.root = right_subtree.detach_left(right_subtree.root)
                if beta.root is not None:
                    self.attach_right(node, beta.root)
                self.attach_left(right_subtree.root, node)    
                self.attach_right(parent_node, right_subtree.root)

    def rotate_right(self, node):
        left_subtree = BST()
        beta = BST()

        if node == self.root:
            left_subtree.root = self.detach_left(node)
            if left_subtree.root is not None:
                beta.root = left_subtree.detach_right(left_subtree.root)
            if beta.root is not None:
                self.attach_left(node, beta.root)
            self.attach_right(left_subtree.root, node)    
            self.root = left_subtree.root
        else:
            parent_node = node.parent
            if parent_node.left == node:
                left_subtree.root = self.detach_left(node)
                if left_subtree.root is not None:
                    beta.root = left_subtree.detach_right(left_subtree.root)
                if beta.root is not None:
                    self.attach_left(node, beta.root)
                self.attach_right(left_subtree.root, node)    
                self.attach_left(parent_node, left_subtree.root)
            else:
                left_subtree.root = self.detach_left(node)
                if left_subtree.root is not None:
                    beta.root = left_subtree.detach_right(left_subtree.root)
                if beta.root is not None:
                    self.attach_left(node, beta.root)
                self.attach_right(left_subtree.root, node)    
                self.attach_right(parent_node, left_subtree.root)
        

