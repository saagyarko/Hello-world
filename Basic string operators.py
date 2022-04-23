#Basic string operators
astring="hello"
astring2="WORLD"
print(len(astring))  #len is used to find number of characters
print(len(astring2))

print(astring.index("l"))  #find it numerical position in the word

#counting the number of words in a word
print(astring.count("l"))

#slicing a string 
print(astring[0:4])
print(astring2[0:3:1])

#casing of strings
print(astring.upper())
print(astring2.lower())

#startwith and endwith commands
astring3="Hello World!"
print(astring3.startswith("Hello"))
print(astring3.endswith("!"))

#split function
print(astring3.split(" "))