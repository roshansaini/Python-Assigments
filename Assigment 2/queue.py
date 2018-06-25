queue=[1,2,3]

def dequeue():
    queue.pop()
    print("Item poped : ",queue)
    menu()

def peek():
    print("Item peek : ",queue[0])
    menu()

def enqueue(x):
    queue.insert(0,x)
    menu()

def menu():
    print("Queue : ",queue)
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.peek")
    choice=int(input("Enter you choice : "))
    if choice==1:
        x=int(input("Enter Item : "))
        enqueue(x)
    elif choice==2:
        dequeue()
    elif choice==3:
        peek()
    else:
        print("Invalid Choice..!!")

menu()
