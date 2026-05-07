# Provides operations to build random trees while keep track of used keys to avoid duplicates.
# It uses a working set, which has to be updated every time we need to change the dimention of the tree. 
# Has a function to generate a random tree.
# Has a function to pick a random key to remove from the tree in order to use it as the key to insert in the next operation.

# In working set, keys after the used keys index are available for insertion, while keys before the used keys index are available for removal.




import random

class RandomKeyHandler:
    def __init__(self):
        self.dimension = 0
        self.working_set = None
        self.used_keys_index = 0

    def update_working_set(self, dimension):
        self.dimension = dimension
        self.working_set = [ i for i in range(1, dimension + 2) ]

    def swap_keys(self, index1, index2):
        temp = self.working_set[index1]
        self.working_set[index1] = self.working_set[index2]
        self.working_set[index2] = temp

    def populateTree(self, tree):
        while self.used_keys_index < self.dimension:
            self.swap_keys(self.used_keys_index, random.randint(self.used_keys_index, self.dimension))
            tree.insert(self.working_set[self.used_keys_index])
            self.used_keys_index += 1
        
       
    def get_key_to_insert(self):
        
        if self.used_keys_index >= self.dimension+1:
            raise Exception("No more keys available for insertion.")
        key = self.working_set[self.used_keys_index]
        self.used_keys_index += 1
        return key
    
    def remove_key(self, tree):
        if self.used_keys_index <= 0:
            raise Exception("No more keys available for removal.")
        key_index = random.randint(0, self.used_keys_index - 1)
        self.swap_keys(key_index, self.used_keys_index - 1)
        tree.remove(self.working_set[self.used_keys_index - 1])
        self.used_keys_index -= 1
        

    def print_working_set(self):
        print("Working set:", self.working_set)
        
        

    