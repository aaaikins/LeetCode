# Last updated: 7/8/2026, 3:02:55 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        # slow, fast = head, head
10
11        # while fast and fast.next:
12        #     slow = slow.next
13        #     fast = fast.next.next
14
15        #     if slow == fast:
16        #         return slow
17        
18        # return None
19        seen = set()
20
21        curr = head
22
23        while curr:
24            if curr in seen:
25                return curr
26            seen.add(curr)
27            curr = curr.next
28        return None
29        