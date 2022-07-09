# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 1 -> 2         3 -> 4
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge_sort(node):
            if not node or not node.next:
                return node
            left = node
            slow = left ; fast = left.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next ; slow.next = None
            list1 = merge_sort(left)
            list2 = merge_sort(right)
            
            p1 = list1 ; p2 = list2
            res = ListNode(-1)
            curr = res
            while p1 and p2:
                if p1.val < p2.val:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next
                curr = curr.next
            if p1 == None:
                curr.next = p2
            elif p2 == None:
                curr.next = p1
            return res.next
        return merge_sort(head)
        
            
                
            
        