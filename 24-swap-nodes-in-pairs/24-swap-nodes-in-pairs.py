# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:return head
        dummy = ListNode(-1) ; dummy.next = head
        
        left = dummy ; first = dummy.next ; second = first.next ; right = second.next
        while True:
            first.next = right
            second.next = first
            left.next = second
            left = first
            first = right
            if first == None:
                break
            second = first.next
            if second == None:
                break
            right = second.next
        return dummy.next