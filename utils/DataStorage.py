# Stores data in a dataframe and allows for easy access and manipulation of the data.
import pandas as pd

class DataStorage:
    def __init__(self):
        self._data = []
    
    def add_data(self, tree_type: str, n: int, insert_time: float):
        self._data.append({
            "Tree Type": tree_type,
            "n": n,
            "Insert Time": insert_time
        })

    def get_dataframe(self):
        return pd.DataFrame(self._data)
    
    def get_csv(self, filename: str = "results.csv"):
        df = self.get_dataframe()
        df.to_csv(filename, index=False)
        print(f"Data successfully saved to {filename}")