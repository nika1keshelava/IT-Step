my_dict = {
    "name":"nika",
    "surname": "keshelava",
    "age": 22,
    "location": "Tbilisi",
    "children": ["gio", "sandro", "luka"]
}
#key:value

#dictionary is ordered
#changeable
#NO duplicates

# print(my_dict["location"])
# print(my_dict["surname"])

# my_dict["children"][1] = "nika"
# print(my_dict)

my_dict["age"] = 23

my_dict.pop("location")
print(my_dict)


couple_dict = {
    "nika" : {
        "age": 22,
        "surname": "keshelava"
    },
    "mariami":{
        "age" : 20,
        "surname" : "ksovreli"
    }
    
}

print(len(couple_dict))