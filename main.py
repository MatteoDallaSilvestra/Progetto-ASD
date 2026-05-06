from RBTreeNode import RBTreeNode
from RBT import RBT


class main:
    def __init__(self):
        self.tree = RBT()
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.tree.insert(15)
        self.tree.insert(25)
        self.tree.insert(5)

if __name__ == "__main__":
    main()