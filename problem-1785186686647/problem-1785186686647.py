# Last updated: 7/27/2026, 5:11:26 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        if not head:
9            return 
10        
11        dummy = ListNode(val = 0, next=head)
12        slow, fast = dummy, dummy.next
13
14        for _ in range(n):
15            fast = fast.next
16
17        while slow and fast:
18            slow = slow.next
19            fast = fast.next
20
21        slow.next = slow.next.next
22
23        return dummy.next
24        