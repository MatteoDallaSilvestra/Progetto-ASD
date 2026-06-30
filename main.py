from trees.BST import BST
from trees.AVL import AVL
from trees.RBT import RBTree
from utils.RandomKeysHandler import RandomKeyHandler
from utils.MeasureTool import measure_insertion_time
from utils.DataStorage import DataStorage

def main():

    # PARTE 2: TEST PRESTAZIONALE
    n_min = 1000
    n_max = 1000000
    num_punti = 100
    
  
    c = (n_max / n_min) ** (1 / (num_punti - 1))
    
    # Generazione dei 100 valori di n (progressione geometrica)
    valori_n = sorted(list(set([int(n_min * (c ** i)) for i in range(num_punti)])))

    handler = RandomKeyHandler()
    tutti_i_risultati = []
    
    print(f"{'n':>10} | {'BST (s)':>12} | {'AVL (s)':>12} | {'RBT (s)':>12}")
    print("-" * 55)

    for n in valori_n:
        # Misurazione tempi di inserimento per le tre strutture
        t_bst = measure_insertion_time(BST, n, handler)
        t_avl = measure_insertion_time(AVL, n, handler)
        t_rbt = measure_insertion_time(RBTree, n, handler)

        # Memorizzazione risultati
        tutti_i_risultati.append((n, t_bst, t_avl, t_rbt))
        
        print(f"{n:10d} | {t_bst:12.8f} | {t_avl:12.8f} | {t_rbt:12.8f}")

    DataStorage.save_to_csv("results.csv", tutti_i_risultati)
    print("\nSimulazione completata. Risultati salvati in 'results.csv'.")

if __name__ == "__main__":
    main()