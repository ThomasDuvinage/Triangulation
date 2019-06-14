from math import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

plt.figure(figsize=(7,7))
ax = plt.gca(projection='3d')

class cercle_parameters:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        
        self.indice_check = 0
        if((y3 - y2) != 0 and (y2-y1) != 0 and (2*(((x3 - x2) / (y3 - y2)) - ((x2 - x1)) != 0))):
            #permet de connaitre la position en x,y et le rayon du centre cercle qui passe par les 3 points
            calc1 = (pow(x3,2) - pow(x2,2)) / (y3 - y2)
            calc2 = (pow(x2,2) - pow(x1,2)) / (y2 - y1)
            calc3 = (x3 - x2) / (y3 - y2)
            calc4 = 2*(calc3 - ((x2 - x1) / (y2 - y1)))

            x = (calc1 - calc2 + y3 - y1) / calc4

            y = 0.5 * (((-2 * x * (x2 - x1)) / (y2 - y1)) + ((pow(x2,2) - pow(x1,2)) / (y2 - y1)) + y2 + y1)

            R = sqrt(pow((x1 - x),2) + pow((y1 - y),2))

            self.X0 = x
            self.Y0 = y
            self.Rc = R
            self.indice_check = 1


def create_circle(x,y,R):
    circle = plt.Circle((x,y),R,fill = False)
    return circle

def show_circle(patch):
    ax = plt.gca()
    ax.add_patch(patch)
