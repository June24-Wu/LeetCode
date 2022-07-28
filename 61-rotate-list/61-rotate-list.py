# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head == None or head.next == None:
            return head
        length = 1
        p = head
        while p.next != None:
            length += 1
            p = p.next
        p.next = head
        k = length - (k % length)
        
        for i in range(k):
            p = p.next
        newHead = p.next
        p.next = None
        return newHead