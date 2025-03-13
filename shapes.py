import math

class Circle:
    def __init__(self, x, y, radius):      
        self.radius = radius
        self.posx = x
        self.posy = y
    def getperimiterlen(self):
        return 2*math.pi*self.radius
    def getarea(self):
        return math.pi*(self.radius**2)
    def detectpoint(self,x,y):
        return ((x - self.posx)**2 + (y - self.posy)**2) <= (self.radius**2)

class Rectangle:
    def __init__(self, x, y, width, height):
        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
    def getpermiterlen(self):
        return 2*(self.width+self.height)
    def getarea(self):
        return self.width*self.height
    def detectpoint(self, x,y):
        bottomcorner = [self.posx-(self.width*1/2), self.posy-(self.height*1/2)]
        topcorner = [self.posx+(self.width*1/2), self.posy+(self.height*1/2)]
        return ((topcorner[0]>x>bottomcorner[0]) and (topcorner[1]>y>bottomcorner[1]))
class Triangle:
    def __init__(self, x, y, side_length):   
        self.x = x
        self.y = y
        self.side_length = side_length
    def getperimiterlen(self):
        return self.side_length*3
    def getarea(self):
        return (math.sqrt(3))/4**(self.side_length**2)
    def detectpoint(self, x, y):
        highenough = y>(self.y-((math.sqrt(3)*self.side_length)/4))
        leftgood = y<=(x+self.side_length+self.y)
        rightgood = y<=(x-self.side_length+self.y)
        return highenough and leftgood and rightgood
class Ellipsis:
    def __init__(self, xpos, ypos, xd, yd):
        self.xpos = xpos
        self.ypos = ypos
        self.xd = xd
        self.yd = yd
    def getpermiterlen(self):
        return 2*math.pi*math.sqrt(((self.xd**2)+(self.yd**2))/2)
    def getarea(self):
        math.pi*self.xd*self.yd
    def detectpoint(self,x,y):
        return ((((x-self.xpos)**2)/(self.xd**2))+(((y-self.ypos)**2)/(self.yd**2)) <= 1)
class Trapezoid:
    def __init__(self, a, b,h, x, y):
        self.a = a
        self.b = b
        self.h = h
        self.x = x
        self.y = y
    def getarea(self):
        return self.h*((self.a+self.b)/2)
    def getpermiterlen(self):
        sidelen = math.sqrt((abs(self.a-self.b)**2)+(self.h**2))*2
        return (2*sidelen)+self.a+self.b
    def detectpoint(self,x,y):
        if self.b>self.a:
            return y>((self.h)/2-self.y) and y<((self.h)/2+self.y) and y<(self.h/(self.b-(self.a/2)))*(x+(self.a/2))+(self.h/2)+ self.y and y<(-self.h/(self.b-(self.a/2)))*(x-(self.a/2))+(self.h/2)+self.y
        else:
            return y>((self.h)/2-self.y) and y<((self.h)/2+self.y) and y>(self.h/(self.b-(self.a/2)))*(x+(self.a/2))+(self.h/2)+ self.y and y>(-self.h/(self.b-(self.a/2)))*(x-(self.a/2))+(self.h/2)+self.y
class Hexagon

            

c = Circle(0,0,3)
print(c.getperimiterlen())
print(c.getarea())
print(c.detectpoint(0,0))
r = Rectangle(0,0, 5,17)
print(r.getpermiterlen())
print(r.getarea())
print(r.detectpoint(10,0))
t = Triangle(0,0,5)
print(t.getperimiterlen())
print(t.getarea())
print(t.detectpoint(0,0))
t = Ellipsis(0,0,5,5)
print(t.getpermiterlen())
print(t.getarea())
print(t.detectpoint(0,0))
t = Trapezoid(1,3,1,0,0)
print(t.getpermiterlen())
print(t.getarea())
print(t.detectpoint(0,0))


