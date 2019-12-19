"""
输入:head->1->3->1->5->5->7
输出:head->1->3->5->7
"""
from traverseRemoveDup import removeDup as tsDup
from RescursiveRemoveDup import removeDup as rsDup
from hashsetRemoveDup import removeDup as hsDup
from CreateNode import CreateNode, NodeDisplay
if __name__ == '__main__':
    head1, head2, head3 = CreateNode(), CreateNode(), CreateNode()
    NodeDisplay(head1)
    print("顺序遍历删除重复项")
    tsDup(head1)
    NodeDisplay(head1)
    print("递归删除重复项")
    rsDup(head2)
    NodeDisplay(head2)
    print("hashset删除重复项")
    hsDup(head3)
    NodeDisplay(head3)
