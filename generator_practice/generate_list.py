def append_list(old_list):
    new_list = []
    s = 0
    for i in old_list:
        s += i
        new_list.append(s)
        yield new_list


old_list = [1, 4, 5, 6, 7, 8]
app = append_list(old_list)
for i in app:
    print(i)
