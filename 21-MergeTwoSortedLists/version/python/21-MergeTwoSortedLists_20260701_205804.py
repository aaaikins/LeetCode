# Last updated: 7/1/2026, 8:58:04 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        new_list = ListNode()
9        curr = new_list
10
11        while list1 and list2:
12            if list1.val < list2.val:
13                curr.next = ListNode(list1.val)
14                list1 = list1.next
15            else:
16                curr.next = ListNode(list2.val)
17                list2 = list2.next
18
19            curr = curr.next
20        
21        if list1:
22            curr.next = list1
23
24        if list2:
25            curr.next = list2       
26
27        return new_list.next
28        