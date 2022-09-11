##pattern 1
for x in range(1,5):
    for y in range(1,6):
        print(x*y,end=" ")
    print('\n')
    
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

##pattern 2
temp=1
for x in range(1,6):
    for y in range (1,x+1):
        print(temp ,end='')
        temp+=1
    print("\n")
