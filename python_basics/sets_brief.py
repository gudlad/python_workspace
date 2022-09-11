##sets are unordered collections of unique elements
##There can be only one representative of the same object

##create a set 
set={1,2,3,4,5}
print(set
      
myset=set()
print(myset)
myset.add(1)
myset.add(2)
myset.add(2) # stores only unique values stores only single 2
print(myset)
##casting to set
my_list=[1,1,1,2,2,2,3,3,3,4] # only unique values are stored
new_set=set(my_list)
print(new_set)
string='Mississippi'
alpha_set=set(string)
print(alpha_set)
