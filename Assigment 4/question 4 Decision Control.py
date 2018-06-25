points=int(input("Enter your points : "))

if points< 200:
    if points<=50 and points>=1:
        print("Sorry ! No prize this time.")
    if points<=150 and points>=51:
        print("Congratulations ! You won a Wooden Dog ")
    if points<=180 and points>=151:
        print("Congratulations ! You won a Book ")
    if points<=200 and points>=181:
        print("Congratulations ! You won a Chocolate ")
else:
    print("Sorry ! No prize this time.")
