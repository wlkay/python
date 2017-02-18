import rhinoscriptsyntax as rs
import random

#definition for placing random points in x,y, and z ranges
def placePt(x_range,y_range,z_range):
    x = random.uniform(0,x_range)
    y = random.uniform(0,y_range)
    z = random.uniform(0,z_range)
    pt = [x,y,z]
    return pt

#making random numbers to call later
def randNum(x_range):
    x = random.uniform(0,x_range)
    return x

def randX(x_range):
    x = random.uniform(0,x_range)
    return x

def randY(y_range):
    y = random.uniform(0,y_range)
    return y

def randZ(z_range):
    z = random.uniform(0,z_range)
    return z

#initializing first point, making empty pts array, appending first point to pts array
ptZero = [0,0,0]
pts = []
pts.append(ptZero)

#setting range for random numbers defined above
xnum = randX(10)
ynum = randY(10)
znum = randZ(10)

#initializing first box, based on random numbers created with xnum, etc
#initializing box zero array
boxes = []
array = rs.AddBox([(0,0,0),(xnum,0,0),(xnum,ynum,0),\
(0,ynum,0),(0,0,znum),(xnum,0,znum),(xnum,ynum,znum),(0,ynum,znum)])
boxes.append(array)

#make random point, move that point closer to closest point in pts array
for i in range(1,10):
    xnum = randX(10)
    ynum = randY(10)
    znum = randZ(10)
    pt = rs.AddPoint(placePt(100,100,100))
    index = rs.PointArrayClosestPoint(pts,pt)
    cp = pts[index]
    vect = rs.VectorCreate(cp, pt)
    unitVect = rs.VectorUnitize(vect)
    subVect = vect - unitVect
    newPt = rs.MoveObject(pt,subVect)
    #find newPt coordinates to feed into the 8 needed box corners
    newPtCoord = rs.PointCoordinates(newPt)
    #take newPt coordinates index 0,1, or 2 for x,y, or z respectively,
    #add random xnum,ynum, or znum to respective index
    newboxArray = rs.AddBox([(newPtCoord),(newPtCoord[0]+xnum,newPtCoord[1],newPtCoord[2]),\
    (newPtCoord[0]+xnum,newPtCoord[1]+ynum,newPtCoord[2]),(newPtCoord[0],newPtCoord[1]+ynum,newPtCoord[2]),\
    (newPtCoord[0],newPtCoord[1],newPtCoord[2]+znum),(newPtCoord[0]+xnum,newPtCoord[1],\
    newPtCoord[2]+znum),(newPtCoord[0]+xnum,newPtCoord[1]+ynum,newPtCoord[2]+znum),\
    (newPtCoord[0],newPtCoord[1]+ynum,newPtCoord[2]+znum)])
    pts.append(newPt)

    boxes.append(newboxArray)

    #for each new box created, boolean difference the previous box

    #newObject = rs.BooleanIntersection(boxes[i-1],boxes[i],delete_input=False)

    if i == 1:
        intersectTrue = rs.IntersectBreps(boxes[i-1],boxes[i])
        if intersectTrue:
            newObject = rs.BooleanDifference(boxes[i-1],boxes[i],delete_input=False)
        else:
            print"No Intersection"
    else:
        intersectTrue = rs.IntersectBreps(newObject,boxes[i])
        if intersectTrue:
            newObject = rs.BooleanDifference(newObject,boxes[i],delete_input=False)
        else:
            print"nothing"
            #newObject = boxes[i]
            #rs.DeleteObject(boxes[i])
