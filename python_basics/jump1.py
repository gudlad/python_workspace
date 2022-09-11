"""
break : Breaks out of current closet enclosing loop.
continue : Goes to the top of the closet enclosing loop.
pass : Does nothing at all.
"""
for letter in "Python":
    if letter=='h':
            break
    print("letter:",letter)

print('\n')
for letter in "Python":
    if letter == 'h':
        continue
    print("letter:",letter)
    
print('\n')
for letter in "Python":
    #no body
    pass #does nothing
## if the loop or method doesn't have a body mention pass keyword othrewise it will
##throw error

