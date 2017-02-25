'''
Created on Feb 15, 2017

@author: Rahil
'''
#Decision Tree-Iris Example Code

## 1-Import Dataset 
from sklearn.datasets import load_iris
iris=load_iris()
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]
for i in range(len(iris.target)):
    print "Example %d: label %s, features %s" % (i,iris.data[i],iris.target[i])
