"""
hashSet用来存放引用
"""


def isLoop(head):
    hashSet = set()
    while head:
        if not head.next:
            print("该链表无环")
            break
        if id(head) in hashSet:
            print("该链表有环")
            break
        hashSet.add(id(head))
        head = head.next
