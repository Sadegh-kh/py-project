s = [
    [1, 2, 3, 4, 5],
    [31, 72, 23, 41, 35],
    [12, 213, 23, 64, 7]
]

s1 = []

for column in range(len(s[:])):
    t_row = []
    for row in s:
        t_row.append(row[column])
    s1.append(t_row)
print(s1)
# step 1 ->
# t_row=[]
# for column in range(len(s[:])):
#     t_row.append([row[column] for row in s])

# step 2 ->
# t_row = [[row[column] for row in s] for column in range(len(s[:]))]
# print(t_row)


s2 = [[row[column] for column in range(len(s[:]))] for row in s]
print(s2)
