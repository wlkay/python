import rhinoscriptsyntax as rs
import random


cloud_pts = []
source_pts = []

def place_pts(x_range, y_range, z_range):
    x = random.uniform(-25, x_range)
    y = random.uniform(-.2, y_range)
    z = random.uniform(-.2, z_range)
    pt = [x,y,z]
    return pt

#put source point coordinates in source_pts list


#og_source_pts = rs.ObjectsByLayer("Source Points", True)
og_source_pts = rs.getobjects("Select Source Points", rs.filter.point)
for pt in og_source_pts:
    ptCoord = rs.PointCoordinates(pt)
    source_pts.append(ptCoord)
    #find layer of each point, put in
    pt_layer_id = rs.ObjectLayer(pt)

#initializing cloud of points
for i in range(0,3000):
    pt = rs.AddPoint(place_pts(25,.2 ,.2))
    cloud_pts.append(pt)
    #find closest points from cloud to source points
    index = rs.PointArrayClosestPoint(source_pts, pt)
    clos_pt = source_pts[index]
    vect = rs.VectorCreate(clos_pt, pt)
    unit_vect = rs.VectorUnitize(vect)
    sub_vect = vect - unit_vect

    new_pt = rs.MoveObject(pt,sub_vect)
    #vect_line = rs.AddLine(pt,new_pt)
    rs.SelectObject(new_pt)
    #print vect
    #print "BREAK"
    #print unit_vect

"""
    index = rs.PointArrayClosestPoint(pts,pt)
    cp = pts[index]
    vect = rs.VectorCreate(cp, pt)
    unitVect = rs.VectorUnitize(vect)
    subVect = vect - unitVect
    newPt = rs.MoveObject(pt,subVect)
"""
