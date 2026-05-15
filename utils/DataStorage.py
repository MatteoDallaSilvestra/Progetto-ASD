# Stores data in a dataframe and allows for easy access and manipulation of the data.
import pandas as pd

class DataStorage:
    def __init__(self):
        self._data = []
    
    def add_data(self, tree_type: str, key: int, insert_time: float):
        self._data.append({
            "Tree Type": tree_type,
            "Key": key,
            "Insert Time": insert_time
        })

    def get_dataframe(self):
        return pd.DataFrame(self._data)