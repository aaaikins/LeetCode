# Last updated: 12/18/2025, 1:50:46 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def reverse(node):
            prev, cur = None, node

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            return prev
        
        dummy = reverse(head)

        res = 0
        exp = 0
        while dummy:
            res += dummy.val * (2**exp)
            exp += 1
            dummy = dummy.next
        
        return res

        