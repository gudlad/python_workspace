line1=' yes I can do '
print(line1)
print(line1.strip())
print('\n')
line2='Have a nice day'
print(line2.startswith('Have'))

print('\n')
line3=' Yes I can DO '
print(line3)
print(line3.strip())
print(line3.lstrip())
print(line3.rstrip())

print('\n')

# split method
letter ='''Dear students
Good morning
Today is Python day'''
print(letter)
print(letter.split()) # default is split by space
print(letter.split('\n')) # split by new line
