##inbulit string methods
str='guruprasad'
print(dir(str))
# the dir() method lists all the methods available for the string object str
## string builtin methods
'''
'capitalize',
'count',
'endswith',
'find',
'format',
'index',
'isalnum',
'isalpha',
'isdecimal',
'isdigit',
'isidentifier',
'islower',
'isnumeric',
'isprintable',
'isspace',
'istitle',
'isupper',
'join',
'lower',
'lstrip',
'replace',
'rsplit',
'rstrip',
'split',
'startswith',
'strip',
'upper‘.
'''
print('\n')
##ex:1
var="Welcome to Python programming"
print(var.count('g'))
print(var.upper())
print(var.lower())
print(var.title())
print(var.swapcase())
print(var.capitalize())
print('\n')

## find() method in python
## The find() method is similar to index() method but
print(var.index('p')) # if not found raises an exception
print(var.find('p'))  # if not found returns -1
print(var.find('Python'))

##syntax of find method
'''
string.find(value,start,end)

value - value to search for
start - Optional. Where to start the search,Default is 0
end - Optional.Where to end the search. Default is to the end of string

'''
print('\n')
print(var.find('o',6))
txt='Hello, welcome to my world.'
print(txt.find('e',5,10))
 
