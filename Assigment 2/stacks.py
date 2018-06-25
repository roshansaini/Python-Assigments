stack=[1,2,3]

def pop():
    stack.pop()
    print("Item poped : ",stack)
    menu()

def peek():
    print("Item peek : ",stack[-1])

def push(x):
    stack.append(x)
    menu()

def menu():
    print("Stack : ",stack)
    print("1.Push")
    print("2.pop")
    print("3.peek")
    choice=int(input("Enter you choice : "))
    if choice==1:
        x=int(input("Enter Item : "))
        push(x)
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    else:
        print("Invalid Choice..!!")

menu()
