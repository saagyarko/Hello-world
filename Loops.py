#Loops
#"for" loop
primes=[1,2,3,4,5,6]
for prime in primes: #prints the numbers individually
    print(prime)

#for range()
for x in range(5):
    print(x)

for x1 in range(1,4):
    print( x1)    

for y in range(2, 9, 2):
    print(y)

#"while" loop
count=0
while count<5:
    print(count)
    count+=1 

count1=0
while False:
    print(count1)
#"break" operator
count=0
while True:
    print(count)
    count+=1
    if count>=6:
        break
        print("Count is greater than 6.")
#"continue" operator
for x in range(10):
    if x % 2==1: #checking for even numebrs
        continue
    print(x)

#"else involved in "for" and "while" loops 
for y in range(1,7):
    if y % 2 == 0:
        break
        print("These are odd numbers")
else:
    print("These are even numbers.")    

count=0
while(count<6):
    print(count)
    count+=1
else:
    print("Count value has reached %d" %count)        
