#Exercise 1

x=int(input('Enter a numbers: '))
y=int(input('Enter a numbers: '))
var1 =x*y
if var1 < 1000:
	print('Multipl. result: ' ,var1)
elif var1>1000:
	print( 'Addition result: ', x+y)

# exercise 2

n=int(input('Enter any number : '))

n1 = 0
n2 = 1
count=0
while count<n:
	
	n3= n1 + n2
	
	n1=n2
	
	n2=n3
	count += 1
print(n1)
