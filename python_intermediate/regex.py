import re
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ',mo.group())

try:                                          #  \s    matches \t \n \r
    IndianphoneNum=re.compile(r'\+91\s[1-9]{10}')
    inmob=IndianphoneNum.search('My number is +91 9743681585.')
    print('Phone number found: ',inmob.group())
except:
    print('error!!')
