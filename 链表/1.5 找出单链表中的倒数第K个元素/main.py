from CreateNode import CreateNode, NodeDisplay
from TraverseFindLastK import findLastK as tsFindLastK
from SFnodeFindLastK import findLastK as sfFindLastK
from RescursivesFindLastK import findLastK as rsFindLastK
if __name__ == '__main__':
    head = CreateNode(range(1, 10))
    target = 2
    NodeDisplay(head)
    print("方法一")
    Node = tsFindLastK(head.next, k=target)
    print("找到该节点{0}".format(Node.data))
    print("方法二")
    Node = sfFindLastK(head.next, k=target)
    print("找到该节点{0}".format(Node.data))
    print("方法三")
    Node = rsFindLastK(head.next, k=target)
    print("找到该节点{0}".format(Node.data))
