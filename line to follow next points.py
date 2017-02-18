import rhinoscriptsyntax as rs
import random
rs.EnableRedraw(True)

#definition for placing random points in x,y, and z ranges
def placePt(x_range,y_range,z_range):
    x = random.uniform(0,x_range)
    y = random.uniform(0,y_range)
    z = random.uniform(0,z_range)
    pt = [x,y,z]
    return pt

#initializing first point, making empty pts array, appending first point to pts array
pts = []
ptZero = (0,0,0)
pts.append(ptZero)

#initializing lines array so i can fillet the fucker
lines = []

for i in range(10):
    pt = rs.AddPoint(placePt(100,100,100))
    pts.append(pt)
    if i >= 0:
        line = rs.AddLine(pts[i-1],pts[i])
        lines.append(line)
    #if i >= 2:
    #    fillet = rs.AddFilletCurve(lines[i-1],lines[i])
