user_list=[]
created_list=['google','apple','facebook','microsoft','tesla']

def add_item():
    x=input("Enter Item : ")
    user_list.append(x)
    menu()

def print_list():
    print("")
    print("Your List : ",user_list)
    print("")
    new_list=[]
    new_list=user_list+created_list
    print("New List : ",new_list)

def menu():
    choice=input(" Add item (y/n) : ")
    if choice=='y' or choice=='Y':
        add_item()
    else:
        print_list()

print("Creating you List : ")
menu()
