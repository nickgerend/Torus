# Written by: Nick Gerend, @dataoutsider
# Viz: "Torus", enjoy!

import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# The Torus! Prolific in topology and pastries!
def Torus(theta, phi, r, R):
    x = (R+r*np.cos(theta*np.pi/180))*np.cos(phi*np.pi/180)
    y = (R+r*np.cos(theta*np.pi/180))*np.sin(phi*np.pi/180)
    z = r*np.sin(theta*np.pi/180)
    return x, y, z

scaler = 1.5
N = 360
n = int(360 * scaler)
theta = np.linspace(0.0,N,n)
phi = np.linspace(0.0,N,n)
T, P = np.meshgrid(theta, phi)

r = 0.65
R = 1.5 #0.85 is the perfect doughnut! (claimed by some articles)

Xgrid, Ygrid, Zgrid = Torus(T, P, r, R)
Xout = np.reshape(Xgrid, -1)
Yout = np.reshape(Ygrid, -1)
Zout = np.reshape(Zgrid, -1)
Tout = np.reshape(T, -1)
Pout = np.reshape(P, -1)

gridplot = plt.axes(projection='3d')
gridplot.plot_wireframe(Xgrid, Ygrid, Zgrid, color='g')
plt.show()

import csv
import os
with open(os.path.dirname(__file__) + '/Torus.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['index', 'x', 'y', 'z', 'theta', 'phi'])
    for i in range(len(Xout)):
        writer.writerow([(i+1), Xout[i], Yout[i], Zout[i], Tout[i], Pout[i]])
print('finished')