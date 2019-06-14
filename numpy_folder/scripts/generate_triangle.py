from math import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

plt.figure(figsize=(7,7))
ax = plt.gca(projection='3d')


class generate_triangle:
    def __init__(self,point_number):
        self.triangles = []

        self.number_of_triangle = 0
        i,k,p = 0,0,0

        while i < point_number:
            k = 0
            while k < point_number:           
                p = 0
                if(i == k and k+1 < point_number):
                    k += 1
                while p < point_number:
                    if(p == i and p+1 < point_number):
                        p += 1
                        if(p == k and p+1 < point_number):
                            p += 1
                    
                    if(p == k and p+1 < point_number ):
                        p += 1
                    
                    if(i != k and i != p and k != p):
                        self.triangles.append([i,k,p])

                        self.number_of_triangle = self.number_of_triangle + 1

                    p += 1    
                k += 1
            i += 1

        n,o = 0,0

        while n < self.number_of_triangle:
            o = 0
            while o < self.number_of_triangle:
                if(o == n and o+1 < self.number_of_triangle):
                    o += 1
                if(self.triangles[n][0] == self.triangles[o][0] or self.triangles[n][0] == self.triangles[o][1] or self.triangles[n][0] == self.triangles[o][2]):
                    if(self.triangles[n][1] == self.triangles[o][0] or self.triangles[n][1] == self.triangles[o][1] or self.triangles[n][1] == self.triangles[o][2]):
                        if(self.triangles[n][2] == self.triangles[o][0] or self.triangles[n][2] == self.triangles[o][1] or self.triangles[n][2] == self.triangles[o][2]):
                            self.triangles.pop(o)
                            self.number_of_triangle -= 1
                o += 1
            n += 1


def display_all_triangles(final_triangles,select_point):
    x = []
    y = []
    for i in range(len(final_triangles)):
        x.append([select_point.points[final_triangles[i][0]][0],select_point.points[final_triangles[i][1]][0],select_point.points[final_triangles[i][2]][0],select_point.points[final_triangles[i][0]][0]])
        y.append([select_point.points[final_triangles[i][0]][1],select_point.points[final_triangles[i][1]][1],select_point.points[final_triangles[i][2]][1],select_point.points[final_triangles[i][0]][1]])

        surf = ax.plot_surface(x[i], y[i], 0, cmap=cm.coolwarm,linewidth=0, antialiased=False)
        #plt.plot(x[i], y[i],color='green', linewidth=3)


                    
