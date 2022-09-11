import math
##multiple assignment 
name=['Rahul','Modi','Amith','Kumar']
n1,n2,n3,n4=name
print(n1);
print(n2);
print(n3);
print(n4);

n=int(input("Enter a number : "))
l=list()
print(f"Enter {n} numbers")
i=0
while i<n :
   l.append(int(input()))
   i+=1
print(l)

sum=0
for i in l:
    sum=sum+i

print(sum)
avg=sum/len(l)
##print(math.floor(avg))
##print(math.ceil(avg))

prod=1
for i in l:
    prod=prod*i

print(f"sum = {sum}, average = {avg} , product = {prod}")
