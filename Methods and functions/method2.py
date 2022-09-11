def say_hello(name='Default') :
    #if the argument is not provided then the default value is used
        print(f'Hello {name}')
##here value is not provided so defualt value is used
say_hello()
##here value is provided so default value is not used
say_hello('guru')
print('\n')


##Drawback of dynamically typed property of python
def sum_numbers(num1,num2) :
    return num1+num2
print(sum_numbers(10,20)) # performs addition
print(sum_numbers('10','20')) # performs concatenation for string arguments
##this is drawback of dynamic type
