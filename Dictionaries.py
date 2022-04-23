countries={"Ghana":"Accra", "USA": "Washingon", "China":"Tokyo"}
print(countries["Ghana"])
countries["China"]= "Shanghai"
print(countries["China"])
print("The capital of Ghana is "+ countries["Ghana"])

for key in countries:
    print(key)
#Accessing the keys and values
print(countries.get("Ghana"))
print(countries.get("China"))
print(countries.keys()) #to access the main names

print(countries.values()) #to get the sub names

new_countries=countries.fromkeys(countries)
print(new_countries)
print(max(countries))
print(len(countries))
print(min(countries))

#deleting from dictionary
del countries["Ghana"]
print(countries)
print(sorted(countries))
