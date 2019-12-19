"""
顺序遍历删除冗余
"""


def removeDup(head):
    preNode = curNode = head.next
    nextNode = curNode.next
    while curNode.next:
        while nextNode:
            if nextNode.data == curNode.data:
                preNode.next = nextNode.next
            preNode, nextNode = nextNode, nextNode.next
        preNode = curNode = curNode.next
        nextNode = curNode.next
