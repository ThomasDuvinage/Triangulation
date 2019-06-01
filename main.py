from scripts.cercle import *
from scripts.points import *
from scripts.generate_triangle import *

import matplotlib.pyplot as plt

points_number = 3

circle_size = cercle_parameters(1,3,3,2,1,1)

print("x  = ",circle_size.X0)
print("y  = ",circle_size.Y0)
print("R  = ",circle_size.Rc)

circle = create_circle(circle_size.X0,circle_size.Y0,circle_size.Rc)
show_circle(circle)

select_point = generate_points(points_number,100,100)

#this loop permit to print all parameters of all points
for row in range(0,points_number):
    print("Row = ",row)
    print("point x  = ",select_point.points[row][0])
    print("point y  = ",select_point.points[row][1],"\n")


#this following line permit us to generate all triangles for the figure 
triangle = generate_triangle(points_number)

for row in range(0,triangle.save_triangle):
    print("Triangle ", row," = ",triangle.triangles_generated[row])

#plt.show()