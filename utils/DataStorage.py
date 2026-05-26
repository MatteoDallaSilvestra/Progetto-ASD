# Stores data in a dataframe and allows for easy access and manipulation of the data.
import pandas as pd
import csv

class DataStorage:
    
    @staticmethod
    def save_to_csv(filename, results):

        headers = ['n', 'BST', 'AVL', 'RBT']
        
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(results)
                
            print(f"Dati salvati con successo in {filename}")
        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")