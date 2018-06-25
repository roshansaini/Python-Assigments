my_dict={}

def create_dict():
    x=input("Enter Key : ")
    y=input("Enter Value : ")
    my_dict[x]=y

length=int(input("Enter the Length : "))
for i in range(length):
    create_dict()

print("My Dict : ",my_dict)
print("Keys : ",my_dict.keys())
