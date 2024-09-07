# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA=set()
        listA=headA
        
        while listA:
            setA.add(listA)
            listA=listA.next
        
        listB = headB
        while listB:
            
            if listB in setA:
                return listB
            listB=listB.next

        return None