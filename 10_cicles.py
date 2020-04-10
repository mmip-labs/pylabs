
children = ['ivanov_2000','petrov_2005','sidorov_2002','gukin_2008']

names =[]

for child_name in children:

    surname = child_name.split('_')[0].title()

    print(surname)

    if surname.startswith('I'):
        continue

    names.append(surname)

print(names)




