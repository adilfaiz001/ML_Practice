'''
**Numpy implementation**

'''

import pandas as pd
import numpy as np 
from csv import reader

def load_data(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row[0].split(','))
    dataset = np.array(dataset)
    dataset=dataset.astype(np.float)
    return dataset
def normalize_dataset(dataset):
    max_col=np.max(dataset, axis = 0)
    min_col=np.min(dataset, axis = 0)
    dataset = dataset - min_col 
    print dataset[0]
    
    
df = load_data('winequality-white.csv')
normalize_dataset(df)