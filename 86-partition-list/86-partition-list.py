# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1 = ListNode(-1) ; p2 = ListNode(-1)
        smallHead = p1 ; LargeHead = p2
        
        
        node = head
        
        while node != None:
            if node.val < x:
                p1.next = ListNode(node.val)
                p1 = p1.next
            else:
                p2.next = ListNode(node.val)
                p2 = p2.next
            node = node.next
        p1.next = LargeHead.next
        return smallHead.next
        
                
            
        