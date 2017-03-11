import rhinoscriptsyntax as rs
import random
import math
pi = 3.14159

cloud_pts = []
source_pts = []

def place_pts(x_range, y_range, z_range):
    x = random.uniform(-25, x_range)
    y = random.uniform(-.25, y_range)
    z = random.uniform(-.25, z_range)
    pt = [x,y,z]
    return pt

def randX(x_range):
    x = random.uniform(0,x_range)
    return x

def randY(y_range):
    y = random.uniform(0,y_range)
    return y

def randZ(z_range):
    z = random.uniform(0,z_range)
    return z

#setting range for random numbers defined above
xnum = randX(10)
ynum = randY(10)
znum = randZ(10)

#og_source_pts = rs.ObjectsByLayer("Source Points", True)
og_source_pts = rs.GetObjects("Select Source Points", rs.filter.point)
for pt in og_source_pts:
    ptCoord = rs.PointCoordinates(pt)
    source_pts.append(ptCoord)
    #find layer of each point, put in
    pt_layer_id = rs.ObjectLayer(pt)



#initializing cloud of points, vectorize between cloud and original points, move pt by sub_vect amount\
#draw line between pt and original points
for i in range(0,3000):
    pt = rs.AddPoint(place_pts(25,.25,.25))
    cloud_pts.append(pt)
    #find closest points from cloud to source points
    index = rs.PointArrayClosestPoint(source_pts, pt)
    clos_pt = source_pts[index]

    vect = rs.VectorCreate(clos_pt, pt)
    unit_vect = rs.VectorUnitize(vect)
    sub_vect = (vect/2)-(unit_vect)

    #draw line between origin (og_) pts and cloud of random pts
    init_dst  = rs.AddLine(pt, clos_pt)
    #move cloud of random pts according to outcome of sub_vect
    new_pt = rs.MoveObject(pt,sub_vect)
    sphere_that_line = rs.AddSphere(new_pt,())
    rs.SelectObject(new_pt)
    #print vect
    #print "BREAK"
    #print unit_vect
