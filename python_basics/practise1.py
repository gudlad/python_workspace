##PYTHON DATA-TYPES
##tuples
tuple1=('guru','guru',1,2,3)
##lists
list1=['guru','guru',1,2,3]
##Dictionaries
dictionary1={'name':'guru','name1':'guru','name':'prasad','usn':'4su19cs031'}
###Sets : ordered collection of unique objects/ no duplicate allowed
set={'a','b'}
##tuple can take duplicate values
for x in tuple1 :
    print(x)
print('\n')    
####list can take duplicate values
for x in list1:
    print(x)
print('\n')    
##print(dictionary1.keys)
print(dictionary1)
print('\n')
##another way of printing values of dictionary
print('for printing the items of dictinary : ')
dictionary_items=dictionary1.items()
for x in dictionary_items:
 print(x)
print('\n')
print('for printing the keys of dictinary : ')
for x in dictionary1.keys():
    print(x)
print('\n')
print('for printing the values of dictinary :') 
for x  in dictionary1.values():
    print(x)
print('\n')
print('priting the set items :')
print(set)
