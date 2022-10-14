from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

arr = []

for i in range(0, 20):
    arr.append([pow(i,2), -i])
    arr.append([pow(i,2), i])

# for i in range(0, 20):
#     arr.append([pow(i,2), i])

arr = np.array(arr)

print(arr)

x = arr[:,0]
y = arr[:,1]

print("x:", x)
print("y:", y)


# use bc_type = 'natural' adds the constraints as we described above
f = CubicSpline(x, y, bc_type='natural')
x_new = np.linspace(0, 2, 100)
y_new = f(x_new)

plt.figure(figsize = (10,8))
plt.plot(x_new, y_new, 'b')
plt.plot(x, y, 'ro')
plt.title('Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()