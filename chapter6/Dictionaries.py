my_person={
    "name":"Dintle",
    "surname":"motswana",
    "age":"23",
    "city":"ekurhuleni"
    }

print(my_person["age"])
print(my_person["city"])
print(my_person["name"])
print(my_person["surname"])


favourite_num={
    "Simone": 4,
    "Thuthu": 7,
    "Leona": 8,
    "Birdie":13,
    "Sethu":3
}

print(f"Simone's favourite number is {favourite_num["Simone"]}")
print(f"Thuthu's favourite number is {favourite_num["Thuthu"]}")
print(f"Leona's favourite number is {favourite_num["Leona"]}")
print(f"Birdie's favourite number is {favourite_num["Birdie"]}")
print(f"Sethu's favourite number is {favourite_num["Sethu"]}")





favorite_languages = {
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")



# my_person={
#     "name":"Dintle",
#     "language":"Setswana",
#     "age":"23"
#     }
# print(my_person)

# my_person["gender"]="female"
  
# print(my_person)

# my_person["language"]="Sepedi"
# print(my_person)

# print(my_person.get("age"))

# print(my_person.pop)


# Mom={"name":"Precious",
#     "age" :"55",
#     "sign":"Gemini",
#     "hobbies":"reading" "gardening" "baking"}

# Sister={"name":"Lukhanyo",
#     "age" :"28",
#     "sign":"Taurus",
#     "hobbies":"shopping" "reading" "makeup"}

# Brother={"name":"Ntokozo",
#     "age" :"24",
#     "sign":"Aquarius",
#     "hobbies":"spinning" "dancing" "hosting"}


# MyFamily=(Mom,Sister,Brother)

# Son={"name":"Ntuthuko",
#     "age" :"08",
#     "sign":"baby",
#     "hobbies":"clapping" "dancing" "feeding"}

# MyFamily.append(Son)
# print(MyFamily)


# capitals={
#     "South Africa":"Pretoria",
#     "Namibia":"Windhoek",
#     "Kenya":"Nairobi"
# }
