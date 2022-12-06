def rev_char(str):
    for i in range(len(str) - 1, -1, -1):
        yield str[i]


name = "sadegh"
rev = rev_char(name)
for i in rev:
    print(i)
