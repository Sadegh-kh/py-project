def sub_multi(number):
    if number == 0:
        return
    if number % 3 == 0:
        print(number)
    sub_multi(number - 1)


sub_multi(10)
