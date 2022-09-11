import math
num=int(input('Enter the number :'))
isprime=True

for i in range(2,int(math.sqrt(num))+1) :
    if num%i ==0:
        isprime=False
        break
print(f'{num} is prime') if isprime==True else print(f"{num} not prime")


