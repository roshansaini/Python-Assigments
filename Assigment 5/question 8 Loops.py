mylist=[1,2,3,4,5,6,7,8,9,10]

x=int(input("Enter the value : "))

for y in mylist:
    if y==x:
        mylist.remove(y)

print("List : ",mylist)
