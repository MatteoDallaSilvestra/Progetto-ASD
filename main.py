from trees.BST import BST
#from trees.AVL import AVL  # Scommentato per il test prestazionale
from trees.BST import TreeNode
#from trees.RBT import RBT  # Scommentato per il test prestazionale
from utils.RandomKeysHandler import RandomKeyHandler
from utils.MeasureTool import measure_insertion_time
from utils.DataStorage import DataStorage

def main():
    """
    # PARTE 1: TEST MANUALE (Commentata come richiesto)
    nodes = [TreeNode(i) for i in range(1, 60)]

    tree = BST()
    tree.insert(nodes[9])  # 10
    tree.insert(nodes[10]) # 11
    tree.insert(nodes[11]) # 12
    tree.insert(nodes[12]) # 13
    tree.insert(nodes[13]) # 14 (indice 13 è 14 se range parte da 1)
    tree.insert(nodes[14]) # 15
    tree.insert(nodes[15]) # 16
    tree.insert(nodes[16]) # 17
    tree.insert(nodes[4])   # 5
    tree.insert(nodes[2])   # 3
    tree.insert(nodes[6])   # 7
    tree.insert(nodes[0])   # 1
    tree.insert(nodes[3])   # 4
    tree.insert(nodes[5])   # 6
    tree.insert(nodes[7])   # 8

    print("Tree prima della rimozione:")
    print(tree.__str__())

    tree.remove(nodes[9])  # 10
    tree.remove(nodes[10]) # 11
    tree.remove(nodes[11]) # 12

    print("Tree dopo la rimozione:")
    print(tree.__str__())
    """

    # PARTE 2: TEST PRESTAZIONALE (IMPLEMENTAZIONE COMPLETA)
    n_min = 1000
    n_max = 10000000
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
        #t_avl = measure_insertion_time(AVL, n, handler)
        #t_rbt = measure_insertion_time(RBT, n, handler)

        # Memorizzazione risultati
        tutti_i_risultati.append((n, t_bst, t_avl, t_rbt))
        
        # Stampa a video in tempo reale
        print(f"{n:10d} | {t_bst:12.8f} | {t_avl:12.8f} | {t_rbt:12.8f}")
        
    # Salvataggio finale su file CSV
    DataStorage.save_to_csv("results.csv", tutti_i_risultati)
    print("\nSimulazione completata. Risultati salvati in 'results.csv'.")

if __name__ == "__main__":
    main()