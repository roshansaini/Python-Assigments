num_list=[]

size=int(input("Enter the length :  "))

for i in range(size):
    num_list.append(int(input("Enter Item : ")))

print("\n Your List : ",num_list)
print("\n Sorted List : ",sorted(num_list))
