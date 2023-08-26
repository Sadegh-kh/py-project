b = open(r"note2.txt", "r+", encoding="utf-8")
print(b.read())
import random

s = "sadegh"
print(s.startswith("s"))
a = ["a", "s", 1]
a.reverse()
a.insert(1, "s")
print(a)
a.remove("s")
a.insert(1, "1")
print(a)
a.pop()
print(a)
print(random.uniform(100, 53242))
print(random.sample(a, 2))

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

print([BASE_DIR])
print(BASE_DIR)
