import numpy as np
import matplotlib.pyplot as plt

#variables
m = 0.1
k = 100
L0 = 1.5
t = 10
ugaoUStepenima = 30

#constants
g = 9.81
dt = 1e-3
n = 1000*t

#starting point
teta = np.deg2rad(ugaoUStepenima)
r = L0
x = r*np.sin(teta)
y = -r*np.cos(teta)
X = np.zeros(n,float); X[0]=x
Y = np.zeros(n,float); Y[0]=y
vx = 0
vy = 0

#creating an array of positions
for i in range(1,n):
    ax = -k * (r - L0) * x / (m * r)
    ay = -k * (r - L0) * y/ (m * r) - g
    vx += ax * dt 
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    X[i] = x
    Y[i] = y
    r = np.sqrt(x * x + y * y)

#ploting
plt.figure()
plt.plot(X,Y)
plt.xlabel('x');
plt.ylabel('y');
plt.show()
