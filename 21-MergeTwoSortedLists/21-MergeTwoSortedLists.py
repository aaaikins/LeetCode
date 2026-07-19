# Last updated: 7/19/2026, 7:58:35 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
9        if not l1:
10            return l2
11        if not l2:
12            return l1
13        
14        if l1.val <= l2.val:
15            l1.next = self.mergeTwoLists(l1.next, l2)
16            return l1
17        else:
18            l2.next = self.mergeTwoLists(l1, l2.next)
19            return l2
20        
21        