
print('%s is smaller than %s' % ('one', 'two'))

"""
The Python interpreter substitutes the first occurrence of %s in the string by t
he given string "one", and the second %s by the string "two".
These %s strings are actually placeholders in our "template" string,
and they indicate that strings will be placed there.
"""
print("Mr. %s, the total is %.2f." % ("Jekyll", 15.53))
print("The character after %c is %c." % ("B", "C"))

place = "New"
print("Welcome to %s!" % place)

## %i and %d
year =2010
print("%d will be a perfect year." % year)

price = 155.345
print("the price is %f" % price)
print("the price is %.1f" % price) # one spaces after the decimal point
print("the price is %.2f" % price) # two spaces after the decimal point
print("the price is %.3f" % price)

##  Aligning the Output
## %10s reserves 10 characters
## %-10s puts any extra space to the right of the placholder

place = "London"
print ("%10s is not a place in France" % place)  # Pad to the left     
print ("%-10s is not a place in France" % place) # Pad to the right

print ("The postcode is %10d." % 25000)    # Padding on the left side
print ("The postcode is %-10d." % 25000)   # Padding on the right side






















.
