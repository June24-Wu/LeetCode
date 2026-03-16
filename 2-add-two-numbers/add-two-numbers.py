# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value1 = []
        value2 = []
        while l1:
            value1.append(str(l1.val))
            l1 = l1.next
        while l2:
            value2.append(str(l2.val))
            l2 = l2.next
        value2 = value2[::-1]
        value1 = value1[::-1]

        value1 = int("".join(value1)) + int("".join(value2))
        value1 = list(str(value1))[::-1]
        dummy = ListNode(-1)
        head = dummy
        for i in value1:
            head.next = ListNode(int(i))
            head = head.next
        return dummy.next
        