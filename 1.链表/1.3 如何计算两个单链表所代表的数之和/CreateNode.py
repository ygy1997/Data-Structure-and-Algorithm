class LNode:
    """
        self.data数据域
        slef.next指针域
    """

    def __init__(self):
        self.data = None
        self.next = None


def CreateNode(NodedataList):
    """
    创建单链表:
        head->3->1->5
        head->5->9->2
    """
    curNode = head = LNode()
    head.data = "head"
    for i in NodedataList:
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
