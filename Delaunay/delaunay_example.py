from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np
NTheta = 26
NR = 8
a0 = 1.0

#define base rectangle (r,theta) = (u,v)
u=np.linspace(0, 2*np.pi, NTheta)
v=np.linspace(1*a0, 3*a0, NR)
u,v=np.meshgrid(u,v)
u=u.flatten()
v=v.flatten()

#evaluate the parameterization at the flattened u and v
x=v*np.cos(u)
y=v*np.sin(u)

#define 2D points, as input data for the Delaunay triangulation of U
points2D=np.vstack([u,v]).T
xy0 = np.vstack([x,y]).T

Tri1 = Delaunay(points2D) #triangulate the rectangle U

last_pt = xy0.shape[0]
xy1 = np.vstack((xy0,(0,0)))  # add ctr point
Tri3 = Delaunay(xy1)
print(Tri3.points.shape, Tri3.simplices.shape)

plt.triplot(Tri3.points[:,0], Tri3.points[:,1], Tri3.simplices, linewidth=0.5)
plt.show()

#plt.scatter(x, y)
plt.triplot(x, y, Tri1.simplices, linewidth=0.5)
plt.show()