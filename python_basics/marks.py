##elif ladder
"""
if(c1):
 statement1
elif(c2):
 statement2
elif (c3):
 statement3
elif (c4):
 statement4
else:
 statement3
"""
marks=int(input('Enter the marks out of 100 :'))
if (marks>=90 and marks<=100) : # use boolean operator and,or,not
    print('A grade')
elif (marks>=80  and marks<=89) :
    print('B grade')
elif (marks>=70 and marks<=79) :
    print('C grade')
elif (marks>=60 and marks<=69) :
    print('D grade')
elif (marks>=35 and marks<=59) :
    print('E grade')
elif (marks>=0 and marks<=34) :
    print('F grade')
else:
    print('Invalid')
