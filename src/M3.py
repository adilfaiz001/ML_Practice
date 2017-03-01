'''
Created on Feb 16, 2017

@author: Rahil
'''
##Features usefulness and correlation 
##Avoid useless features and make use of independent features 
##Dont use multiple features of same kind 

import numpy as np
import matplotlib.pyplot as plt

greyhounds=500
labs=500

grey_height=28+4*np.random.randn(greyhounds)
lab_height=24+4*np.random.randn(labs)

plt.hist([grey_height,lab_height],stacked=True,color=['r','b'])
plt.show()