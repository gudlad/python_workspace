# take three inputs
name="-welcome-"*3
print(name)
print("enter three values")
i1,i2,i3=input("Enter three values : ").split(",")
i1=int(i1)
i2=int(i2)
i3=int(i3)
print("The values of i1, i2 , i3 :{} {} {}".format(i1,i2,i3))
##another example
print("The values of i1,i2,i3 : {1} {2} {0}".format(i1,i2,i3))
