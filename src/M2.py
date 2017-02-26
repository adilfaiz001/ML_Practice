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

#Separating Training Data and Testing data
import numpy as np
test_idx=[0,50,100]
#Training Data
train_target=np.delete(iris.target,test_idx)
train_data=np.delete(iris.data,test_idx, axis=0)

#Testing 
test_target=iris.target[test_idx]
test_data=iris.data[test_idx]

#Training Tree Classifier
from sklearn import tree
clf=tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)


print test_target
print clf.predict(test_data)

#viz code
from sklearn.externals.six import StringIO
import pydot
dot_data=StringIO()
tree.export_graphviz(clf, out_file=dot_data, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         impurity=False)  
graph=pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf('iris.pdf')

