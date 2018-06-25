class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def getDetails(self):
        print("Name : ",self.name)
        print("Rollno : ",self.rollno)

stud1=student("Roshan",8)
stud1.getDetails()

