# Last updated: 7/19/2026, 7:52:18 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        cur = head
10        prev = None
11
12        while cur:
13            temp = cur.next
14            cur.next = prev
15            prev = cur
16            cur = temp
17        
18        return prev