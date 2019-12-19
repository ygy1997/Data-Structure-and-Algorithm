"""
hashset去除冗余
"""


def removeDup(head):
    hashset = set()
    curNode = head.next
    preNode = head
    while curNode:
        if curNode.data in hashset:
            preNode.next = curNode.next
        else:
            hashset.add(curNode.data)
        preNode, curNode = curNode, curNode.next
