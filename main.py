
from trees.BST import BST
from trees.RBT import RBT
from trees.AVL import AVL
from utils.RandomKeysHandler import RandomKeyHandler

def generateAVL():
        tree = AVL()
        tree.insert(10)
        tree.insert(20)
        tree.insert(30)      
        tree.insert(40)
        tree.insert(50)
        tree.insert(25)
        tree.insert(5)
        tree.insert(15)
        tree.insert(35)
        tree.insert(45)
        tree.insert(55)
        tree.insert(3)
        tree.insert(7)
        tree.insert(13)
        tree.insert(17)
        tree.insert(33)
        tree.insert(37)
        tree.insert(43)
        tree.insert(47)
        tree.remove(10)
        tree.remove(20)
        tree.remove(30)
        tree.remove(40)
        tree.remove(50)
        tree.print_tree()

    
def generateRBT():
        tree = RBT()
        tree.insert(10)
        tree.insert(20)
        tree.insert(30)      
        tree.insert(40)
        tree.insert(50)
        tree.insert(25)
        tree.insert(5)
        tree.insert(15)
        tree.insert(35)
        tree.insert(45)
        tree.insert(55)
        tree.insert(3)
        tree.insert(7)
        tree.insert(13)
        tree.insert(17)
        tree.insert(33)
        tree.insert(37)
        tree.insert(43)
        tree.insert(47)
        '''tree.remove(10)
        tree.remove(20)
        tree.remove(30)
        tree.remove(40)
        tree.remove(50)'''
        tree.print_tree()



def random_gen():
    random_generator = RandomKeyHandler()
    random_generator.update_working_set(10)
    random_generator.print_working_set()
    tree = BST()
    random_generator.populateTree(tree)
    tree.print_tree()
    tree.insert(random_generator.get_key_to_insert())
    random_generator.print_working_set()
    tree.print_tree()
    random_generator.remove_key(tree)

    
    
    
   
    


    
    


class main:
    def __init__(self):
        random_gen()
        #generateRBT()
        
        
       
    
    

if __name__ == "__main__":
    main()