import rhinoscriptsyntax as rs
import random

def place_pts(x_range,y_range,z_range):
    x = random.uniform(-100, x_range)
    y = random.uniform(-100,y_range)
    z = random.uniform(-100,z_range)
    pt = [x,y,z]
    return pt

point1 = rs.AddPoint(-100,0,0)
point2 = rs.AddPoint(100,0,0)

#cloud = rs.PointAdd(point1, point2)
#cloud = rs.AddPoints(point1)
cloud = (point1, point2)

line = rs.AddLine(point1, point2)
pipe = rs.AddPipe(line, 0, 4)

all_points = []
for i in range(0,100):
    pt = rs.AddPoint(place_pts(100,100,100))
    index = rs.PointArrayClosestPoint(cloud, pt)
    cp = cloud[index]
    vect = rs.VectorCreate(cp, pt)
    #move = rs.MoveObject(pt,vect)
    #vector = rs.VectorCreate(index, pt)
    #index_points = rs.PointArrayClosestPoint(pipe_points, pt)
    #vector = rs.VectorCreate(index_points, pt)
    #rs.VectorCreate()
    #unit_vector = rs.VectorUnitize(vector)
    #new_pt = rs.MoveObject(pt, unit_vector)

    project = rs.ProjectPointToSurface(pt, pipe, vect)
    rs.AddPoints(project)

    all_points.append(pt)

#pipe_points = []
#for i in range(300):
#contour = rs.CurveContourPoints(pipe, point1, point2, 1)

#SurfaceDomain requires two arguments, second argument = u or v direction, 0 or 1 respectively
#dom_u = rs.SurfaceDomain(pipe,0)
#dom_v = rs.SurfaceDomain(pipe,1)
#eval_srf = rs.EvaluateSurface()(pipe,uv)

#cloud = rs.GetPoints()
#cloud.append(point1)
#cloud = rs.PointCloudPoints(cloud)

"""
points = [point1, point2]
add_to_cloud = rs.AddPointCloud(points)
end_points = rs.PointCloudPoints(add_to_cloud)
"""

"""
 import rhinoscriptsyntax as rs
              cloud= rs.GetObject("Select point cloud")
              if cloud:
              point = rs.GetPoint("Point to test")
              if point:
              cloud = rs.PointCloudPoints(cloud)
              index = rs.PointArrayClosestPoint(cloud, point)
              if index is not None:
              point_id = rs.AddPoint(cloud[index])
              rs.SelectObject( point_id )
"""
