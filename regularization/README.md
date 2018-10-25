# Regularization #

## Overfit in machine learning algorithms ##
![Overfitting](https://codingstartups.com/wp-content/uploads/2017/08/overfit.png)

Overfit can happen in linear models as well when dealing with multiple features. If not filtered and explored up front, some features can be more destructive than helpful, repeat information that already expressed by other features and add high noise to the dataset.

## Overcoming overfit using regularization ##
Because overfit is an extremely common issue in many machine learning problems, there are different approaches to solving it. The main concept behind avoiding overfit is simplifying the models as much as possible. Simple models do not (usually) overfit. On the other hand, we need to pay attention the to gentle trade-off between overfitting and underfitting a model.
One of the most common mechanisms for avoiding overfit is called regularization. Regularized machine learning model, is a model that its loss function contains another element that should be minimized as well.

## 1. Ridge Regression ##

![Ridge](http://latex.codecogs.com/png.latex?%5Cinline%20L%20%3D%20%5Csum%20%28%5Chat%7BY_%7Bi%7D%7D-Y_%7Bi%7D%29%5E%7B2%7D%20&plus;%20%5Clambda%20%5Csum%20%5Cbeta%20%5E%7B2%7D)

This loss function includes two elements. The first one is the one you’ve seen before – the sum of distances between each prediction and its ground truth.The second element though, a.k.a the regularization term.
It sums over squared β values and multiplies it by another parameter λ. The reason for doing that is to “punish” the loss function for high values of the coefficients β.<br/>
Ridge regression is an extension for linear regression. It’s basically a regularized linear regression model. The λ parameter is a scalar that should be learned as well, using a method called cross validation.<br/>
A super important fact we need to notice about ridge regression is that it enforces the β coefficients to be lower, but it does not enforce them to be zero. That is, it will not get rid of irrelevant features but rather minimize their impact on the trained model.<br/>


## 2. LASSO Method ##

Lasso is another extension built on regularized linear regression.

![LASSO](http://latex.codecogs.com/png.latex?%5Cinline%20L%20%3D%20%5Csum%20%28%5Chat%7BY_%7Bi%7D%7D-Y_%7Bi%7D%29%5E%7B2%7D%20&plus;%20%5Clambda%20%5Csum%20%5Cleft%20%7C%20%5Cbeta%20%5Cright%20%7C%20%5E%7B2%7D)

The only difference from Ridge regression is that the regularization term is in absolute value. But this difference has a huge impact on the trade-off we’ve discussed before. Lasso method overcomes the disadvantage of Ridge regression by not only punishing high values of the coefficients β but actually setting them to zero if they are not relevant. Therefore, you might end up with fewer features included in the model than you started with, which is a huge advantage.


## 3. Elastic Net ##
