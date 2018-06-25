print("*------Bill Counter--------*")

quantity=int(input("Enter the quantity : "))
price=quantity*100

if price>=1000:
    print("Total Price : ",price)
    print("\t 10% Discount Available.")
    new_price= price*0.10
    print("You have to pay  :",price-new_price)
else:
    print("Sorry ! No discount Available.")
    print("You have to Pay : ",price)
