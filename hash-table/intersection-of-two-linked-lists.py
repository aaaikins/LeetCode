# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        tempB = headB
        listA = []
        # intersection = None

        while tempA:
            listA.append(tempA.val)
            tempA = tempA.next
        
        listA = listA[::-1]

        while tempB:
            if tempB.val in listA:
                return tempB
            tempB = tempB.next

        
        return None

            
            

        