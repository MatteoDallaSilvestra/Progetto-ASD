from trees.BST import BST
from trees.AVL import AVL
from trees.RBT import RBTree
#from trees.AVL import AVL  # Scommentato per il test prestazionale
from trees.BST import TreeNode
#from trees.RBT import RBT  # Scommentato per il test prestazionale
from utils.RandomKeysHandler import RandomKeyHandler
from utils.MeasureTool import measure_insertion_time
from utils.DataStorage import DataStorage

def main():

    #provaAVL()
    #provaBST()
    '''
    handler = RandomKeyHandler()
    tree = AVL()
    handler.update_working_set(10)
    handler.populateTree(tree)
    print("Albero AVL popolato con 10 nodi:")
    print(tree.__str__())

    node_to_insert = handler.get_node_to_insert()
    print(f"Inserimento chiave {node_to_insert.key}...")
    tree.insert(node_to_insert)
    print("Albero AVL dopo inserimento:")
    print(tree.__str__())
    

    handler.remove_key(tree)
    print("Albero AVL dopo rimozione di una chiave a caso:")
    print(tree.__str__())
    print(handler.print_working_set())
    print(handler.print_working_nodes())
'''

    # PARTE 2: TEST PRESTAZIONALE (IMPLEMENTAZIONE COMPLETA)
    n_min = 1000
    n_max = 1000000
    num_punti = 100
    
    # Calcolo della ragione per la progressione geometrica
    c = (n_max / n_min) ** (1 / (num_punti - 1))
    
    # Generazione dei 100 valori di n (progressione geometrica)
    valori_n = sorted(list(set([int(n_min * (c ** i)) for i in range(num_punti)])))

    handler = RandomKeyHandler()
    tutti_i_risultati = []
    
    # Intestazione tabella
    print(f"{'n':>10} | {'BST (s)':>12} | {'AVL (s)':>12} | {'RBT (s)':>12}")
    print("-" * 55)

    for n in valori_n:
        # Misurazione tempi di inserimento per le tre strutture
        t_bst = measure_insertion_time(BST, n, handler)
        t_avl = measure_insertion_time(AVL, n, handler)
        t_rbt = measure_insertion_time(RBTree, n, handler)

        # Memorizzazione risultati
        tutti_i_risultati.append((n, t_bst, t_avl, t_rbt))
        
        # Stampa a video in tempo reale
        print(f"{n:10d} | {t_bst:12.8f} | {t_avl:12.8f} | {t_rbt:12.8f}")
        
    # Salvataggio finale su file CSV
    DataStorage.save_to_csv("results.csv", tutti_i_risultati)
    print("\nSimulazione completata. Risultati salvati in 'results.csv'.")

'''
def provaAVL():
    nodes = [TreeNode(i) for i in range(1, 11)]
    avl_tree = AVL()
    for node in nodes:
        avl_tree.insert(node)
        print(f"Inserito {node.key}:")
        print(avl_tree.__str__())


def provaBST():
    nodes = [TreeNode(i) for i in range(1, 11)]
    bst_tree = RBTree()
    for node in nodes:
        bst_tree.insert(node)
        print(f"Inserito {node.key}:")
        print(bst_tree.__str__())
    print(bst_tree.print_tree())
'''

if __name__ == "__main__":
    main()
