def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        yield b
        a = b + a
        b = b + a


x = fibonacci()
i = 10
setb = []
while i > 0:
    setb.append(next(x))
    i -= 1
print(setb)
