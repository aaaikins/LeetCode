# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        num = ""
        
        while temp:
            num += str(temp.val)
            temp = temp.next

        temp_sum = str(2 * int(num))
        print(temp_sum)
        
        result = ListNode(0)
        temp = result

        for char in temp_sum:
            result.next = ListNode(int(char))
            result = result.next

        return temp.next
      
