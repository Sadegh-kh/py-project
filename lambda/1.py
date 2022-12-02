even_numbers = lambda number: True if number % 2 == 0 else False
list_number = [1, 2, 3, 5, 6, 7, 8, 30, 28, 36, 436, 215]
even_list = []
odd_list = []
for i in list_number:
    if even_numbers(i):
        even_list.append(i)
    else:
        odd_list.append(i)

print(
    f"even number is : {even_list}"
    f"\nodd number is : {odd_list}")
