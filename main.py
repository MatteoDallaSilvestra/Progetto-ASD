
from BST import BST
from TreeNode import TreeNode


class main:
    def __init__(self):
        
        tree = BST(TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8)), TreeNode(15, TreeNode(12), TreeNode(18))))
        tree.print_tree()
        tree.rotate_left(tree.root)
        tree.print_tree()
       
        
        
        

if __name__ == "__main__":
    main()