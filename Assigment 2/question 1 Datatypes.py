user_list=[]

def add_item():
    x=input("Enter Item : ")
    user_list.append(x)
    menu()

def print_list():
    print("")
    print("Your List : ",user_list)

def menu():
    choice=input(" Add item (y/n) : ")
    if choice=='y' or choice=='Y':
        add_item()
    else:
        print_list()
print("Creating you List : ")
menu()
