# Regression ##

## Simple Linear Regression #
Dependence of output variable onto the single input variable.
y = m*x + c

![Simple Linear Regression](http://latex.codecogs.com/png.latex?Y%3DB_%7Bo%7D&plus;B_%7B1%7D%20x)

The goal is to find the best estimates for the coefficients to minimize the errors in predicting y from x.

![B1](http://latex.codecogs.com/png.latex?B_%7B1%7D%3D%5Csum%20%28x_%7Bi%7D-%5Coverline%7Bx%7D%29%28y_%7Bi%7D-%5Coverline%7By%7D%29/%5Csum%20%28x_%7Bi%7D-%5Coverline%7Bx%7D%29%5E%7B2%7D)

![B0](http://latex.codecogs.com/png.latex?B_%7Bo%7D%3D%5Coverline%7By%7D-B_%7B1%7D%20%5Coverline%7Bx%7D)



covariance(x,y) = sum((x(i) - mean(x)) * (y(i) - mean(y)))

B1 = covariance(x, y)  /  variance(x)

B0 = mean(y) - B1 * mean(x)

## Stochastic Gradient Descent Linear Regression

### Model Representation ##
![Model](https://cdn-images-1.medium.com/max/1600/1*XfDb8XhzTy1nVnwSy1mv6g.png)

### Cost Function ##

One common function that is often used is mean squared error, which measure the difference between the estimator (the dataset) and the estimated value (the prediction). It looks like this:
![Cost Function](https://cdn-images-1.medium.com/max/1600/1*20m_U-H6EIcxlN2k07Z7oQ.png)

It turns out we can adjust the equation a little to make the calculation down the track a little more simple. We end up with:
![Final Cost Function](https://cdn-images-1.medium.com/max/1600/1*VanG05Ab6yknqJ2bRGFzrQ.png)
It is represented by J(theta).


### Gradient Descent Algorithm ###

Gradient Descent basically just does what we were doing by hand — change the theta values, or parameters, bit by bit, until we hopefully arrived a minimum.

We start by initializing theta0 and theta1 to any two values, say 0 for both, and go from there. Formally, the algorithm is as follows:

![J(theta)](https://cdn-images-1.medium.com/max/1600/1*QKHtyn4Rr-0R-s0an1eSsA.png)

where α, alpha, is the learning rate, or how quickly we want to move towards the minimum. If α is too large, however, we can overshoot.

![Gradient Descent Visualization](https://cdn-images-1.medium.com/max/1600/1*WGHn1L4NveQ85nn3o7Dd2g.png)



## Logistic Regression ##
