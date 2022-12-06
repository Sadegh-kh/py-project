def recognize_number(char: str):
    i = 1
    char = char.lower()
    while True:
        if char == 'e' and i % 2 == 0:
            yield i
        elif char == 'o' and i % 2 != 0:
            yield i
        i += 1


char = input("Enter your char you want (o,e): ")
rec_num = recognize_number(char)
print(next(rec_num))
print(next(rec_num))
print(next(rec_num))
print(next(rec_num))
