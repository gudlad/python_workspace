""" (Doc string)
Syntax of function:

def name_of_function():  # def keyword tells python that this is a fuction
    print('Hello')
    
# this function follows snake-casing.
Snake-Casing is all lowercase(function name) with underscores between words

"""

def name_of_function(name='guru'):
    print("Hello "+name)
name_of_function()

def name_of_function(name):
    print("Hello "+name)
name_of_function('guru')

## most functions use return rarely use print()
##return allows us to assign the output of the functiion to a new variable
def name_of_function(name):
    return "Hello "+name
print(name_of_function('guru'))
