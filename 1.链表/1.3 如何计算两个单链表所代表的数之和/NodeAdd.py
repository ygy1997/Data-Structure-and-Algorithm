"""
由于两个链表都是从个位开始，保证了可以让两个链表正向时，都是相同的位相加
使用carry用来表示是否需要进位
如果两个链表其中一个链表已经遍历完毕，那么直接连接没有遍历完毕的链表
"""
from CreateNode import LNode


def add(head1, head2):
    headAll = LNode()
    curNode = LNode()
    headAll.data = "head"
    headAll.next = curNode
    carry = curNode.data = 0
    while True:
        if head1 and head2:
            carry, surplus = divmod(head1.data + head2.data, 10)
            curNode.data += surplus
            head1, head2 = head1.next, head2.next
        if not head1 and head2:
            curNode.next = head2
            curNode.next.data += carry
            break
        if not head2 and head1:
            curNode.next = head1
            curNode.next.data += carry
            break
        curNode.next = LNode()
        curNode.next.data = carry
        curNode = curNode.next

    return headAll
