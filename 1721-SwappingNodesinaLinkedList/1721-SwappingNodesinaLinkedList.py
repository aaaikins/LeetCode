# Last updated: 8/22/2026, 8:38:11 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        slow = fast = head
9
10        for _ in range(k - 1):
11            fast = fast.next
12
13        node1 = fast
14
15        while fast.next:
16            slow = slow.next
17            fast = fast.next
18        
19        node2 = slow
20 
21        node1.val, node2.val = node2.val, node1.val
22
23        return head