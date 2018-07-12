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
    print dataset.shape
    return dataset

    
load_data('winequality-white.csv')