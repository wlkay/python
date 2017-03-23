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

#og_source_pts = rs.ObjectsByLayer("Source Points", True)
og_source_pts = rs.GetObjects("Select Source Points", rs.filter.point)
for pt in og_source_pts:
    ptCoord = rs.PointCoordinates(pt)
    source_pts.append(ptCoord)


def obj_layer(layer_name):
    '''trying to be able to call obj_layer on clos_pt with a particular
    layer name to give the corresponding cloud points a different parameter
    to move by
    '''
    layer = rs.ObjectsByLayer(layer_name)
    return layer

#initializing cloud of points, vectorize between cloud and original points, move pt by sub_vect amount\
#draw line between pt and original points
for i in range(0,5000):
    pt = rs.AddPoint(place_pts(25,.25,.25))

    #find closest points from cloud to source points
    index = rs.PointArrayClosestPoint(source_pts, pt)
    clos_pt = source_pts[index]

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


    """
    name = rs.ObjectName(source_pts)
    if name == "Denver":
        print "gotchya1"
    for pt in source_pts:
        rs.ObjectName()
        name = rs.ObjectName(pt)
        if name == "Denver":
            print "gotchya2"
        #if rs.ObjectName(pt) == rs.ObjectsByName(layer_name):
            #print "gotchya"
    """


    sub_vect = (vect)-(unit_vect)

    #draw line between origin (og_) pts and cloud of random pts
    init_dst  = rs.AddLine(pt, clos_pt)
    line_set1.append(init_dst)
    #move cloud of random pts according to outcome of sub_vect
    new_pt = rs.MoveObject(pt,sub_vect)
    new_pt_coord = rs.PointCoordinates(new_pt)
    cloud_pts.append(new_pt)
    #adding spheres to the new lines
    #sphere_that_line = rs.AddSphere(new_pt,rs.VectorLength(sub_vect)/6)
    #adding boxes to the new lines
    div_num = 10
    vector_length = rs.VectorLength(sub_vect)/div_num
    box_that_line = rs.AddBox(\
    [(new_pt_coord),\
    (new_pt_coord[0]+vector_length,new_pt_coord[1],new_pt_coord[2]),\
    (new_pt_coord[0]+vector_length,new_pt_coord[1]+vector_length,new_pt_coord[2]),\
    (new_pt_coord[0],new_pt_coord[1]+vector_length,new_pt_coord[2]),\
    (new_pt_coord[0],new_pt_coord[1],new_pt_coord[2]+vector_length),\
    (new_pt_coord[0]+vector_length,new_pt_coord[1],new_pt_coord[2]+vector_length),\
    (new_pt_coord[0]+vector_length,new_pt_coord[1]+vector_length,new_pt_coord[2]+vector_length),\
    (new_pt_coord[0],new_pt_coord[1]+vector_length,new_pt_coord[2]+vector_length)])


"""
def PassPtName(pt_name):
    pt_name = rs.ObjectsByName(pt_name)
    if pt_name == "Denver":
        pass

index = rs.ObjectsByName("Denver")
print index
rs.MoveObject(index, (0,0,10))


for pt in og_source_pts:
    if rs.ObjectsByLayer("Denver"):
        sphere_that_line = rs.AddSphere(new_pt,rs.VectorLength(sub_vect))
        rs.SelectObject(sphere_that_line)
    else:
        pass

    #print vect
    #print "BREAK"
    #print unit_vect
"""
