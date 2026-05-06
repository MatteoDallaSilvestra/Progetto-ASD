
from BST import BST
from TreeNode import TreeNode
from AVLTreeNode import AVLTreeNode
from AVL import AVL


class main:
    def __init__(self):
        
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
        
       
        
        
        

if __name__ == "__main__":
    main()