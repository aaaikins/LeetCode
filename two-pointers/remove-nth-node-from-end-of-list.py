# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        temp = ListNode(0, head)
        slow = temp
        fast = head
        for _ in range(n):
            fast = fast.next

        while slow and fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        # print(fast)
        return temp.next
        