user_list=[]
created_list=['google','apple','facebook','microsoft','tesla']
new_list=[]

def add_item():
    x=input("Enter Item : ")
    user_list.append(x)
    menu()

def menu():
    choice=input(" Add item (y/n) : ")
    if choice=='y' or choice=='Y':
        add_item()
    else:
        print_list()

def item_count(new_list=[]):
    print("\nFrequency :\n")
    for x in set(new_list):
        print(x," occures ",new_list.count(x)," times..!!")

def print_list():
    print("")
    print("Your List : ",user_list)
    print("")

    new_list=user_list+created_list
    print("New List : ",new_list)
    item_count(new_list)

print("Creating you List : ")
menu()

