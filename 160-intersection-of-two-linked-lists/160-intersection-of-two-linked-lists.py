# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA.val == None or headB.val == None:
            return None
        pA , pB = headA , headB
        while (pA != pB):
            pA = pA.next if pA != None else headB
            pB = pB.next if pB != None else headA
        return pA
        