myfile=open('myfile.txt')
"""
myfile_content=myfile.read()        #read is not very useful 
print(myfile_content)
"""
##to store every line of file as element of list we have to use the readline() method
myfile_list=myfile.readlines()
print(myfile_list)
for x in myfile_list :
    print(x)
myfile.close()
