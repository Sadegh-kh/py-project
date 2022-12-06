def tri_num(n):
    for i in range(n):
        for j in range(i):
            yield i
        print()


num=tri_num(10)
for i in num:
    print(i,end="")