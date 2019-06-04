import math
import numpy as np 
from random import randint
import matplotlib.pyplot as plt

class generate_points:
    def __init__(self, nb_points,taille_x,taille_y,choice):
        self.points = []

        if(choice == 'random'):
            self.number_point = nb_points
            for n in range(0,nb_points):
                x = randint(0,taille_x)
                y = randint(0,taille_y)
                self.points.append([x,y])

                plt.plot(x,y,'ro')
        
        elif(choice == 'table'):
            self.points = [[2,2],[2,50],[50,49.99],[50,2]]
            self.number_point = len(self.points)
            for n in range(len(self.points)):
                plt.plot(self.points[n][0],self.points[n][1],'ro')
            

            


