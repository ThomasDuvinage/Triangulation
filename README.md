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

So first we generate all triangles for example if I choose 4 points it will be :
For the point A :

| Triangles |
| --- |
| ABC |
| ABD |
| ACB |
| ACD |
| ADB |
| ADC |

We do that for all points.

After that we can see that some triangles are the same like ABD = ADB so we delete one of them, so at the end of the loop we don't have any repetitions.

By analysis table of triangles we can see that the number of triangles for one point which are really useful is :

```python
((nb_point-1) * (nb_point - 2)) / 2
```

Go to -->scripts/generate_triangle.py to see the code.

## Sources :

These links help me a lot to understand how it works.

 - [Delaunay Triangulation](https://members.loria.fr/MPouget/files/enseignement/delaunay-maitrise-od.pdf)
 - [Delaunay Triangulation, University of Luxembourg by Guendalina Palmirotta](http://math.uni.lu/eml/projects/reports/MathExp_Palmirotta.pdf) (This link is very useful to understand algorithms)

 - [Other methods](http://www.achrafothman.net/docs/mesh3d.2tnsi.chapitre%204.pdf)

