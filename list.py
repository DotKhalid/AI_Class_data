# person_list  = ["ali","hamza","usama","khalid","ahmed"]
# numbers = [2,4,5,6,7]

# print(person_list)
# print(type(person_list))
# print(numbers)
# print(len(person_list))
# print(person_list[2])
# print(person_list[-2])
# print(person_list[2:4])


# person_list[2] = "ahmed"
# print(person_list)

# person_list.insert(2, "alia")
# print(person_list)

# person_list.append("hadi")

# print(person_list)

# person_list.extend(numbers)
# print(person_list)

# person_list.remove("hamza")
# print(person_list)

# if "hadi" in  person_list:
#     print("hadi availabele hai")



#list
#tuple
#sets
#dictionary

# fruits = ("apple","banana", "mango")

# # fruits[1] = "anaar" not allowed

# print(type(fruits))

# new_fruits = list(fruits)

# print(type(new_fruits))

# new_fruits[2] = "Anaar"

# fruits = tuple(new_fruits)

# print(fruits)

# print(new_fruits)

# cars = {"gli", "civic", "mehran"}

# print(cars)

data = {
    "car" : "mehran",
    "name" : "ali",
    "age" : 23,
    "subject": ["urdu ", "math"]
    

}


print(data["subject"])
print(len(data))


print(data.get("name"))

a = data.keys()

data["address"] = "Karachi"

print(data)




