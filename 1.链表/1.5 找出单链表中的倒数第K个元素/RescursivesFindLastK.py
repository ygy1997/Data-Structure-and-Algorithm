"""
通过递归返回当前结点
尾节点的层数为1，倒数第二个结点尾2
"""


def RescursivesFindLastK(head, k):
    if not head.next:
        return head, k
    nextNode, count = RescursivesFindLastK(head.next, k)
    if count == 1:
        return nextNode, count
    else:
        return head, count - 1


def findLastK(head, k):
    head, _ = RescursivesFindLastK(head, k)
    return head
