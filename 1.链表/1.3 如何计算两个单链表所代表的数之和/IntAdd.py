"""
遍历两个链表，生成两个整数；
再将两个整数相加后的数，转换成链表
"""

from CreateNode import CreateNode


def nodeToInt(head):
    intStr = ""
    while head:
        intStr = str(head.data) + intStr
        head = head.next
    return int(intStr)


def add(head1, head2):
    intHead1, intHead2 = nodeToInt(head1), nodeToInt(head2)
    intHeadAll = intHead1 + intHead2
    return CreateNode("".join(str(intHeadAll)[::-1]))
