even=[]
odd=[]

for i in range(1,101):
    if i%2==0:
        even.append(i)
    if i%2!=0:
        odd.append(i)

print("Even : ",even)
print("Odd : ",odd)
