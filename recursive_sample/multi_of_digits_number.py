def multi(number):
    if number == 0:
        return 1
    new_number = number % 10
    if new_number >= 5:
        new_number *= multi(number // 10)
        return new_number
    return multi(number // 10)


number = 591684
print(multi(number))
