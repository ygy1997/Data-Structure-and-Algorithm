"""
      (1)找到链表的中间节点
      (2)对链表的后半部分进行逆序
      (3)把链表的前半部分和后半部分进行合并
"""
from CreateNode import LNode, NodeDisplay


def FindMiddleNode(head) -> LNode:
    """
    方法功能：找出链表的中间节点，把链表从中间断链成两个节点
    输入参数：链表头结点head
    返回值：链表中间节点
    """
    # fast一次遍历两个节点，当fast遍历到末尾时，slow遍历到一半
    fastStep = head
    slowStep = head
    slowpre = head
    while fastStep and fastStep.next:
        slowpre = slowStep
        fastStep, slowStep = fastStep.next.next, slowStep.next
    slowpre.next = None
    return slowStep


def Reverse(head) -> LNode:
    """
    方法功能：对不带头结点的单链表翻转
    输入参数:head链表头结点
    输出：逆序的头结点
    """
    preNode = head
    curNode = head.next
    nextNode = curNode.next
    preNode.next = None
    while curNode:
        curNode.next = preNode
        preNode = curNode
        curNode = nextNode
        if nextNode:
            nextNode = nextNode.next
    return preNode


def Reorder(head) -> LNode:
    """
    方法功能：对链表进行排序
    输入参数：head链表头结点
    """
    head2 = FindMiddleNode(head.next)
    head2 = Reverse(head2)
    curNode1 = head
    curNode2 = head2
    nextnode1 = head.next
    nextnode2 = head2.next

    while curNode2:
        curNode2.next = curNode1.next
        curNode1.next = curNode2
        NodeDisplay(head)

        curNode1, curNode2 = nextnode1, nextnode2
        if not nextnode2 or not nextnode1:
            break
        nextnode1 = nextnode1.next
        nextnode2 = nextnode2.next
