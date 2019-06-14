from scripts.points import *
from scripts.cercle import *
import matplotlib.pyplot as plt

def voronoi(final_triangles,select_point):
    cercle_position_x = []
    cercle_position_y = []

    for i in range(len(final_triangles)):
        circle_size = cercle_parameters(select_point.points[final_triangles[i][0]][0],select_point.points[final_triangles[i][0]][1],select_point.points[final_triangles[i][1]][0],select_point.points[final_triangles[i][1]][1],select_point.points[final_triangles[i][2]][0],select_point.points[final_triangles[i][2]][1])
        circle = create_circle(circle_size.X0,circle_size.Y0,circle_size.Rc)
        show_circle(circle)

        cercle_position_x.append(circle_size.X0)
        cercle_position_y.append(circle_size.Y0)
    
    plt.plot(cercle_position_x,cercle_position_y,color = 'blue',linewidth = 2)