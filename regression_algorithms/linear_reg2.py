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
    
def predict(dataset,coefficient):
    X=dataset[:,:-1]
    Y=dataset[:,-1]
    X=X.T
    ap=np.array([1]*X.shape[1])
    X=np.insert(X,0,ap, axis = 0)
    yhat = np.multiply(coefficient,X)
    return yhat
    
    
def coefficient_sgd(train,l_rate,n_epoch):
    coef=np.array([np.random.randn(len(train[0]),1)]*0.01)
    for epoch in range(n_epoch):
        yhat=predict(train,coef)
        error=sum(yhat-train[:,-1])
        coef[0] = coef[0] - l_rate * error
        for row in train:
            for i in range(1,train.shape[1]):
                coef[i] = coef[i] - l_rate * error * row[i] 
    return coef
    
def linear_regression_sgd(train,test,l_rate,n_epoch):    
    
def evaluate_algorithm(dataset,algorithm,n_folds,*args):

    
df = load_data('winequality-white.csv')
df = normalize_dataset(df)

predict(df,[0])
