# instead of doing mylist=[0,1,..9] use range function
# Then cast it to list
mylist=list(range(0,10))
print(mylist)
index_count=0
for letter in 'abcde':
    print(f'At index {index_count} the letter is {letter}')
    index_count+=1
print('\n')

##ENUMERATE function
##for automating indexing
word='abcde'
for index,letter in enumerate(word) :
    print(index)
    print(letter)
    print('\n')
    
## Zip function is used for packing
##   using zip to combine the used the lists
mylist1=[0,1,2]
mylist2=['a','b','c','d','e'] #it will ignore d and e
mylist3=[100,200,300]

for a,b,c in zip(mylist1,mylist2,mylist3) :
    print(b, c)

##casting the zip to list
ziplist=list(zip(mylist1,mylist2,mylist3))
print(ziplist)
