class Polygon:
    def __init__(self,length):
        Polygon.length=length

class Rectangle(Polygon):
    def __init__(self,length,breadth):
        Polygon.__init__(self,length)
        self.breadth=breadth
        self.area=self.length*self.breadth
        self.perimeter=2*(self.length+self.breadth)
        
class Square(Polygon):
    def __init__(self,length):
        Polygon.__init__(self,length)
        self.area=self.length*self.length
        self.perimeter=4*self.length
        
class Triangle(Polygon):
     def __init__(self,length,l2,base,height):
        Polygon.__init__(self,length)
        self.l2=l2
        self.base=base
        self.height=height
        self.area=self.base*self.height*(1/2)
        self.perimeter=length+l2+base
    
class Rhombus(Polygon):
     def __init__(self,length,height):
        Polygon.__init__(self,length)
        self.height=height
        self.area=self.length*self.height
        self.perimeter=4*self.length
        

    
r1=Rectangle(15,10)
s1=Square(6)
rh1=Rhombus(7,8)
t1=Triangle(3,5,8,7)
print("Area of rectangle : ",r1.area)
print("perimeter of rectangle ",r1.perimeter)
print(" ")
print("Area of square : ",s1.area)
print("perimeter of square ",s1.perimeter)
print(" ")
print("Area of rhombus : ",rh1.area)
print("perimeter of rhombus ",rh1.perimeter)
print(" ")
print("Area of triangle : ",t1.area)
print("perimeter of triangle",t1.perimeter)

