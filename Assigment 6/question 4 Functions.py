x=int(input("Enter the Base : "))
y=int(input("Enter the Power : "))

def cal_power(p,num=1):
    if p==0:
        print("Power : ",num)
        return
    num*=x
    p-=1
    cal_power(p,num)


cal_power(y)
