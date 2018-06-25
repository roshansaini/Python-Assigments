class circle:
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getCircumference(self):
        return 2*3.14*self.radius
circle1=circle(10)
print("Area : ",circle1.getArea())
print("Circumference : ",circle1.getCircumference())
