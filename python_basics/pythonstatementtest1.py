#1
st = 'Print only the words that start with s in this sentence'
for x in st.split() :
    if x[0]=='s':
        print(x)
print('\n')

#2
print(list(range(0,11,2)))
print('\n')

#3
mlist=[x for x in range(1,51,) if x%3==0]
print(mlist)
print('\n')

#4
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split() :
    if len(word)%2==0:
        print(f'{word} --> has even! length')
print('\n')

#5
for x in range(1,21):
    if x%3==0 and x%5==0:
        print(f'{x} --FizzBuzz')
    elif x%3==0:
        print(f'{x} -- Fizz')
    elif x%5==0:
        print(f'{x} --Buzz')

#6
str='Create a list of the first letters of every word in this string'
listoffirstletters=[x[0] for x in str.split()]
print(listoffirstletters)
