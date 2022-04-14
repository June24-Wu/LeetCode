# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1 ; p2 = l2
        l3 = ListNode(-1) ; p3 = l3
        add = 0
        while p1 != None or p2 != None:
            if p1 == None:
                p3.next = ListNode((p2.val + add) % 10)
                add = (p2.val + add) // 10
                p2 = p2.next ; p3 = p3.next
            elif p2 == None:
                p3.next = ListNode((p1.val + add) % 10)
                add = (p1.val + add) // 10
                p1 = p1.next ; p3 = p3.next
            else:
                p3.next = ListNode((p1.val + p2.val + add) % 10)
                add = (p1.val + p2.val + add) // 10
                p2 = p2.next ; p3 = p3.next ; p1 = p1.next
        if add != 0:
            p3.next = ListNode(add)
                
        return l3.next
            
            
        
        
        
        