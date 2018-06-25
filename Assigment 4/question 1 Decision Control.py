year=int(input("Enter the Year : "))

if year%4==0:
    if year%100==0:
        if year%400:
            print("A Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("A Leap Year")
else:
    print("Not a Leap Year")
