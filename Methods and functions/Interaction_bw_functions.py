##guessing game using python
from random import shuffle

##function 1
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


##function 2
def player_guess():
    guess=''
    while guess not in [0,1,2]:
        guess=int(input("Pick a number : 0,1 or 2 "))
    return guess


##function 3
def check_guess(mylist,guess):
    if mylist[guess]=='o':
        print('Correct guess')
    else :
        print('Wrong guess!!')
        print(mylist)

##menu
##Intialize the list
mylist=['','o','']
##shuffle the list
shuffled_list = shuffle_list(mylist)
##user guesses
userguess=player_guess()
##check guess
check_guess(mylist,userguess)
