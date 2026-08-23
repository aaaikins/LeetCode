# Last updated: 8/22/2026, 8:31:05 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        dummy = ListNode(next=head)
9        node1 = dummy
10
11        for _ in range(k):
12            node1 = node1.next
13        print(node1.val)
14        node2, fast = dummy, node1
15
16        while node2 and fast:
17            node2 = node2.next
18            fast = fast.next
19        print(node2.val)
20        
21        node1.val, node2.val = node2.val, node1.val
22
23        return head