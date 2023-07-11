def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    else:
        low_sub = []
        high_sub = []
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                low_sub.append(i)
            elif i > pivot:
                high_sub.append(i)
        return quick_sort(low_sub) + [pivot] + quick_sort(high_sub)


tesl = [1, 5, 7, 8, 3, 2]
print(quick_sort(tesl))
