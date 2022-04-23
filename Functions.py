#Functions
def myfunction():
    print("This is a function")
myfunction()    

#functions with arguments
def myfun(name,greetings):
    print("Hi %s, %s to you." %(name,greetings))
myfun("John", "Good Afternoon")   

#returning with "return" keyword
def myfun1(a,b):
    return a + b
print(myfun1(1 , 3) )


#exercise
def list_benefits():
    return "More organized", "More readable code", "Easier code reuse", "Allowing programmers to share and connect worldwide"

def build_sentence(benefits):
    return "%s is a benefit of Python function" %benefits

def sum_of_sentences():
    list_of_benefits=list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence("\n"+benefit))
sum_of_sentences()        