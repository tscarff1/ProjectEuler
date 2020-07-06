import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Get the slope in the form y/x from this point to other
    #Parameter other should be a Point
    def getYSlope(self, other):
        if self.x == other.x:
            return None
        return (other.y - self.y) / (other.x - self.x)

    #Get the slope in the form x/y from this point to other
    #Parameter other should be a Point
    def getXSlope(self, other):
        if self.y == other.y:
            return None
        return (other.x - self.x) / (other.y - self.y)

#The segment class consists of 2 points. The segment class stores the slope and inverse-slope between the two points
#The segment also stores if the segment passes through either the x or y axis
class Segment:
    def __init__(self, p1, p2):
        #This if-else makes sure that self.p1 is left of or aligned with self.p2
        if p1.x < p2.x:
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1

        self.slope = self.p1.getYSlope(self.p2)
        self.slopeInv = self.p1.getXSlope(self.p2)

        if self.p1.x == 0:
            self.yInt = self.p1.y
        elif self.p2.x == 0:
            self.yInt = self.p2.y
        elif (sign(self.p1.x) == sign(self.p2.x)) or self.p1.x == self.p2.x:
            self.yInt = None
        else:
            self.yInt = getYIntercept(self.p1, self.slope)

        if self.p1.y == 0:
            self.xInt = self.p1.x
        elif self.p2.y ==0:
            self.xInt = self.p2.x
        elif (sign(self.p1.y) == sign(self.p2.y)) or self.p1.y == self.p2.y:
            self.xInt = None
        else:
            self.xInt = getXIntercept(self.p1, self.slopeInv)

    #return an array containing the axes which the segment intercepts
    #0: positive y
    #1: positive x
    #2: negative y
    #3: negative x
    def getInterceptAxes(self):
        axes = []
        if self.yInt == 0 and self.xInt == 0:
            axes.append(0)
            axes.append(1)
            axes.append(2)
            axes.append(3)
        if self.yInt is not None:
            axes.append(1 - sign(self.yInt))
        if self.xInt is not None:
            axes.append(2 - sign(self.xInt))
        return axes

#returns if a number is negative (-1), positive (1) or 0 (0)
def sign(num):
    if num < 0:
        return -1
    if num > 0:
        return 1
    else:
        return 0

#Calculate the y intercept of a line which has slope ySlope and contains Point samplePoint
def getYIntercept(samplePoint, ySlope):
    return -1 * samplePoint.x * ySlope + samplePoint.y

#Calculate the y intercept of a line which has inverted slope xSlope and contains Point samplePoint
def getXIntercept(samplePoint, xSlope):
    return -1 * samplePoint.y * xSlope + samplePoint.x

#The Triangle class takes 3 Points as arguments for initialization
# It then creates 3 Segments using these points to determine if the triangle containsOrigin (the point (0,0))
# A triangle contains the origin if and only if the segments pass through each of the 4 axes (+y,-y,+x,-x)
class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

        self.ab = Segment(self.a,self.b)
        self.ac = Segment(a,c)
        self.bc = Segment(b,c)

        intercepts = [0] * 4
        for axis in self.ab.getInterceptAxes():
            intercepts[axis] += 1
        for axis in self.ac.getInterceptAxes():
            intercepts[axis] += 1
        for axis in self.bc.getInterceptAxes():
            intercepts[axis] += 1

        if (intercepts[0] > 0 and intercepts[1] > 0 and intercepts[2] > 0 and intercepts[3] > 0):
            self.containsOrigin = True
        else:
            self.containsOrigin = False

#String is expected to be of form 'a,b,c,d,e,f'
#This string denotes 3 points: (a,b), (c,d), (e,f)
def triangleFromStr(str):
    split = str.split(",")
    a = Point(int(split[0]), int(split[1]))
    b = Point(int(split[2]), int(split[3]))
    c = Point(int(split[4]), int(split[5]))
    t= Triangle(a,b,c)
    return t

start = int(round(time.time() * 1000))
#read in each set of points
with open("p102_triangles.txt", "r") as file:
    lines = file.readlines()

#remove whitespace and line endings from each entry
lines = [x.strip() for x in lines]

#Get the number of triangles which contain the origin
originCount = 0
for line in lines:
    if triangleFromStr(line).containsOrigin:
        originCount+=1
end = int(round(time.time() * 1000))
print(originCount)
print(end - start)