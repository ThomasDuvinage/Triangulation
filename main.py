from scripts.cercle import *
from scripts.points import *
from scripts.generate_triangle import *
from scripts.voronoi import *
from math import sqrt

import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
plt.axis([-10,210,-10,210])

points_number = 13
final_triangles = []

select_point = generate_points(points_number,200,200,'random')

#this loop permit to print all parameters of all points
for row in range(select_point.number_point):
    print("Row = ",row)
    print("point x  = ",select_point.points[row][0])
    print("point y  = ",select_point.points[row][1],"\n")


#this following line permit us to generate all triangles for the figure 
triangle = generate_triangle(select_point.number_point)

final_triangles = []

#the following loop permit us to see all cercle for all points
for row in range(triangle.number_of_triangle):
    print("Triangle ", row," = ",triangle.triangles[row])
    
    circle_size = cercle_parameters(select_point.points[triangle.triangles[row][0]][0],select_point.points[triangle.triangles[row][0]][1],select_point.points[triangle.triangles[row][1]][0],select_point.points[triangle.triangles[row][1]][1],select_point.points[triangle.triangles[row][2]][0],select_point.points[triangle.triangles[row][2]][1])
    
    print("x  = ",circle_size.X0)
    print("y  = ",circle_size.Y0)
    print("R  = ",circle_size.Rc)


    circle = create_circle(circle_size.X0,circle_size.Y0,circle_size.Rc)
    #show_circle(circle)

    n = 0
    info = 0
    while n < select_point.number_point:
        distance = math.sqrt((select_point.points[n][0] - circle_size.X0)**2 + (select_point.points[n][1] - circle_size.Y0)**2)

        if(round(distance,3) < round(circle_size.Rc,3)):
            info += 1
            print("distance = ",distance)  
        
        n+=1  

    if(info == 0):
            final_triangles.append(triangle.triangles[row])
        
display_all_triangles(final_triangles,select_point)

voronoi(final_triangles,select_point)

plt.show()
