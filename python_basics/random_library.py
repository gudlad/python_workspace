##random library
from random import shuffle
newlist=[1,2,3,4,5]
shuffle(newlist)
print(newlist)
print('\n')
from random import randint
for _ in range(0,10) :
    print(randint(0,1000))
