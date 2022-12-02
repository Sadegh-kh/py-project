sort_fruit = lambda fruit: list(dict(fruit).items())[1][1]

my_fruit = [{"weight": 70, "apple": "Red"},
            {"weight": 58, "lubiya": "Green"},
            {"weight": 70, "moze": "Yellow"},
            {"weight": 30, "anar": "Red"},
            {"weight": 75, "nrengo": "Orange"},
            {"weight": 400, "portugize": "Blue"}, ]

print(sorted(my_fruit, key=sort_fruit))
