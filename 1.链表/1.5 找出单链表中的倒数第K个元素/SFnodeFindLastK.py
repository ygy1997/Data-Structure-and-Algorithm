"""
快指针比慢指针先走k步，即快慢指针间隔7个k个结点
快指针走到头时，慢指针刚好在倒数第K个
"""


def findLastK(head, k):
    slowNode = head
    fastNode = head
    while k > 0:
        k += -1
        fastNode = fastNode.next
    while fastNode:
        fastNode = fastNode.next
        slowNode = slowNode.next
    return slowNode
