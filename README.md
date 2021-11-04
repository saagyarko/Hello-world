# Hello-world

first repository
Kay here, I like python and java.s 
first_name = "samuel"
last_name = "agyarko"
full_name = first_name +" "+ last_name
message = "Hi, " + full_name.title() + "would you like to learn bow to sing ?"
print(message) 



# Casing of words

name = "sam kay"
print(name.title())
print(name.lower())
print(name.upper())
print("\n")
print('Jesus said, "knock and it shall be open unto you"\n')
famous_name = "Jesus"
print(famous_name +" "+"said," +'"knock and it shall be open unto you"')




# Clearing the whitespace 

name_1=" Ako "
name_2=" Kofi"
name_3="Kay "
print(name_1.strip())
print(name_2.lstrip())
print(name_3.rstrip())




# The use of str

age = 20
birthday = "Happy" +" "+ str(age) + "th Birthday !!"
print(birthday)
print('\n')




# Dealing with numbers

print(5+3)
print(16-8)
print(16/2)
print(4*2)
print('\n')
fav_num = 5
fav  = "My favourite number is" +" "+ str(fav_num)
print(f)


# List

books = ['rich dad', 'poor dad', 'henry danger', 'thundermans']
print(books)




# Accessing list

print(books[0].title())
print(books[1].lower())
print(books[2].upper())
print(books[3].title())
word= "My favourite comedy show is" +" "+ books[2].title() + '.'
print(word)
print('\n')



# message for names

names=['lukman', 'godey', 'delius', 'allfix']
print(names[0].title()+" "+ "is a mad boy")
print(names[1].title()+" "+ "is a mad boy")
print(names[2].title()+" "+ "is a mad boy")
print(names[3].title()+" "+ "is a mad boy")
print('\n')



# Replacing elements in a list

motorcycles = ['Honda', 'Suzuki', 'BMW']
motorcycles[1]='Ducati'
motorcycles[0] ='Yamaha'



# Adding elements to list

motorcycles.append('honda'.title())
print(motorcycles)



# Creating an empty list and filling

motorbikes=[]
motorbikes.append('ducati'.title())
motorbikes.append('yamaha'.title())
motorbikes.append('honda'.title())
motorbikes.append('suzuki'.title())
motorbikes.append('bugati'.title())
print(motorbikes)



# Removing element

del motorbikes[2]
print(motorbikes)




# Removing element using pop() and re-using the element


popped_motorbikes_1 = motorbikes.pop()
popped_motorbikes_2 = motorbikes.pop(0)
popped_motorbikes_3 = motorbikes.pop(1)
print(motorbikes)

print("My last motorcycle I bought was" +" "+ popped_motorbikes_1 + ".")
print("My first motorcycle I bought was" +" "+ popped_motorbikes_2 + ".")
print("My second motorcycle I bought was" +" "+ popped_motorbikes_3 + ".")



# Try works

print('\n')
guests = ['Ellie', 'Mimi', 'Joy']

print('Agyarko is inviting you,' +" "+ guests[0]+" "+'to a dinner')
print('Agyarko is inviting you,' +" "+ guests[1]+" "+'to a dinner')
print('Agyarko is inviting you,' +" "+ guests[2]+" "+'to a dinner\n')


print("Unfortunately" +" "+ guests[0] +" "+ "can't make it")
guests.remove('Ellie')
guests.append('Lydia')
guests.append('Max')
guests.append('Phoebe')
guests.append('Lynk')
print(guests)



print("Hey, I found a bigger table and would like to invite you," +" "+ guests[3] +" "+ "to a late night dinner.")
print("Hey, I found a bigger table and would like to invite you," +" "+ guests[4] +" "+ "to a late night dinner.")
print("Hey, I found a bigger table and would like to invite you," +" "+ guests[-1] +" "+ "to a late night dinner.")



# Organising list

cars = ['bmw', 'suzuki', 'toyota', 'audi', 'bugatti']
cars.sort()
print(len(cars))
print(cars)
cars.sort(reverse=True)
print(cars)

print(sorted(cars))
carss = ['benz', 'ferrari', 'mercedes', 'bmw']
carss.reverse()
print(carss)



# Try Work

cities = ['tokyo', 'qatar', 'dubai', 'hawaii', 'suadi arabia']
print(cities)
print(sorted(cities))
print(cities)
print(sorted(cities))
print(cities)
cities.reverse()
print(cities)
cities.reverse()
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
print('\n')

words = ['daphline', 'godfred', 'godrich',
'felix', 'alima']
print(words)
print('\n')



# working with lists

for word in words:
	print('The name'+" " +word.title()+"," + " "+ "is a word not a name!!!")
print('\n')
magicians=['sam', 'omar', 'frank', 'henry']
for magician in magicians:
	print(magician)
	print(magician.title()+ ", that was an awesome trick")
	print("waw I can't wait for your next show, " + magician.title() + "\n")
print("Thank you all that was a great show !")	

print('\n')
pizzas = ["papa\'s", "eddie\'s", "pizzaman"]
for pizza in pizzas:
	print('I love' +" "+ pizza.title() +" "+ 'pizza.')



#making numerical list
# use of range

for value in range(1,10):
 print(value)

print('\n')
num = list(range(1,21))
print(num)
print('\n')
squares=[]
for value in range(1,11):
	
	squares.append(value**2)
print(squares)

print('\n')



# statistics with list of numbers

digits = []
for value in range(1,13):
	digits.append(value*4)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))		
print('\n')



# list comprehension

comp = [value**2 for value in list(range(1,11))]
print(comp)
com=[value+4 for value in list(range(1,13))]
print(com)



# Try work 

counts=[]
for value in range(1,21):
	counts.append(value)
print(counts)
mill = []
for value in range(1,100):
	mill.append(value)
print(mill)	
print(min(mill))
print(max(mill))
print(sum(mill))
print('\n')
threes = [value*3 for value in range(1,11)]
print(threes)
print('\n')
cubess = []
for value in range(1,11):
	cubess.append(value**3)
print(cubess)
	
print('\n')

cubes = [value**3 for value in range(1,11)]
print(cubes)



# working with part of list
# slicing list

players = ['florence', 'ellie', 'sam', 'martha', 'randy']
print(players[0:3])

print(players[2:])
print(players[:3])
print(players[:-3])



# looping through slice

players = ['florence', 'ellie', 'sam', 'martha', 'randy']
for player in players[:3]:
	print(player.title())



# copying list

my_foods = ['ampesi', 'rice', 'potato']
friend_foods = my_foods[:]

print("These are my foods: ")
print(my_foods)

print("\nThese are my firend's foods: ")
print(friend_foods)	

my_foods.append('jollof')
friend_foods.append('creams bars')
print("These are my foods: ")
print(my_foods)

print("\nThese are my firend's foods: ")
print(friend_foods)



# Tuples

demp = (250,60)
print(demp[0])
print(demp[1])
print('\n')



#looping through tuple
demps = (260,50)
for demp in demps:
	print(demp)



# over writing tuples

demps = (250,60)
print('Original demps:')
for demp in demps:
	print(demp)
		
demps = (300,100)
print("\n Modified demps: ")
for demp in demps:
	print(demp)
print('\n')
	
# if statements

cities = ['tokyo', 'new york', 'MAIMI', 'texas']
for city in cities:
	if city == 'MAIMI':
		print(city.lower())
	else:
		print(city.title())
diseases = ['typhoid', 'fever', 'bp', 'whole in heart']
sam = input("\nPlease enter your disease: ")

if sam == 'typhoid':
	print("\nYou have typhoid.")
elif sam == ' bp':
	print("\nYou have BP.")
elif sam == 'whole in heart':
	print("\nYou have whole in heart.")
else:
	print("\nYour sickness is not in our list.\n")
	
print("\nThank you dear customer for using our service.\n")		
				
for disease in diseases:
	if disease == 'bp':
		print(disease.upper())
	else:
		print(disease.title())	
numps = []	
numpe = input("Enter any integer of your choosing btw 1 and 100: ")
numps.append(numpe)	

if numpe == value:
	print("Your integer is in range ! ")
elif numpe != value:
	print("Your integer is way out of range. Try again.")	
else:
	print('You did not follow simple instructions.')
print("Dear user this is your list below: ")
print(numps)		
		
	
# using AND to check conditions

goal = 30
print(goal < 31)
print(goal<= 50 and goal<= 35)
print(goal <= 40 and goal >= 36)
print('\n')


# using OR to check conditions

goal = 30
print(goal < 31)
print(goal<= 50 or goal<= 35)
print(goal <= 40 or goal >= 36)
print('\n')	


# checking for value in a list

cities = ['tokyo', 'new york', 'MAIMI', 'texas']
print('tokyo' in cities)
print('ghana'in cities)

# checking for not values in list

cities = ['tokyo', 'new york', 'MAIMI', 'texas']
city = 'ghana'

if city not in cities:
  print(city.title() +", you can continue borrowing money from USA")		

age = input("Kindly enter your age: ")
if age > str(18):
	print("You are now an adult and eligible to vote.")
elif age < str(18):
	print("You are not yet an adult and not eligble to vote.")
else:
	("Please enter a correct answer.\n Thank you." )	
		


# Asking for name and age 

print("Hey there what's your name ? ")
myName = input()
print("It's a pleasure meeting you, " + myName)
print("How old are you," + myName)
myage = input()
print("You will be "+ str(int(myage) +1) + " next year")
print("\n")
password = input()
if name == ' Sam':
	print('My name is ' + name)
if password == 'sunflower':
	print("Access Granted")
else:
	print("Wrong Password\n")
spam = 0
if spam < 5:
	print("This is an if statement.")
	spam = spam + 1
  
  
# While loop
spam = 0
while spam < 5:
	print("This is an if statement.")
	spam = spam + 1
	continue
	
name = ''
while name != 'myname':
	print('Please type your name')
	name = input()
	print("Thank you for your time")
print("\n")



# break usage
name = ''
while name != 'myname':
	print('Please type your name')
	name = input()
	break
	print("Thank you for your time")	
	continue
# infinite loop
while True:
     print('Hello world!\n')
     break
     
while True:
	print('Who are you?')
	name = input()
	if name == 'sam':
	
		print("Hello, " + name +", " + "  what's your password ? ( It's a fish) ")
		password = input()
		if password == 'star fish':
			break
print("Access granted")	
print("\n")

while True:
	print("Who are you ?")
	name =input()
	if name != 'joe':
		print("Hello, " + name +","+ "  what's your password ? ( It's a fish) ")
		password = input()
		if password != 'starfish':
			print("Forgot password ?")
		elif password == 'starfish':
			print("Access Granted")	
			break
		
# Importing modules
import random
for i in range(10,1,-1):
	print(random.randint(1, 20))
#Import examples
#random, sys
#os, math

	



	
