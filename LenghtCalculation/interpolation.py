from scipy.interpolate import Rbf, InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
from scipy import interpolate
from matplotlib import cm
import numpy as np

def onedInterpolation():
    arr = []
    for i in range(-19, 20):
        arr.append([pow(i,2), i])

    arr = np.asarray(arr)
    x = arr[:,0]
    y = arr[:,1]
    f = interpolate.interp1d(x, y)

    xnew = np.arange(0, 350, 0.1)
    ynew = f(xnew)   # use interpolation function returned by `interp1d`
    plt.plot(x, y, 'o', xnew, ynew, '-')
    plt.show()

def twodInterpolation():
    # 2-d interpolation
    rng = np.random.default_rng()
    x = rng.random(100)*4.0-2.0
    y = rng.random(100)*4.0-2.0
    z = x*np.exp(-x**2-y**2)
    edges = np.linspace(-2.0, 2.0, 101)
    centers = edges[:-1] + np.diff(edges[:2])[0] / 2.
    XI, YI = np.meshgrid(centers, centers)

    rbf = Rbf(x, y, z, epsilon=2)
    ZI = rbf(XI, YI)

    plt.subplot(1, 1, 1)
    X_edges, Y_edges = np.meshgrid(edges, edges)
    lims = dict(cmap='RdBu_r', vmin=-0.4, vmax=0.4)
    plt.pcolormesh(X_edges, Y_edges, ZI, shading='flat', **lims)
    plt.scatter(x, y, 100, z, edgecolor='w', lw=0.1, **lims)
    plt.title('RBF interpolation - multiquadrics')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.colorbar()
    plt.show()

def cubicspline():
    arr = []
    for i in range(-19, 20):
        if(i % 2 == 1):
            arr.append([pow(i,2), i])
        else:
            arr.append([pow(i,2), i])

    arr = np.asarray(arr)
    arr = arr[arr[:,0].argsort()]

    arr2 =[]
    for i in range(0, len(arr)):
        coord = arr[i]
        x = coord[0]
        y = coord[1]
        if(i % 2 == 0):
            arr2.append([x, y])
      
    
    arr2 = np.asarray(arr2)
    arr2 = arr2[arr2[:,0].argsort()]
       

    x = arr2[:,0]
    y = arr2[:,1]

    # x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
    # y = np.sin(x)
    
    # for i in range(0, len(x)):
    #     print(f"x:{x[i]} y:{y[i]}")
    
    tck = interpolate.splrep(x, y, s=0)
    xnew = np.arange(0, 361)
    ynew = interpolate.splev(xnew, tck, der=0)
    print("dneeme", interpolate.splev(154, tck, der=0))

    plt.figure()
    plt.plot(x, y, 'x', xnew, ynew, x, y, 'b')
    plt.title('Cubic-spline interpolation')
    plt.show()

def interpolatedUnivariateSpline():
    x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
    y = np.sin(x)
    s = interpolate.InterpolatedUnivariateSpline(x, y)
    xnew = np.arange(0, 2*np.pi, np.pi/50)
    ynew = s(xnew)

    plt.figure()
    plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
    plt.legend(['Linear', 'InterpolatedUnivariateSpline', 'True'])
    plt.axis([-0.05, 6.33, -1.05, 1.05])
    plt.title('InterpolatedUnivariateSpline')
    plt.show()

def radialBasisInterpolation():
    # setup data
    # x = np.linspace(0, 10, 9)
    # y = np.sin(x)

    arr = []
    for i in range(-19, 20):
        if(i % 2 == 1):
            arr.append([pow(i,2), i])
        else:
            arr.append([pow(i,2), i])

    arr = np.asarray(arr)
    arr = arr[arr[:,0].argsort()]

    arr2 =[]
    for i in range(0, len(arr)):
        coord = arr[i]
        x = coord[0]
        y = coord[1]
        if(i % 2 == 0):
            arr2.append([x, y])
      
    
    arr2 = np.asarray(arr2)
    arr2 = arr2[arr2[:,0].argsort()]
       
    print(arr)
    print("-----------")
    print(arr2)

    x = arr2[:,0]
    y = arr2[:,1]

    
    xi = np.linspace(0, 400, 101)


    ius = InterpolatedUnivariateSpline(x, y)
    yi = ius(xi)

    rbf = Rbf(x, y)
    fi = rbf(xi)

    plt.subplot(2, 1, 2)
    plt.plot(x, y, 'bo')
    plt.plot(xi, fi, 'g')
    #plt.plot(xi, np.sin(xi), 'r')
    plt.title('Interpolation using RBF - multiquadrics')
    plt.show()
    return rbf

  
def main():
    # onedInterpolation()
    # twodInterpolation()
    cubicspline()
    # interpolatedUnivariateSpline()
    # rbf = radialBasisInterpolation()
    # print("res", rbf(324))

if __name__ == "__main__":
    main()