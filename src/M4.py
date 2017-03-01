'''
Created on Mar 1, 2017

@author: Rahil
'''
##Writing a pipeline
from sklearn import datasets
iris=datasets.load_iris()

X=iris.data
y=iris.target

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train, y_test=train_test_split(X,y,test_size=.5)

from sklearn.neighbors import KNeighborsClassifier 
clf=KNeighborsClassifier()

clf.fit(X_train, y_train)

pred=clf.predict(X_test)
##print pred

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,pred)
print accuracy

