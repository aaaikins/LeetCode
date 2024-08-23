# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            cur = node

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                
            return prev

        reverse_list = reverse(head)
        node = reverse_list
        
        carry = 0
        while node:
            current_double = node.val * 2 + carry
            node.val = current_double % 10
            carry = current_double // 10
            if not node.next and carry:
                node.next = ListNode(carry)
                break
                
            node = node.next
        
        return reverse(reverse_list)
      
