from copy import copy

nums = [1, 2, 3]
new_nums = copy(nums)
for i in nums:
    new_nums.append(i)
print(new_nums)
s = [1, 2, 3, 4]
d = [2, 4, 5, 7]
for i in s:
    if i in d:
        d.remove(i)

print(d)
a = {"a0": 1, "b": 3}
a.update({"a": 3})
print(a)
b = {1, 2}
c = {2, 3}
d = b & c
print(d.pop())
print(set([[1, 2, 3], [2, 3, 4]]))
