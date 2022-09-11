## Tuples in python
##Tuples are immutable
##we can't change the elements in the index
t=(1,2,3)
t=(1,2.4,'guru')
print(t)
print(t[1])
print(t[-1])
##tuples are indexed in the same way as string and lists
##count and index methods in tuple
t=('a','a','b')
print(t.count('a'))
print(t.index('a')) # return the first occurance of a

"""
[3]='b'
print(t)

""" 
##TypeError: 'tuple' object does not support item assignment
t=(1,2,[3,4])
print(t)
t=([1,2,3],{'k1':4})
print(t)
print(t[1])
