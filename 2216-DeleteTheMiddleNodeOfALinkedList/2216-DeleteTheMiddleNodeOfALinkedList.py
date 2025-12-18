# Last updated: 12/18/2025, 1:50:29 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        temp = ListNode(next=head)
        slow = temp
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # print(slow)
        slow.next = slow.next.next
        # print(slow)

        return temp.next