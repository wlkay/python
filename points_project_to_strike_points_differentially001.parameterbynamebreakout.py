import rhinoscriptsyntax as rs
import random
import math
pi = 3.14159

cloud_pts = []
source_pts = []
line_set1 = []

def place_pts(x_range, y_range, z_range):
    x = random.uniform(-25, x_range)
    y = random.uniform(-.25, y_range)
    z = random.uniform(-.25, z_range)
    pt = [x,y,z]
    return pt

"""
#setting up random ranges for boxes to come later
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
"""

#below automatically selects points for script based on layer
#og_source_pts = rs.ObjectsByLayer("Source Points", True)
#below manual selection of points for script
og_source_pts = rs.GetObjects("Select Source Points", rs.filter.point)
for pt in og_source_pts:
    ptCoord = rs.PointCoordinates(pt)
    source_pts.append(ptCoord)

#initializing cloud of points, vectorize between cloud and original points, move pt by sub_vect amount\
#draw line between pt and original points
for i in range(0,500):
    pt = rs.AddPoint(place_pts(25,.25,.25))

    #find closest points from cloud to source points
    index = rs.PointArrayClosestPoint(source_pts, pt)

    clos_pt = source_pts[index]

    #rs.LayerId("Denver")

    denver = rs.ObjectLayer("f753777e-e8b5-4641-a968-8a6da86d3d74")
    print denver

    """
    #find layer of each point, put in
    for pt in og_source_pts:
        pt_name = rs.ObjectLayer(pt)
        change_layer = rs.ObjectLayer(clos_pt, pt_name)
    """
        #rs.ObjectsByLayer()
        #clos_pt_layer = rs.ObjectLayer(og_source_pts)
        #print clos_pt_layer
        #change_layer = rs.ObjectLayer(pt, clos_pt_layer)


    #vector initializing
    vect = rs.VectorCreate(clos_pt, pt)
    unit_vect = rs.VectorUnitize(vect)


    #this makes the objects fall along a sphere
    #sub_vect = (vect)-(unit_vect)
    #this makes the objects fall along a straight line
    sub_vect = (vect)/3

    #draw line between origin (og_) pts and cloud of random pts
    init_dst  = rs.AddLine(pt, clos_pt)
    line_set1.append(init_dst)
    #pipes the lines
    #rs.AddPipe(init_dst, 0, .01, 0)
    #move cloud of random pts according to outcome of sub_vect
    new_pt = rs.MoveObject(pt,sub_vect)
    new_pt_coord = rs.PointCoordinates(new_pt)
    cloud_pts.append(new_pt)


    #set parameter for spheres and boxes
    #run through clos_pt, if it's layer is x, then move cloud pts that are close to it into x layer,
    #then get those close pts by layer, and apply parameter to the boxes that grow off them.

    #string_l = rs.ObjectLayer(index)
    #print string_l
    div_num = 5
    vector_length = rs.VectorLength(sub_vect)/div_num

    #adding spheres to the new lines
    rs.AddSphere(new_pt,vector_length)

    #adding boxes to the new lines

    '''rs.AddBox(\
    [(new_pt_coord),\
    (new_pt_coord[0]+vector_length,new_pt_coord[1],new_pt_coord[2]),\
    (new_pt_coord[0]+vector_length,new_pt_coord[1]+vector_length,new_pt_coord[2]),\
    (new_pt_coord[0],new_pt_coord[1]+vector_length,new_pt_coord[2]),\
    (new_pt_coord[0],new_pt_coord[1],new_pt_coord[2]+vector_length),\
    (new_pt_coord[0]+vector_length,new_pt_coord[1],new_pt_coord[2]+vector_length),\
    (new_pt_coord[0]+vector_length,new_pt_coord[1]+vector_length,new_pt_coord[2]+vector_length),\
    (new_pt_coord[0],new_pt_coord[1]+vector_length,new_pt_coord[2]+vector_length)])
    '''

"""
def PassPtName(pt_name):
    pt_name = rs.ObjectsByName(pt_name)
    if pt_name == "Denver":
        pass

index = rs.ObjectsByName("Denver")
print index
rs.MoveObject(index, (0,0,10))



"""
