# The ord() and chr() functions help in converting
# character to ascii value and vicaversa

# char to ascii value
char=input()
print(ord(char))
print('\n')

smalllist=list()
biglist=list()

# ascii value to char
for i in range(97,123):
    smalllist.append(chr(i))
print(smalllist)

print('\n')
    
for j in range(65,91):
    biglist.append((chr(j)))
print(biglist)
