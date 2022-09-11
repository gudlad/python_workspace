"""
Reading,Writing,Appending Modes :
    mode='r' is read only
    mode='w' is write only (wil overwrite files or create new)
    mode='a' is append only will add on to files
    mode='r+' is reading and writing
    mode='w+' is writing and reading(Overwrites existing files or creates a new file!)
"""
with open('/home/prasad/python_workspace/myfile.txt',mode='r') as f:
    print(f.read()) # only read no write

with open('/home/prasad/python_workspace/myfile.txt',mode='a') as f:
    f.write("this is a appended line") # append to the file
    
with open('/home/prasad/python_workspace/myfile.txt',mode='r') as f:
    print(f.read()) # only read no write
