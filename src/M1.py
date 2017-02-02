'''
Created on Feb 3, 2017

@author: Rahil
'''
#Hello World Problem-Machine learning_curve
'''
Supervised Machine Learning
        Training Data--->Train Classifier--->Make Predictons
'''

from sklearn import tree
features=[[140,1],[130,1],[170,0],[160,0]]
labels=[1,1,0,0]
clf=tree.DecisionTreeClassifier()
clf.fit(features,labels)
print clf.predict([[145,1]])

