# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head ; fast = head 
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        
        def reverse(node):
            if not node or not node.next:
                return node
            new_node = reverse(node.next)
            node.next.next = node
            node.next = None
            return new_node
        second = reverse(second)
        first = head
        dummy = ListNode(-1)
        curr = dummy
        while first or second:
            if first:
                curr.next = first
                first = first.next
                curr = curr.next
            if second:
                curr.next = second
                second = second.next
                curr = curr.next
        return dummy.next
        