import time


# 3,2,1
# 3,timer(2)
def timer(number):
    if number == 0:
        return 0
    print(number)
    time.sleep(1)
    return timer(number - 1)


print(timer(5))
