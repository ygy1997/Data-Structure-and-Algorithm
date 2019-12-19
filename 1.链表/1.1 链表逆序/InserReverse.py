"""
插入法逆序
"""


def Reverse(head):
    '''
    将原链表分割成待插链表和插入链表
    head->1->Null,2->3->4...7->Null
    插入链表从头结点后的第二个结点开始，
    插入链表头结点向待插链表Head节点后插入
    '''

    curNode = head.next.next  # 插入链表中的头节点
    head.next.next = None  # 使原链表第一个节点成为待插链表尾节点
    while curNode:
        # curNode->head.next
        nextNode, curNode.next = curNode.next, head.next
        # 使Head->curNode
        head.next = curNode
        # 此时head->curNode->head.next ，nextNode成为插入链表头结点
        curNode = nextNode
