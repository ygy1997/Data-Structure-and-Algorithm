from CreateNode import CreateNode,  NodeDisplay
from LocalReverse import Reverse as LocalRS
from RecursiveReverse import Reverse as ResursiveRs
from InserReverse import Reverse as inserRs
if __name__ == '__main__':
    head1, head2, head3 = CreateNode(), CreateNode(), CreateNode()
    NodeDisplay(head1)
    print("就地逆序")
    LocalRS(head1)
    NodeDisplay(head1)
    print("递归逆序")
    ResursiveRs(head2)
    NodeDisplay(head2)
    print("插入法逆序")
    inserRs(head3)
    NodeDisplay(head3)
