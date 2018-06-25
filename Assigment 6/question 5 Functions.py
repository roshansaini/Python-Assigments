def factorial(x,fact):
    if x==1:
        print("factorial : ",fact)
        return
    fact*=x
    x-=1
    factorial(x,fact)

num=int(input("Enter the number : "))
factorial(num,1)
