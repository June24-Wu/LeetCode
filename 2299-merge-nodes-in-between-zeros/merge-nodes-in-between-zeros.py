# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head ; curr = head.next
        dummy = ListNode(-1); ans = dummy 
        while curr != None:
            if pre.val == 0:
                curr_val = curr.val
            elif curr.val == 0:
                ans.next = ListNode(curr_val)
                ans = ans.next
                curr_val = 0
            else:
                curr_val += curr.val
            curr = curr.next
            pre = pre.next
        return dummy.next
