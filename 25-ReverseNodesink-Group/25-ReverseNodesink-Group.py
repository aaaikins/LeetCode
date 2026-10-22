# Last updated: 10/22/2026, 6:54:10 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
8        dummy = ListNode(0, head)
9        groupPrev = dummy
10
11        while True:
12            # Step 1: Find the kth node
13            kth = groupPrev
14            for _ in range(k):
15                if not kth:
16                    break
17                kth = kth.next
18            if not kth:
19                break
20
21            # Step 2: Stop if fewer than k nodes remain
22            groupNext = kth.next
23            prev = groupNext
24            curr = groupPrev.next
25
26            # Step 3: Reverse the group
27            while curr != groupNext:
28                temp = curr.next
29                curr.next = prev
30                prev = curr
31                curr = temp
32
33            # Step 4: Reconnect the group
34            oldHead = groupPrev.next
35            groupPrev.next = prev
36            groupPrev = oldHead
37        
38        return dummy.next