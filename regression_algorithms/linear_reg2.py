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

    dataset = np.divide(dataset-min_col,max_col-min_col)
    return dataset

def cross_validation_split(dataset,n_folds):
    dataset_split=list()
    dataset_copy = dataset
    fold_size = int(len(dataset)/n_folds)
    i=0
    for n in xrange(n_folds):
        folds=dataset_copy[i:fold_size+1]
        i = (i+1)*(fold_size+1)
        dataset_split.append(folds)
        
    print (dataset_split[0])    

    
def coefficient_sgd(train,l_rate,n_epoch):
    coef=np.array([np.random.randn(len(train[0]),1)])
    
    


    
df = load_data('winequality-white.csv')
df = normalize_dataset(df)
df = cross_validation_split(df,5)