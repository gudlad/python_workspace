##String indexing and slicing 
##These actions use [] squar brackets and a number index to
##indicate positions of what you wish to grab 
string='guruprasad'
##   [start: stop : step ]
##we can use both positive and negative to get the characters
print(string[0])
print(string[-1])
substring=string[:4:]
print("{}".format(substring))
print(len(substring))
print(string[::])
##step size of 2
print(string[::2])
##reverse the sting 
print(string[::-1])
print('samsung'[::2])
##String is immutable in python
##string concatenation
x='hellow world'
x=x+" it is a beautiful "+x[7:12:]+"!!!"
print(x)
##String bulitin methods
y='guru prasad'
print(y.upper())
##string split method
print("hello my name is guruprasad".split())
##split by character 'i'
print("higimsnimimmirrr".split('i'))
