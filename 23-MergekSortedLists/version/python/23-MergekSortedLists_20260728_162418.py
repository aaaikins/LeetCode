# Last updated: 7/28/2026, 4:24:18 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8    
9        def merge2Lists(l1, l2):
10            dummy = ListNode()
11            tail = dummy
12            while l1 and l2:
13                if l1.val <= l2.val:
14                    tail.next = l1
15                    l1 = l1.next
16                else: 
17                    tail.next = l2
18                    l2 = l2.next
19                tail = tail.next
20            
21            tail.next = l1 or l2
22            return dummy.next
23
24        if len(lists) < 1:
25            return None
26
27        merged = lists[0]
28        for ll in lists[1:]:
29            merged = merge2Lists(merged, ll)
30        
31        return merged