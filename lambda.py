people = [
    {"name": "Hary", "house": "Griffindor"},
    {"name": "Draco", "house": "Slyterin"},
    {"name": "Cho", "house": "Raavenclaw"}
]

# def f(person):
#     return person["name"]
people.sort(key=lambda person: person["name"])

print(people)