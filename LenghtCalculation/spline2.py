import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt

def scipy_bspline(cv, n=100, degree=3, periodic=False):
    """ Calculate n samples on a bspline

        cv :      Array ov control vertices
        n  :      Number of samples to return
        degree:   Curve degree
        periodic: True - Curve is closed
    """
    cv = np.asarray(cv)
    count = cv.shape[0]

    # Closed curve
    if periodic:
        kv = np.arange(-degree,count+degree+1)
        factor, fraction = divmod(count+degree+1, count)
        cv = np.roll(np.concatenate((cv,) * factor + (cv[:fraction],)),-1, axis=0)
        degree = np.clip(degree,1,degree)

    # Opened curve
    else:
        degree = np.clip(degree,1,count-1)
        kv = np.clip(np.arange(count+degree+1)-degree,0,count-degree)

    # Return samples
    max_param = count - (degree * (1-periodic))
    spl = si.BSpline(kv, cv, degree)
    return spl(np.linspace(0,max_param,n))

def bspline(cv, n=100, degree=3, periodic=False):
    """ Calculate n samples on a bspline

        cv :      Array ov control vertices
        n  :      Number of samples to return
        degree:   Curve degree
        periodic: True - Curve is closed
                  False - Curve is open
    """

    # If periodic, extend the point array by count+degree+1
    cv = np.asarray(cv)
    count = len(cv)

    if periodic:
        factor, fraction = divmod(count+degree+1, count)
        cv = np.concatenate((cv,) * factor + (cv[:fraction],))
        count = len(cv)
        degree = np.clip(degree,1,degree)

    # If opened, prevent degree from exceeding count-1
    else:
        degree = np.clip(degree,1,count-1)


    # Calculate knot vector
    kv = None
    if periodic:
        kv = np.arange(0-degree,count+degree+degree-1)
    else:
        kv = np.clip(np.arange(count+degree+1)-degree,0,count-degree)

    # Calculate query range
    u = np.linspace(periodic,(count-degree),n)


    # Calculate result
    return np.array(si.splev(u, (kv,cv.T,degree))).T


def main():
    colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')

    arr = []

    for i in range(0, 20):
        arr.append([pow(i,2), -i])
    for i in range(0, 20):
        arr.append([pow(i,2), i])
    
    arr = np.array(arr)

    cv = np.array([[ 50.,  25.],
    [ 59.,  12.],
    [ 50.,  10.],
    [ 57.,   2.],
    [ 40.,   4.],
    [ 40.,   14.]])

    plt.plot(arr[:,0],arr[:,1], 'o-', label='Control Points')

    # p = bspline(arr,n=100,degree=10,periodic = False)
    # print(p)
    # x,y = p.T
    # plt.plot(x,y, color='r')

    for d in range(1,21):
        p = bspline(arr,n=100,degree=d,periodic = False)
        x,y = p.T
        plt.plot(x,y,'k-',label='Degree %s'%d,color=colors[d%len(colors)])
        print(f'------------------------Array {d}----------------------')
        print(p)

    plt.minorticks_on()
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 500)
    plt.ylim(-30, 30)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
   


if __name__ == "__main__":
    main()