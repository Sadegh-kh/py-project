even_numbers = lambda number: number % 2 == 0
odd_numbers = lambda number: number % 2 != 0
my_numbers = [1, 6, 8, 4, 3, 4, 54, 67, 23, 64, 56, 34, 97]
print(f"even numbers : {list(filter(even_numbers, my_numbers))}\nodd numbers : {list(filter(odd_numbers, my_numbers))}")
