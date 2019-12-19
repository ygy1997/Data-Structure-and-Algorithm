"""
输入:
    head->3->3->5->7
    head->5->9->8

输出:
    head->8->4->2->8 // 因为7533+895=8428
"""
from CreateNode import CreateNode, NodeDisplay
from IntAdd import add as intAdd
from NodeAdd import add as nodeAdd
if __name__ == '__main__':
    head1 = CreateNode([3, 3, 5, 7])
    head2 = CreateNode([5, 9, 8])
    NodeDisplay(head1)
    NodeDisplay(head2)
    print("整数相加法")
    headAll = intAdd(head1.next, head2.next)
    NodeDisplay(headAll)
    print("链表相加法")
    headAll = nodeAdd(head1.next, head2.next)
    NodeDisplay(headAll)
