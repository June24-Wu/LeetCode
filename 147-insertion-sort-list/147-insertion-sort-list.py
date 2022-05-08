# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = head ; p = curr.next
        
        while p:
            if p.val > curr.val:
                curr = curr.next
                p = p.next
            else:
                pre = dummy
                while pre.next.val < p.val:
                    pre = pre.next
                curr.next = p.next
                p.next = pre.next
                pre.next = p
                p = curr.next
        return dummy.next
        