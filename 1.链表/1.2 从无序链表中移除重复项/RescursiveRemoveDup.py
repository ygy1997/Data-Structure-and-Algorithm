"""
递归遍历删除冗余
"""


def rescursiveRemoveDup(head):

    if not head.next:
        return head
    else:
        nextNode = rescursiveRemoveDup(head.next)
        preNode = head
        while nextNode:
            if nextNode.data == head.data:
                preNode.next = nextNode.next
            preNode, nextNode = nextNode, nextNode.next
        return head


def removeDup(head):
    head.next = rescursiveRemoveDup(head.next)
