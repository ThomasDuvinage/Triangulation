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
                        triangles.append([i,k,p])

                        self.number_of_triangle = self.number_of_triangle + 1

                    p += 1    
                k += 1
            i += 1


        final_triangle = []
        final_triangle.append(triangles[0])
        self.save_triangle = 1

        # for i in range(self.number_of_triangle):
        #     print(triangles[i])

        #for n in range(self.number_of_triangle):
        #    for n in range(self.save_triangle):
                #if(final_triangle[n][0] == final_triangle[self.save_triangle][0] or )
                                
        for n in range(self.number_of_triangle):
            self.triangles_generated[n] = triangles[n]
                    
