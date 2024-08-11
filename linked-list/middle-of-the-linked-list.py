# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        

        while temp:
            temp = temp.next
            length += 1
        print(length)
        fast = head
        for i in range(length//2):
            fast = fast.next
        
        return fast


        