
"""
就地逆序
"""


def Reverse(head):
    """
    输入:head
    方法功能:就地逆序
    输出:None #没有输出
    """
    curNode = head.next  # curNode:当前遍历到的结点
    preNode = None  # curNode的前驱结点
    nextNode = curNode.next  # curNode的后继节点

    while curNode.next:  # 如果当前结点不是尾结点
        curNode.next = preNode  # 将当前结点指向上一个结点

        preNode = curNode  # 更新前驱结点
        curNode = nextNode  # 更新遍历结点
        nextNode = curNode.next  # 更新后继结点

    curNode.next = preNode  # 将尾结点指向倒数第二个结点
    head.next = curNode  # 将头结点指向尾节点
