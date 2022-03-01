# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if l1 == None:
        #     return l2
        # if l2 == None:
        #     return l1
        # if l2.val >= l1.val:
        #     l1.next = self.mergeTwoLists(l1.next,l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l2.next,l1)
        #     return l2
        final = ListNode(-1)
        p = final
        while l1 != None and l2 != None:
            if l2.val >= l1.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1 == None:
            p.next = l2
        else:
            p.next = l1
        return final.next