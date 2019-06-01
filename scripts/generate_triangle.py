from math import *
import numpy as np
import matplotlib.pyplot as plt


class generate_triangle:
    def __init__(self,point_number):
        triangles = []
        self.triangles_generated = {}

        self.number_of_triangle = 0
        i,k,p = 0,0,0

        while i < point_number:
            k = 0
            while k < point_number:           
                p = 0
                while p < point_number:
                    
                    if(i != k and i != p and k != p):
                        triangles.append([i,k,p])

                        self.number_of_triangle = self.number_of_triangle + 1

                    p += 1    
                k += 1
            i += 1


        final_triangle = []
        self.save_triangle = 0

        for n in range(self.number_of_triangle):
            if(n < self.number_of_triangle - 1):
                if(triangles[n][0] == triangles[n+1][0]):
                    if((triangles[n][1] == triangles[n+1][1] or triangles[n][1] == triangles[n+1][2]) and (triangles[n][2] == triangles[n+1][2] or triangles[n][2] == triangles[n+1][1])):
                        final_triangle.append([triangles[n][0],triangles[n][1],triangles[n][2]])
                        self.save_triangle += 1
                                

        for n in range(self.save_triangle):
            self.triangles_generated[n] = final_triangle[n]
                    
