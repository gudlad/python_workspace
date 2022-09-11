# dictionaries dont keep the items in order manner
##that's why we can't do sorting in dictionary
my_dict={'key1':'value1','key2':'value2'}
print(my_dict['key1'])
prices_lookup={'apple':2.99,'orange':[4.5,55,4,3],'mango':{'inside_key':199}}
print(prices_lookup['orange'])
print(prices_lookup['orange'][2])
print(prices_lookup['mango'])
print(prices_lookup['mango']['inside_key'])
print('\n')
d={'key1':['a','b','c']}

print(d)
print(d['key1'][2])
##to change the item in the list we can write like
d['key1'][2].upper()
print(d)
print('\n')
##adding the keys and values to dictionary
d={'k1':100,'k2':200,'k3':300}
d['k4']=400
print(d)
##we can overwrite the existing value as
d['k1']="changed"
print(d)
##to see the values use d.keys() and to see the values use d.values()
##to see both key value pair use d.items()
""" to remove the items from the dictionary use pop() method """
d.pop('k1')
print(d)
print('\n')

##delete operation in dictionary
dict={'k1':1,'k2':2,'k3':3,'k1':4} # for key k1 the value is 4 recently assigned value
##to remove the entry with key k2
del dict['k2']
print(dict)
# to clear all the keys and values of  dictionary use clear()
dict.clear()
print(dict)
# to delete the whole dictionary
del dict
print(dict)


##get() method in dictionary
# get() returns the fallback value if the mentioned key is not present in dict
picnicItems={'apple':5,'eggs':2}
str1='I am bringing '+str(picnicItems.get('apple',0))+' apple.'
print(str1)
str1='I am bringing '+str(picnicItems.get('banans',0))+' eggs.'
print(str1)
print('\n')

##  setdefault() method in dictionary
#   this will check whether the key exits in the dictionary,
##  if it exits then it will do nothing
##  else it will add that key to the dictionary
spam={'name':'Pooka','age':5}
print(spam) 
spam.setdefault('color','white')
print(spam)
spam.setdefault('color','black') # it will not chage the value of color
print(spam)
print('\n')

##    pretty printing in dictionary
##   it can be used to the nested dictionries


import pprint
message='It was a bright cold day in April, and the clocks were striking thirteen'
count=dict() #or count={} , create empty dictionary
print(count)
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)
