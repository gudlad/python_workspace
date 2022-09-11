##formatted string outputs
print('This is a string {}'.format("inserted"))
print("The {} {} {}".format('fox','brown','quick'))
print("The {2} {1} {0}".format('fox','brown','quick'))
print("The {0} {0} {0}".format('fox','brown','quick'))
##assigning the keywords
print("The {q} {b} {f}".format(f='fox',b='brown',q='quick'))
print("The {f} {f} {f}".format(f='fox',b='brown',q='quick'))
##float formatting using the format method()
##   {value : width . precision f}
result=0.12345678990
##precision is 3
print("The result is {r:1.3f}".format(r=result))
##precision is 5 with 10 width i.e whitespace 
print("The result is {r:10.5f}".format(r=result))
