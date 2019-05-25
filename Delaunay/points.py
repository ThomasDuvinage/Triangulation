import math
import numpy as np 
from random import randint
import matplotlib.pyplot as plt

class generate_points:
    def __init__(self, nb_points,taille_x,taille_y):
        plt.axis([-10,110,-10,110])
        self.points = {}

        for n in range(0,nb_points):
            x = randint(0,taille_x)
            y = randint(0,taille_y)
            self.points[n] = [x,y]

            plt.plot(x,y,'ro')
            


