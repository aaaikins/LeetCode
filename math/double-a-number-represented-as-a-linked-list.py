# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        current = head
        while current:
            num = num * 10 + current.val
            current = current.next
        
        # Step 2: Double the integer
        num *= 2
        
        # Step 3: Convert the doubled number back to a linked list
        dummy = ListNode(0)
        current = dummy
        for digit in str(num):
            current.next = ListNode(int(digit))
            current = current.next
        
        # Step 4: Return the new linked list
        return dummy.next
      
