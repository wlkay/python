import rhinoscriptsyntax as rs
import random


def placePt(x_range,y_range,z_range):
    x = random.uniform(0,x_range)
    y = random.uniform(0,y_range)
    z = random.uniform(0,z_range)
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

xnum = randX(10)
ynum = randY(10)
znum = randZ(10)

ptZero = [0,0,0]
pts = []
pts.append(ptZero)

boxes = []
array = rs.AddBox([(0,0,0),(xnum,0,0),(xnum,ynum,0),\
(0,ynum,0),(0,0,znum),(xnum,0,znum),(xnum,ynum,znum),(0,ynum,znum)])
boxes.append(array)

firstBox = rs.GetBox()
if firstBox: rs.AddBox(firstBox)

for i in range(0,300):
    xnum = randX(10)
    ynum = randY(10)
    znum = randZ(10)
    pt = rs.AddPoint(placePt(100,100,50))

    index = rs.PointArrayClosestPoint(pts,pt)
    cp = pts[index]
    vect = rs.VectorCreate(cp, pt)
    unitVect = rs.VectorUnitize(vect)
    subVect = vect - unitVect
    newPt = rs.MoveObject(pt,subVect)

    #find newPt coordinates to feed into the 8 needed box corners
    newPtCoord = rs.PointCoordinates(newPt)
    #newPtCoord = rs.PointCoordinates(pt)
    #take newPt coordinates index 0,1, or 2 for x,y, or z respectively,
    #add random xnum,ynum, or znum to respective index
    newboxArray = rs.AddBox([(newPtCoord),(newPtCoord[0]+xnum,newPtCoord[1],newPtCoord[2]),\
    (newPtCoord[0]+xnum,newPtCoord[1]+ynum,newPtCoord[2]),(newPtCoord[0],newPtCoord[1]+ynum,newPtCoord[2]),\
    (newPtCoord[0],newPtCoord[1],newPtCoord[2]+znum),(newPtCoord[0]+xnum,newPtCoord[1],\
    newPtCoord[2]+znum),(newPtCoord[0]+xnum,newPtCoord[1]+ynum,newPtCoord[2]+znum),\
    (newPtCoord[0],newPtCoord[1]+ynum,newPtCoord[2]+znum)])
    pts.append(newPt)

    boxes.append(newboxArray)

selectVol = rs.GetObject("Select main volume")
boolInter = rs.BooleanIntersection(selectVol,boxes)
