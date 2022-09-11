my_list=['String',200,34.44]
##length of list
print(len(my_list))
print(len('guru'))
print('\n')
my_list=['one','two','three','four','five']

##slicing and indexing in list
##slicing in lists works just like  in strings
print(my_list[0])
mini_list=my_list[2::]
print(mini_list)
print('\n')

##concatenation of lists
my_list2=['six','seven']
new_list=my_list+my_list2;
print(new_list)
print('\n')

##lists are mutable unlike strings
new_list[0]='ONE ALL CAPS'
print(new_list)
print('\n')

##using the builtin list methods
##adding item to the end of the list
new_list.append('eight')
##list.append() takes exactly one argument

##removing the item of the list
##remove the item from the end of the list
popped_item=new_list.pop()
print(f'the popped item is {popped_item}')
print('\n')



##sort method in list it doesn't return anything
num_list=[3,6,2,1,5]
num_list.sort()
print('sort')
print(num_list)
print('\n')

##reverse method reverses the entire list
num_list.reverse()
print('reverse')
print(num_list)
print('\n')
list3=[1,2,[3,4,'hello']]
list3[2][2]='good bye'
print(list3)
print('\n')

# list extend method
list1=[1,2,3,4]
list1.append(5)
print(list1)
list1.extend([6,7])
print(list1)
print('\n')

#list insert method
list1.insert(0,55)
print(list1)
print('\n')

# deleting item in list
# if you don't know the position of an element than use the remove method
list1.remove(55)
print(list1)
print('\n')

# if you don't want the deleted to be returned then use
# del operator
del list1[2]
print(list1)


