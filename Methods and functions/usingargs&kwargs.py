##using both arguments and keywork arguments
def myfunc(*args,**kwargs): # (arguments,key word arguments)
    print(args) #tuple
    print(kwargs) #dictionary
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='apple',food='eggs',animal='dog')


myset={1,2,2,2}
print(myset)

'''
here there the keyword argument food='eggs' is converted into 'food':'eggs' a dictionary item
