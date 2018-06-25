num_list1=[]
num_list2=[]
merged_list=[]

def create_list(num_list=[]):
    size=int(input("Enter the list1 length :  "))
    for i in range(size):
        num_list.append(int(input("Enter Item : ")))

def merge_list(list1=[], list2=[]):
    merged_list=list1 + list2
    merged_list=sorted(merged_list)
    return merged_list

create_list(num_list1)
create_list(num_list2)

print("\n List 1 : ",num_list1)
print("\n List 2 : ",num_list2)
print("")
print("\n Merged List : ",merge_list(num_list1,num_list2))
