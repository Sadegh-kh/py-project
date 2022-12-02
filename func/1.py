def counter(value) -> int:
    count = 0
    for _ in value:
        count += 1
    return count


x = {7, 2, 3, 5}

print(counter(x))
