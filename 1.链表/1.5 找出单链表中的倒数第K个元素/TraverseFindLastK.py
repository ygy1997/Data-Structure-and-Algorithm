"""
第一次遍历获得长度N
第二次遍历获位于第N-k位置上的结点
"""


def findLastK(head, k):
    N = 0
    curNode = head
    while curNode:
        N += 1
        curNode = curNode.next
    curNode = head
    while N - k > 0:
        N += -1
        curNode = curNode.next
    return curNode
