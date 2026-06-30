from trees.BST import TreeNode

import random

class RandomKeyHandler:
    def __init__(self):
        self.dimension = 0
        self.working_set = None
        self.working_nodes = None
        self.used_keys_index = 0

    def update_working_set(self, dimension):
        self.used_keys_index = 0
        self.dimension = dimension
        self.working_set = [ i for i in range(0, dimension + 1) ]
        self.working_nodes = [ TreeNode(i) for i in range(0, dimension + 1) ]
        self.used_keys_index = 0
        

    def swap_keys(self, index1, index2):
        temp = self.working_set[index1]
        self.working_set[index1] = self.working_set[index2]
        self.working_set[index2] = temp

    def swap_nodes(self, index1, index2):
        temp = self.working_nodes[index1]
        self.working_nodes[index1] = self.working_nodes[index2]
        self.working_nodes[index2] = temp

    def populateTree(self, tree):
        while self.used_keys_index < self.dimension:
            self.swap_keys(self.used_keys_index, random.randint(self.used_keys_index, self.dimension))
            tree.insert(self.working_nodes[self.working_set[self.used_keys_index]])
            self.used_keys_index += 1
        
    def get_node_to_insert(self):
        
        if self.used_keys_index >= self.dimension+1:
            raise Exception("No more keys available for insertion.")
        node = self.working_nodes[self.working_set[self.used_keys_index]]
        self.used_keys_index += 1
        return node

    def remove_key(self, tree):
        if self.used_keys_index <= 0:
            raise Exception("No more keys available for removal.")
        key_index = random.randint(0, self.used_keys_index - 1)
        self.swap_keys(key_index, self.used_keys_index - 1)
        (a,b) = tree.remove(self.working_nodes[self.working_set[self.used_keys_index - 1]])
        self.used_keys_index -= 1
        if a is not None and b is not None:
            self.swap_nodes(a,b)
        
    def print_working_set(self):
        print("Working set:", self.working_set)

    def print_working_nodes(self):
        print("Working nodes:", [node.key for node in self.working_nodes])