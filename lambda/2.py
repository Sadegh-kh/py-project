sort_person = lambda value: value[1]

person_list = [('ali', 65), ('abas', 85), ('sara', 45), ('bijan', 24), ('saeed', 554), ('sadegh', 125)]
print(sorted(person_list, key=sort_person))
