# Last updated: 7/8/2026, 3:21:32 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        slow, fast = head, head
10
11        while fast and fast.next:
12            slow = slow.next
13            fast = fast.next.next
14
15            if slow == fast:
16                temp = head
17                while temp != slow:
18                    temp = temp.next
19                    slow = slow.next
20
21                return temp
22        return None
23        
24        return None
25        # seen = set()
26
27        # curr = head
28
29        # while curr:
30        #     if curr in seen:
31        #         return curr
32        #     seen.add(curr)
33        #     curr = curr.next
34        # return None
35        