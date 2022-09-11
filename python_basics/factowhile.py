##18/10/2021

##while loop
##Syntax :
## intitalization

"""
 while condition :
     statement 1
     statement 2
     updation
"""
n=int(input('Enter the number :'))
m=1
fact=1
while(m<=n) :
    fact=fact*m
    m+=1
print('factorial of {0} is {1}'.format(n,fact))
