# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        slow = head ; fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
        fast = head
        slow = slow.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        