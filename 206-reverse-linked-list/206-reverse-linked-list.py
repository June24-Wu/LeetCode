# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#      recursion
        # if head == None:
        #     return None
        # if head.next == None:
        #     return head
        # headNode = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return headNode

        
        previous = None
        current = head
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
        