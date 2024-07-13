# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            temp = current.next

            current.next = previous
            # Set prev node to current node
            previous = current
            # Set current node to next node
            current = temp
        
        # Return previous node
        return previous





        

        