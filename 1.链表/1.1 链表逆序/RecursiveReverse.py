
"""
递归逆序
"""

reverseNodeHead = None  # 定义逆转链表头结点


def ResursiveReverse(head):
    """
    ①每次递归获取逆转链表的尾节点
    ②保存原链表的尾节点做头结点
    输入:head
    方法功能:逆置链表
    输出:逆置链表的尾节点
    """
    if head.next:
        LNode = ResursiveReverse(head.next)  # 获取递归得来的尾节点
        LNode.next, head.next = head, None  # 当前结点指向空，并将尾节点指向当前结点
    else:
        global reverseNodeHead  # 申明使用逆转链表头结点
        reverseNodeHead = head  # 将原链表尾节点保存为头结点
    return head  # 返回逆置链表的尾节点


def Reverse(head):
    """
    输入:head
    方法功能:递归逆序
    """
    global reverseNodeHead
    ResursiveReverse(head.next)
    head.next = reverseNodeHead
