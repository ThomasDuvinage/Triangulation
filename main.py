from scripts.cercle import *
from scripts.points import *
from scripts.generate_triangle import *
from math import sqrt

import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))

points_number = 10
final_triangles = []

select_point = generate_points(points_number,100,100)

#this loop permit to print all parameters of all points
for row in range(0,points_number):
    print("Row = ",row)
    print("point x  = ",select_point.points[row][0])
    print("point y  = ",select_point.points[row][1],"\n")


#this following line permit us to generate all triangles for the figure 
triangle = generate_triangle(points_number)

final_triangles = []

#the following loop permit us to see all cercle for all points
for row in range(triangle.number_of_triangle):
    print("Triangle ", row," = ",triangle.triangles[row])
    
    circle_size = cercle_parameters(select_point.points[triangle.triangles[row][0]][0],select_point.points[triangle.triangles[row][0]][1],select_point.points[triangle.triangles[row][1]][0],select_point.points[triangle.triangles[row][1]][1],select_point.points[triangle.triangles[row][2]][0],select_point.points[triangle.triangles[row][2]][1])

    print("x  = ",circle_size.X0)
    print("y  = ",circle_size.Y0)
    print("R  = ",circle_size.Rc)

    circle = create_circle(circle_size.X0,circle_size.Y0,circle_size.Rc)
    show_circle(circle)

    n = 0
    info = 0
    while n < points_number:
        distance = math.sqrt((select_point.points[n][0] - circle_size.X0)**2 + (select_point.points[n][1] - circle_size.Y0)**2)

        if(round(distance,3) < round(circle_size.Rc,3)):
            info += 1
            print("distance = ",distance)  
        
        n+=1  

    if(info == 0):
            final_triangles.append(triangle.triangles[row])
        
x = []
y = []
for i in range(len(final_triangles)):
    x.append([select_point.points[final_triangles[i][0]][0],select_point.points[final_triangles[i][1]][0],select_point.points[final_triangles[i][2]][0],select_point.points[final_triangles[i][0]][0]])
    y.append([select_point.points[final_triangles[i][0]][1],select_point.points[final_triangles[i][1]][1],select_point.points[final_triangles[i][2]][1],select_point.points[final_triangles[i][0]][1]])

    plt.plot(x[i], y[i],color='green', linewidth=3)

plt.show()

print("final_triangles = ",final_triangles)



