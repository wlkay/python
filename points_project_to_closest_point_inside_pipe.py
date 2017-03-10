import rhinoscriptsyntax as rs
import random

all_points = []
pipe_points = []

def place_pts(x_range,y_range,z_range):
    x = random.uniform(-100, x_range)
    y = random.uniform(-100,y_range)
    z = random.uniform(-100,z_range)
    pt = [x,y,z]
    return pt

#initializing first points to build line to build pipe
point1 = rs.AddPoint(-100,0,0)
point2 = rs.AddPoint(100,0,0)

#initialize cloud of initial end points of line (from last script, not used here)
cloud = (point1, point2)


line = rs.AddLine(point1, point2)
pipe = rs.AddPipe(line, 0, 4)

#get coordinates of first point to feed to integerize loop, get length, turn into integer
point_coord = rs.PointCoordinates(point1)
length = rs.CurveLength(line)
integerize = int(length)

#put points on the line
for i in range(integerize):
    points_on_line = rs.AddPoint(point_coord[0]+i,0,0)
    pipe_points.append(points_on_line)

#initializing cloud of line points
line_cloud = pipe_points

#move random cloud of points to closest points on line cloud
for i in range(0,100):
    pt = rs.AddPoint(place_pts(100,100,100))
    index = rs.PointArrayClosestPoint(line_cloud, pt)
    cp = line_cloud[index]
    vect = rs.VectorCreate(cp, pt)

    project = rs.ProjectPointToSurface(pt, pipe, vect)
    rs.AddPoints(project)

    all_points.append(pt)


#making a function to delete objects, but I guess it'd be easier to just do the built in rs.DeleteObject
"""def delete_object(a,b,c,d,e):
    rs.DeleteObjects(object)
    return object
delete_object(pipe_points, all_points, pipe, point1, point2)
#delete_object(all_points)
#delete_object(pipe)
#delete_object(point1)
#delete_object(point2)


rs.DeleteObjects(pipe_points)
rs.DeleteObjects(all_points)
rs.DeleteObjects(pipe)
rs.DeleteObject(point1)
rs.DeleteObject(point2)
"""
