import matplotlib.pyplot as plt
import numpy as np
import math 
import cv2
import numpy as np
from scipy.optimize import curve_fit

def getSciOptime(points):
 
    x = np.linspace(0, 10, num = 40)
    
    # y is another array which stores 3.45 times
    # the sine of (values in x) * 1.334.
    # The random.normal() draws random sample
    # from normal (Gaussian) distribution to make
    # them scatter across the base line
    y = 3.45 * np.sin(1.334 * x) + np.random.normal(size = 40)
    
    # Test function with coefficients as parameters
    def test(x, a, b):
        return a * np.sin(b * x)
    
    # curve_fit() function takes the test-function
    # x-data and y-data as argument and returns
    # the coefficients a and b in param and
    # the estimated covariance of param in param_cov
    param, param_cov = curve_fit(test, x, y)
    
    
    print("Sine function coefficients:")
    print(param)
    print("Covariance of coefficients:")
    print(param_cov)
    
    # ans stores the new y-data according to
    # the coefficients given by curve-fit() function
    ans = (param[0]*(np.sin(param[1]*x)))

def getPolynomialFitFunction(points):
    # get x and y vectors
    x = points[:,0]
    y = points[:,1]

    # calculate polynomial
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)

    # calculate new x's and y'sq
    x_new = np.linspace(x[0], x[-1], 3)
    y_new = f(x_new)

    plt.plot(x,y,'o', x_new, y_new)
    plt.xlim([x[0]-1, x[-1] + 1 ])
    plt.show()

    return f

def main():
    arr = []

    for i in range(0, 20):
        arr.append([pow(i,2), -i])
    for i in range(0, 20):
        arr.append([pow(i,2), i])
    
    arr = np.array(arr)
    print(arr)
    f = getPolynomialFitFunction(arr)
    #print(f(19*19))


if __name__ == "__main__":
    main()