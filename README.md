# Triangulation

This project permit to generate faces with points.

To do that I use the Delaunay triangulation algorithm.

## How I implement this problem ? 

### Generate all points 

Firstly to generate all points, I decided to give them random positions for x and y for a given number of points.
But you can also create two tables, x and y positions, with this solution you will be able to make faces out of a given amoud of points.

### Generate all triangles 
To make the Delaunay algorithm works you have to create an array which include all triangles you can draw with all points you gave or determined.
    
So the array will look like that :

```python
array[] = [[A,B,C][A,D,C],...] //depend of the number of point you gave
```

The following formula allows us to determine the number of triangles you will be able to create :

```python
((nb_point - 1)(nb_point - 2)(nb_points)) / 2
```

This is very useful because you have to create an array with all triangles, or you will have repetition in the generation of triangles (for example ABC = CBA it is the same traingle). 

So to avoid those repetitions I note that we can make an algorithm to solve that.

To show it, I took 4 points A,B,C,D, the table below represent all triangles you can draw for one point and if you have to delete because of a repetition

    |Triangles    | Delete     | n    |  
    | ---         |  ---       | ---  |
    | ABC         | X          |      |
    | ABD         | X          | 2    |
    |             |            |      |
    | ACB         |            |      |
    | ACD         | X          | 1    |
    |             |            |      |
    | ADB         |            |      |
    | ADC         |            | 0    |

So here you can see that the 2 (--> n) first points are deleted and after you substract 1 to n and after you delete all the n points from the end of the (nb_points - 2) group.



## Sources :

These links help me a lot to understand how it works.

 - [Delaunay Triangulation](https://members.loria.fr/MPouget/files/enseignement/delaunay-maitrise-od.pdf)
 - [Delaunay Triangulation, University of Luxembourg by Guendalina Palmirotta](http://math.uni.lu/eml/projects/reports/MathExp_Palmirotta.pdf) (This link is very useful to understand algorithms)


