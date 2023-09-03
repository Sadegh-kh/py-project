class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a1, a2, a3 = LinkNode(2), LinkNode(4), LinkNode(3)

a1.next = a2
a2.next = a3

b1, b2, b3 = LinkNode(5), LinkNode(6), LinkNode(4)

b1.next = b2
b2.next = b3


def to_list(head: LinkNode):
    help_list = []
    currnt = head
    while currnt:
        help_list.append(str(currnt.val))
        currnt = currnt.next

    return help_list


# list1, list2 = to_list(a1), to_list(b1)

# num1, num2 = int("".join(list1[::-1])), int("".join(list2[::-1]))

# print(num1 + num2)


def solution(p1: LinkNode, p2: LinkNode) -> LinkNode:
    head = LinkNode()
    curr = head
    c = 0
    while p1 or p2 or c:
        p1, v1 = (p1.next, p1.val) if p1 else (p1, 0)
        p2, v2 = (p2.next, p2.val) if p2 else (p2, 0)
        c, sum_ = divmod(v1 + v2 + c, 10)
        curr.next = LinkNode(sum_)

        curr = curr.next

    return head.next


my_list = to_list(solution(a1, b1))
print(my_list)
