##when you use for loop and append method to convert a string into a list u can use
##list comprehension to do it efficiently
string = 'hello'
stringlist=[]
##mylist=list(string)
##print(mylist)
for letter in string :
    stringlist.append(letter)
print(stringlist)

##we can do this more efficiently using the list comprehension
##ALTERNATIVE WAY
String2='good bye'
stringlist=[x for x in String2]
print(stringlist)
print('\n')
mylist=[num for num in range(0,11)]
print(mylist)
print('\n')
##condition in list comprehension
mylist=[num for num in range(0,11) if num%2==0]
print(mylist)
print('\n')
##squre of even numbers
mylist=[num**2 for num in range(0,11) if num%2==0]
print(mylist)
print('\n')
celsius=[0,10,20,30.5]
fahrenheit=[(9/5)*temp+32 for temp in celsius]
print(fahrenheit)
print('\n')
##the same code can be written as
"""
fahrenheit=[]
for temp in celsius :
    fahrenheit.append(((9/5)*temp+32))
print(fahrenheit)
"""

##we can also use if else inside the list comprehension
listx=[x if x%2==0 else 'ODD' for x in range(0,11)]
print(listx)
##
list2=[1,2,3]
list3=[x for x in list2]
print(list3)
print('\n')
##
##for loop can also be used inside a list comprehension
mylist=[]
"""
for x in [10,20,30]:
    for y in [10,20,30]:
        mylist.append(x*y)
print(mylist)
"""
mylist=[x*y for x in [10,20,30] for y in [10,20,30]]
print(mylist)
