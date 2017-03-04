'''
Created on Mar 5, 2017

@author: Rahil
'''
##Building the classifier from scratch
##Intro to k-NN algorithm
import random
class ScrapClassifier():
    '''
    classdocs
    '''


    def __init__(self,X_train,y_train):
        '''
        Constructor
        '''
        self.X_train=X_train
        self.y_train=y_train
        
    def fit(self,X_train,y_train):
        self.X_train=X_train
        self.y_train=y_train
    
    def predict(self,X_test):
        predictions=[]
        for row in X_test:
            label=random.choice(self.y_train)
            predictions.append(label)
        return predictions


from sklearn import datasets
iris=datasets.load_iris()

X=iris.data
y=iris.target

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train, y_test=train_test_split(X,y,test_size=.5)

##from sklearn.neighbors import KNeighborsClassifier 
clf=ScrapClassifier()

clf.fit(X_train, y_train)

pred=clf.predict(X_test)
##print pred

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,pred)
print accuracy
