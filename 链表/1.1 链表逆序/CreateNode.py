class LNode:
    """
        self.data数据域
        slef.next指针域
    """

    def __init__(self):
        self.data = None
        self.next = None


def CreateNode():
    """
    创建单链表:head->1->2->3->4->5->6->7
    """
    curNode = head = LNode()
    head.data = "head"
    for i in range(1, 8):
        curNode.next = LNode()
        curNode.next.data = i
        curNode = curNode.next
    return head


def NodeDisplay(head):
    # 显示链表
    curNode = head
    NodeStr = ""
    while curNode:
        NodeStr += str(curNode.data) + "->"
        curNode = curNode.next
    NodeStr += "Null"
    print(NodeStr)
