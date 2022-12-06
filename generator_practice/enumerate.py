def list_counter(old_list):
    i = 0
    while i < len(old_list):
        yield tuple([i, old_list[i]])
        i += 1


my_list = [1, 2, 3, 6, 7, 5, 46, 46]
for i in list_counter(my_list):
    print(i)
