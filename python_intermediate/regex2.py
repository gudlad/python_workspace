import re
target_string='My number is 415-555-4242.'
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo=phoneNumRegex.search(target_string)
print('Phone number found: ',mo.group(0))
print('Phone number found: ',mo.group(1))
print('Phone number found: ',mo.group(2))
print('Phone number found: ',mo.group(3))
print('Phone number found: ',mo.groups())
print(phoneNumRegex.findall(target_string)) # if there is a group in the regex findall will return a list of tuples

IndianphoneNum=re.compile(r'\+91\s[1-9]{10}')
inmob=IndianphoneNum.search('My number is +91 9743681585.')
print('Phone number found: ',inmob.group())

IndianphoneNum=re.compile(r'\+91\s[1-9]{10}')
# if there is no group in the regex it will return a list of matched objects
match_objects=IndianphoneNum.findall('Cell:+91 9743681585 work:+91 97499981595')
print('matched objects: {}'.format(match_objects))
