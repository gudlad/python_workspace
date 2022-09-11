# write a python program to accept USN and marks obtained,find maximum,minimum
# and students USN who scored high in the range 100-85,85-75,75-60 and below 60
# marks seperately

print('Type "done" when done')
dic={}
while True:
    usn=input("usn:")
    if usn=='done':
        break;
    mar=int(input('marks:'))

    if usn in dic:
        print("Duplicate of usn")
    else:
        dic[usn]=mar
high=0 # set two pointers high and low
highusn=None
# when you want to declare a varaible and dont want to store anything assing it to null
low=100
lowusn=None

for i in dic:
    if high<dic[i]:
        high=dic[i]
        highusn=i
    if low>dic[i]:
        low=dic[i]
        lowusn=i

for i in dic:
    if dic[i]>=85 and dic[i]<=100:
        print("Range 100-85: usn:{} Marks:{}".format(i,dic[i]))
    elif dic[i]>=75 and dic[i]<=85:
        print("Range 85-75: usn:{} Marks:{}".format(i,dic[i]))
    elif dic[i]>=60 and dic[i]<=75:
        print("Range 75-60: usn:{} Marks:{}".format(i,dic[i]))   
    elif dic[i]<60:
        print("Range below 60: usn:{} Marks:{}".format(i,dic[i]))
print('\n')      
print('usn:{} with lowest marks:{}'.format(lowusn,dic[lowusn]))
print('usn:{} with highest marks:{}'.format(highusn,dic[highusn]))
