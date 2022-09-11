mylist=[1,2,3,4,5,6,7,8,9,10]
for jelly in mylist:
    print(jelly)
print('\n')
##you can do may things with for loop
for jelly in mylist:
    print("hello")
print('\n')
for jelly in mylist:
##    check for even
    if jelly%2 :
       print(jelly)
    else :
        print(f'odd number :{jelly}')
print('\n')
listsum=0
for jelly in mylist:
    listsum=listsum+jelly
##    if we use don't give the identation output will be different
    print(listsum)
print('\n')
##when we dont want use a variable we can just use a symbol _
for _ in 'Hello World': 
    print("HI")
print('\n')
mylist=[(1,2),(3,4),(5,6),(7,8)]
for _ in mylist:
    print(_)
print('\n')
##Tuple unpacking
for (a,b) in mylist:  # parathesis in (a,b) not necesssary 
    print(a)
    print(b)
print('\n')
mylist=[(1,2,3),(3,4,5),(5,6,7),(7,8,9)]
for a,b,c in mylist :
    print(c)
print('\n')
d={'k1':1,'k2':2,'k3':3}
for key,value in d.items():
    print(key)
