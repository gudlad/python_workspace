##    variable no of arguments in python

##    *arg -- allows us to take arbitary no of arguments the user can pass as many
##     arguments he likes the argumets will be converted to tuple
def myfunc(*args) :
    print(args)
    return sum(args)

print(myfunc(10,20,30,40,50,60)) # these args will converted to tuple
##you can give as many arguments you want

#     USE **kwargs for keyword arguments
#     **kwargs -- allows us to handle variable no key word arguments
#     arguments will converted into a dictionary


'''
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My favourite fruit is {}'.format(kwargs['fruit']))
    else:
        print("I did n't find any fruit")
myfunc(fruit='apple',veggie='lettuce')
'''

def myfunc(**jelly):
    print(jelly)
    if 'fruit' in jelly:
        print('My favourite fruit is {}'.format(jelly['fruit']))
    else:
        print("I did n't find any fruit")
        
myfunc(fruit='apple',veggie='lettuce')
