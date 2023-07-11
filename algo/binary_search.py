def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = my_list[mid]

        if guess == item:
            return mid
        elif item < guess:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    lis = [12, 3, 5, 76, 8, 4]
    lis.sort()
    test = binary_search(lis, 76)
    print(test)
