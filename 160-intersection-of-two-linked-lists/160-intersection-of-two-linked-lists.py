# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if headA.val == None or headB.val == None:
        #     return None
        # pA , pB = headA , headB
        # while (pA != pB):
        #     pA = pA.next if pA != None else headB
        #     pB = pB.next if pB != None else headA
        # return pA
        p1 , p2 = headA , headB
        while p1 != p2 :
            
            if p1 != None:
                p1 = p1.next
            else:
                p1 = headB
            if p2 != None:
                p2 = p2.next
            else:
                p2 = headA
        return p1
        