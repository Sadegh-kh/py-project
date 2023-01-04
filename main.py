def check_len(obj):
    try:
        print(len(obj))
    except TypeError:
        print("Sorry")


x = 5
y = [1, 2, 3, 45, 65]
check_len(x)
check_len(y)
