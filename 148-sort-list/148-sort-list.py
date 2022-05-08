# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return head
        
        
        def sort(node):
            if node.next == None:return node
            left = node ; right = node.next
            while right != None and right.next != None:
                left = left.next
                right = right.next.next
            right = left.next
            left.next = None
            node = sort(node)
            right = sort(right)
            # return node
            return merge(node,right)
            # return right
        
        
        def merge(node1,node2):
            dummy = ListNode(-1) ; p = dummy ; p1 = node1 ; p2 = node2
            while p1 != None or p2 != None:
                if p2 == None or (p1 != None and p2 != None and p1.val < p2.val):
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            return dummy.next
        return sort(head)