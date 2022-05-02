# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                x = curr.next.val
                p = curr.next
                while p != None and p.val == x:
                    p = p.next
                curr.next = p
            else:
                curr = curr.next
        return dummy.next
                
        