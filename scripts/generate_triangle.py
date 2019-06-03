from math import *
import numpy as np
import matplotlib.pyplot as plt


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


                    
