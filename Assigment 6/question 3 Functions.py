num=12
val=1
def multiple(val):
    if val==11:
        return
    print(num*val)
    val+=1
    multiple(val)

multiple(val)
