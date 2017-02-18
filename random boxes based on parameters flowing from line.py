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

def randX(x_range):
    x = random.uniform(-10,x_range)
    return x

def randY(y_range):
    y = random.uniform(-10,y_range)
    return y

def randZ(z_range):
    z = random.uniform(-10,z_range)
    return z

xnum = randX(10)
ynum = randY(10)
znum = randZ(10)

#initializing first point, making empty pts array, appending first point to pts array
pts = []
#ptZero = (0,0,0)
#pts.append(ptZero)

#initializing boxes
boxes = []
array = rs.AddBox([(0,0,0),(xnum,0,0),(xnum,ynum,0),\
(0,ynum,0),(0,0,znum),(xnum,0,znum),(xnum,ynum,znum),(0,ynum,znum)])
boxes.append(array)


#initializing line
start = rs.AddPoint(0,0,0)
end = rs.AddPoint(100,0,0)
line = rs.AddLine(start,end)

#Points = rs.DivideCurveLength(line,1,True,True)
#pts.append(Points)

for i in range(100):
    newPt = rs.AddPoint(i,0,0)
    xnum = randX(10)
    ynum = randY(10)
    znum = randZ(10)


    #find newPt coordinates to feed into the 8 needed box corners
    newPtCoord = rs.PointCoordinates(newPt)
    #newPtCoord = rs.PointCoordinates(pt)

    #add random xnum,ynum, or znum to respective index
    newboxArray = rs.AddBox([(newPtCoord),(newPtCoord[0]+xnum,newPtCoord[1],newPtCoord[2]),\
    (newPtCoord[0]+xnum,newPtCoord[1]+ynum,newPtCoord[2]),(newPtCoord[0],newPtCoord[1]+ynum,newPtCoord[2]),\
    (newPtCoord[0],newPtCoord[1],newPtCoord[2]+znum),(newPtCoord[0]+xnum,newPtCoord[1],\
    newPtCoord[2]+znum),(newPtCoord[0]+xnum,newPtCoord[1]+ynum,newPtCoord[2]+znum),\
    (newPtCoord[0],newPtCoord[1]+ynum,newPtCoord[2]+znum)])

    pts.append(newPt)

    boxes.append(newboxArray)
