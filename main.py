import math
from trees.BST import BST
from trees.AVL import AVL
from trees.RBT import RBT
from utils.RandomKeysHandler import RandomKeyHandler
from utils.MeasureTool import measure_insertion_time

def main():
    n_min = 1000
    n_max = 10000000
    num_punti = 100
    
    # rogressione geometrica
    c = (n_max / n_min) ** (1 / (num_punti - 1))
    
    # Generazione 100 valori di n 
    valori_n = [int(n_min * (c ** i)) for i in range(num_punti)]
    
    # rimozione eventuali duplicati causati dall'arrotondamento per difetto
    #valori_n = sorted(list(set(valori_n)))
    
    handler = RandomKeyHandler()
    alberi_da_testare = [
        ("BST", BST),
        ("AVL", AVL),
        ("RBT", RBT)
    ]
    
    print(f"{'n':>10} | {'BST (s)':>12} | {'AVL (s)':>12} | {'RBT (s)':>12}")
    print("-" * 55)

    for n in valori_n:
        risultati_n = {"n": n}
        
        for nome, classe_albero in alberi_da_testare:

            mediana = measure_insertion_time(classe_albero, n, handler)
            risultati_n[nome] = mediana
        
        print(f"{n:10d} | {risultati_n['BST']:12.8f} | {risultati_n['AVL']:12.8f} | {risultati_n['RBT']:12.8f}")
        
        # TO DO: salvare i dati

if __name__ == "__main__":
    main()



'''

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
        tree.print_tree()
        print("\n\n\n")
        tree.remove(10)
        tree.remove(20)
        tree.remove(30)
        tree.remove(40)
        tree.remove(50)
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

'''