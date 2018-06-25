# Sets

my_set1={}
my_set2={}
my_set1=set(my_set1)
my_set2=set(my_set2)

def add_item(myset=()):
    x=input("Enter Item : ")
    myset.add(x)

def create_set(myset=()):
    size=int(input("Enter the Length : "))
    for i in range(size):
        add_item(myset)

def menu():
    print("Set A : ",my_set1)
    print("Set B : ",my_set2)
    print("1.Add Item")
    print("2.Difference")
    print("3.Intersecction")
    print("4.Compare")
    choice=int(input("Enter choice : "))
    if choice==1:
        create_set(my_set1)
        create_set(my_set2)
        menu()
    if choice==2:
        print("Difference : ",my_set1-my_set2)
        menu()
    if choice==3:
        print("Intersection : ",my_set1 & my_set2)
        menu()


menu()
