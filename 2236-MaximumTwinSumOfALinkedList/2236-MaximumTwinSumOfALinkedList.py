# Last updated: 12/18/2025, 1:50:28 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        l, r = head, prev
        maxTwin = 0

        while r:
            maxTwin = max(l.val + r.val, maxTwin)
            l = l.next
            r = r.next
        
        return maxTwin
        