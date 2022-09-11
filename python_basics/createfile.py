##write will create a new file if the file doesn't exist or overwrite existing file
with open('/home/prasad/python_workspace/newfile.txt',mode='w') as f :
    f.write('I creted this file')

with open('/home/prasad/python_workspace/newfile.txt',mode='r') as f :
    print(f.read())
print('\n')
with open('/home/prasad/python_workspace/newfile.txt',mode='a') as f :
    f.write("\nThis is the second line")
with open('/home/prasad/python_workspace/newfile.txt',mode='r') as f :
    print(f.read())
