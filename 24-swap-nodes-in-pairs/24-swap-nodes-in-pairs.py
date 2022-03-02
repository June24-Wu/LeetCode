# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        
        while prev != None:
            if prev.next == None or prev.next.next == None:
                break
            p1 = prev.next
            p2 = p1.next
            next = p2.next
            prev.next = p2
            p2.next = p1
            p1.next = next
            prev = p1
        return dummy.next