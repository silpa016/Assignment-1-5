Assignment1 prog1
num1 = 2.5
num2 = 2.5
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

Assignment1 prog2
l=[]
for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))signment 1 prog 2

Assignment 1 prog 3
first_name=input("enter first name")
last_name= input("enter last name")

print(last_name +" "+ first_name)
print(last_name[::-1]+" "+first_name[::-1])

Assignment 1 prog 4
import math
pi = math.pi
r = 15
v=(4/3)*(pi)*r**3
print(v)
