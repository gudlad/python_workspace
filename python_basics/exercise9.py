def myfunc(*args):
    place_holder=[]
    for x in args:
        if x%2==0:
            place_holder.append(x)
        else:
            pass
    return place_holder
print(myfunc(5,6,7,8))

