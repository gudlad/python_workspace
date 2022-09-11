import re
regexvowel=re.compile('[aeiouAEIOU]')
vowelregex=regexvowel.findall('Robocop eats baby food.Baby Food.')
print(vowelregex)

regexvowel=re.compile('[^aeiouAEIOU]')
vowelregex=regexvowel.findall('Robocop eats baby food.Baby Food.')
print(vowelregex)


regexvowel=re.compile('[0-5.]')
vowelregex=regexvowel.findall('Robocop wighs 45.42kg.')
print(vowelregex)
