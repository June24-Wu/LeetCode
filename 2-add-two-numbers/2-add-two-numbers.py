# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(-1)
        curr = node
        p1 = l1 ; p2 = l2 ; remain = 0
        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            val , remain = (val1 + val2 + remain) % 10 , (val1 + val2 + remain) // 10
            curr.next = ListNode(val)
            curr = curr.next
            p1 = p1.next if p1 else p1
            p2 = p2.next if p2 else p2
        curr.next = ListNode(remain) if remain > 0 else None
        return node.next
        