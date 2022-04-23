#Condition
x= 2
print(x==2)
print(x==3)
print(x<4)

#Boolean operators ("and" "or")
name="John"
age=23
if name=="John" and age==23:
    print("Your name is John  and you're %d years" %age)

if name=="John" or age==23:
    print("Your name is %s and you're %d years old." %(name,age))    

#"in" operator
name="John"
if name in ["John", "Rick"]:
    print("This means your name is in the list.")
else:
    print("Try again next time")  

#'is' operator
x=[12,12,13,14]
y=[12,12,13,14]
print(x==y)
print(x is y)      

#"not" operator
print(not False)
print((not False) == True)
print((not False) == (False))
print((not 1) != (3))


