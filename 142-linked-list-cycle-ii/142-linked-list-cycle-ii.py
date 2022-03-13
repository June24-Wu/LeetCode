# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        table = {}
        if head == None:return None
        p1 = head
        while p1 != None:
            if p1 in table.keys():
                return p1
            else:
                table[p1] = p1
                p1 = p1.next
        return None
        