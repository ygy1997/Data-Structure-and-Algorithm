"""
输入：
    head->L0->L1->L2...Ln-1->Ln
输出:
    head->L0->Ln->L1->Ln-1->L2->Ln-2...
要求：
    不能申请新结点
    不能修改数据域
"""
from CreateNode import CreateNode, NodeDisplay
from NormalReorder import Reorder
if __name__ == '__main__':
    head = CreateNode(range(1, 7))
    NodeDisplay(head)
    print("开始重排序")
    Reorder(head.next)
    # NodeDisplay(head)
