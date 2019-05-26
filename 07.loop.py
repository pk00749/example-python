list =[]
attributes = ['name', 'dob', 'gender']
values = [
    ['jason', '2000-01-01', 'male'],
    ['mike', '1999-01-01', 'male'],
    ['nancy', '2001-02-01', 'female']
]

for value in values:
    d = {}
    for j in range(len(attributes)):
        d[attributes[j]] = value[j]
    list.append(d)
print(list)


# expected outout:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]


