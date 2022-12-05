def gen_range(start, end, step=1):
    while start < end:
        yield start
        start += step


def list_range(start, end, step=1):
    new_list = []
    while start < end:
        new_list.append(start)
        start += step
    return new_list


g = gen_range(10, 20)
for i in g:
    if i == 15:
        g.throw(ValueError("Error"))
