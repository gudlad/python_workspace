# the end parameter is used to append any string at the end of the output of the print statement in python

print("Hello world my name is guruprasad.",end='')   # by default in print() the end is '\n' we don't need to specify
print(" I study cse at sdmit ujire")                 # when we explicitly specify the value for end '\n' will be ignore 
print('\n')

## using end we can print the output in single line


## sometimes we may wish to print multiple values in python progrm in a readable mannner
## this is when the sep argument comes to play
## by default the value of sep param is whitespace ' '

print("Hello world "," my name is guruprasad " ," i study cse at "," sdmit ujire ",sep='$')
print('\n')
print('1','3','5',sep="<")
print('Study '," Tonight",sep='&')
