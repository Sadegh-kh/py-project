def sum_req(arr: list) -> int:
    x = arr[0]
    arr.pop(0)
    if len(arr) == 0:
        return x
    else:
        return x + sum_req(arr)


def count_req(arr: list) -> int:
    x = 1
    arr.pop(0)
    if len(arr) == 0:
        return 1
    else:
        return x + count_req(arr)


def max_(arr: list) -> int:
    if len(arr) <= 1:
        return arr[0]
    else:
        m = max_(arr[1:])
        return m if m > arr[0] else arr[0]


if __name__ == '__main__':
    print(sum_req([2, 3, 6, 4]))
    print(count_req([2, 3, 6, 4]))
    print(max_([2, 3, 6, 4, 10, 9]))
