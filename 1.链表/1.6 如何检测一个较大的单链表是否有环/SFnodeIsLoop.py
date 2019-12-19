"""
快慢指针
快指针比慢指针多遍历一次
当快指针重合到慢指针的时候说明有环
"""


def isLoop(head):
    slowNode = head.next
    fastNode = head.next.next
    while True:
        if fastNode == slowNode:
            print("该链表有环")
            break
        if not (fastNode.next and fastNode.next.next):
            print("该链表无环")
            break
        fastNode, slowNode = fastNode.next.next, slowNode.next
