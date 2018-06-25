mylist=[]
square_list=[]
for i in range(4):
    x=int(input("Enter the data : "))
    mylist.append(x)

for i in mylist:
    square_list.append(i*i)

print("List : ",mylist)
print("Squared : ",square_list)
