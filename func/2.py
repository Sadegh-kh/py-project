def square(number):
    for i in range(1, number):
        divisor = number // i
        if number % i == 0 and divisor == i:
            print(f"this is square {i} * {i}")
            break
    else:
        print("it isn't square number ")


x = 169
square(x)
