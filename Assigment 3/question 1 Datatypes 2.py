# Tuples

my_tuple=(1,2,'a','b',"Roshan","Rahul",12.0,14.0)

print("My Tuple : ",my_tuple)
print("length : ",len(my_tuple))

my_tuple2=(1,2,3,4,5,6,7,8,9,10)
print("\nMy Tuple : ",my_tuple2)
print("Max : ",max(my_tuple2))
print("Min : ",min(my_tuple2))

product=1

for i in my_tuple2:
    product=product*i

print("Product : ",product)
