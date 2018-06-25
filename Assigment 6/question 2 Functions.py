num=int(input("Enter the number : "))

def perfect_num(num):
    factor=[]
    for i in range(1,num):
        if num%i==0:
            factor.append(i)
    mysum=sum(factor)
    if mysum==num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

perfect_num(num)
