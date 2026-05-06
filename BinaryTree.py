from TreeNode import TreeNode

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def attach_left(self, parent_node, child_node):
        parent_node.left = child_node
        if child_node is not None:
            child_node.parent = parent_node

    def attach_right(self, parent_node, child_node):
        parent_node.right = child_node
        if child_node is not None:
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

    def rotate_left(self, node):
        working_tree = BinaryTree()
        right_subtree = BinaryTree()
        beta = BinaryTree()

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
        working_tree = BinaryTree()
        left_subtree = BinaryTree()
        beta = BinaryTree()

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
    

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.right is not None:
            self.print_tree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.key))
        if node.left is not None:
            self.print_tree(node.left, level + 1)


    def find_min(self, node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node