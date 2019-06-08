#Dictionary

person = {
    "name": "Duc",
    "age": 22,
    "ex-gf": 3,
    "university": "FTU",
}

#key: value

#CRUD
#1. READ
#1.1 READ one
# name = person["name"]
# age = person["age"]
# print(name)
# print(age)

#1.2 READ many (hiển thị những key bên trái)
#loop by keys
# for key in person.keys():
#     print(key)

# #loop by values
# for value in person.values():
#     print(value)

#loop by items
# for key, value in person.items():
#     print(key, value)
#     #hoặc print ("{0}: {1}".format(key,value))

#2.CREATE/UPDATE
# #CREATE
# person["major"]="chinese"
# print(person)

# #UPDATE
# person["age"]=25
# print(person)

#3.DELETE
del person["ex-gf"]
print(person)