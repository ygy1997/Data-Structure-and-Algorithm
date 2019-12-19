from CreateNode import CreateNode,  LNode
from HashSetIsLoop import isLoop as hsIsLoop
from SFnodeIsLoop import isLoop as sfIsLoop
if __name__ == '__main__':
    head1 = CreateNode(range(1, 10))
    # 构造有环链表
    headLoop = LNode()
    head2 = CreateNode(range(1, 10))
    headLoop.next = head2  # 将headLoop指向head2的头结点
    while head2.next:
        head2 = head2.next
    head2.next = headLoop  # 将head2的尾节点指向Headloop
    print("方法一")
    hsIsLoop(head1)
    hsIsLoop(headLoop)
    print("方法二")
    sfIsLoop(head1)
    sfIsLoop(headLoop)
