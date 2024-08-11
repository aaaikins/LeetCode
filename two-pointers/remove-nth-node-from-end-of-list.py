# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        temp = ListNode(next=head)
        slow = temp
        fast = head

        for i in range(n):
            fast = fast.next
            
        
        while slow and fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
 
       

        return temp.next
        