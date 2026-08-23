# Last updated: 8/22/2026, 8:11:21 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head:
9            return
10
11        dummy = ListNode(next=head)
12        prev = dummy
13        first, second = head, head.next
14
15        while first and second:
16            temp = second.next
17            second.next = first
18            # if temp:
19            first.next = temp
20            prev.next = second
21            prev = first
22            first = temp
23            second = temp.next if temp else None
24        
25        return dummy.next