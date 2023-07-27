from collections import deque
from graph import graph


def find_seller(name: str):
    if name[-2:] == "'m":
        return True
    return False


def search(name: str) -> bool:
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if find_seller(person):
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


print(search('sadegh'))
