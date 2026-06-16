# Provides operation to measure the execution time of a function and store the results in a dataframe.

import gc
import time
import statistics

def measure_insertion_time(tree_type, n, key_handler):
    # handler per la dimensione n
    key_handler.update_working_set(n)
    
    # 2. Creazione albero e popolamento
    tree = tree_type()
    key_handler.populateTree(tree)
    
    times = []
    
    # Misurazioni
    for _ in range(100):  # 100 misurazioni per ogni n  
        # Chiave esterna da inserire
        node_to_insert = key_handler.get_node_to_insert()
        
        # MISURAZIONE CRONOMETRATA
        start = time.perf_counter()
        tree.insert(node_to_insert)
        end = time.perf_counter()
        
        times.append(end - start)
        
        # Rimossa chiave a caso (per riporate a n)
        # (fase non cronometrata)
        key_handler.remove_key(tree)

    # Libera subito l'istanza dell'albero usata per questa misura.
    del node_to_insert
    del tree
    gc.collect()
    
    # mediana
    return statistics.median(times)
