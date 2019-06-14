import math
import numpy as np 
from random import randint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

plt.figure(figsize=(7,7))
ax = plt.gca(projection='3d')

class generate_points:
    def __init__(self, nb_points,taille_x,taille_y,choice):
        self.points = []

        if(choice == 'random'):
            self.number_point = nb_points
            for n in range(0,nb_points):
                x = randint(0,taille_x)
                y = randint(0,taille_y)
                self.points.append([x,y])

                ax.scatter(x,y,0,c="r", marker="o")
        
        elif(choice == 'table'):
            self.points = [[2,2],[2,50],[50,49.99],[50,2]]
            self.number_point = len(self.points)
            for n in range(len(self.points)):
                ax.scatter(self.points[n][0],self.points[n][1],0,c="r", marker="o")
            

            


