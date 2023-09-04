from typing import Optional


class NodeLink:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


a, b, c = NodeLink(1), NodeLink(6), NodeLink(3)
a.next = b
b.next = c
c.next = None

my_list = []
head = NodeLink()
head.next = a
while head.next != None:
    head = head.next
    my_list.append(head.value)

print(my_list)


class Solution:
    def hasCycle(self, head: Optional[NodeLink]) -> bool:
        # Method 1 time : O(n) memory : O(n)
        # visited_node = set()
        # current_node = head
        # if head == None:
        #     return False

        # while current_node:
        #     if current_node.next in visited_node:
        #         return True
        #     visited_node.add(current_node)
        #     current_node = current_node.next
        # return False

        # Method 2 time:O(n) Memory:O(1) (hare and tortoise method)

        slow_node = head
        fast_node = head

        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            if fast_node == slow_node:
                return True
        return False
