# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while l1 != None:
            stack.append(l1.val)
            l1 = l1.next
        value1 = 0
        for i in range(len(stack)):
            value1 += stack.pop() * 10**i
        stack = []
        while l2 != None:
            stack.append(l2.val)
            l2 = l2.next
        value2 = 0
        for i in range(len(stack)):
            value1 += stack.pop() * 10**i
        value1 = str(value1+value2) 
        
        dummy = ListNode()
        p = dummy
        for i in value1:
            p.next = ListNode(i)
            p = p.next
        return dummy.next
        # return value1
        