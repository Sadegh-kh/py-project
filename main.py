# b = open(r"note2.txt", "r+", encoding="utf-8")
# print(b.read())
# import random

# s = "sadegh"
# print(s.startswith("s"))
# a = ["a", "s", 1]
# a.reverse()
# a.insert(1, "s")
# print(a)
# a.remove("s")
# a.insert(1, "1")
# print(a)
# a.pop()
# print(a)
# print(random.uniform(100, 53242))
# print(random.sample(a, 2))

# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# print([BASE_DIR])
# print(BASE_DIR)


# print("a" + "b")
# s = {1, 2, 3, 4}
# s.remove(3)
# print(s)


# dis = {"dsa": 1, "ads": 2}
# print(dis.pop("dsa", 2))
# for i in dis.keys():
#     print(i)

# d = {"3": 1, "4": 5}
# print(d.pop())
# print(d)
tags = ["programming tag", "programming-tag", "programming_tag"]
new_tags = set()
for tag in tags:
    tag = tag.replace(" ", '_')
    tag = tag.replace("-", "_")
    new_tags.add(tag)

print(new_tags)
