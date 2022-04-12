# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0 ; p1 = head
        
        while p1 != None:
            length += 1
            print(length)
            p1 = p1.next
        length = length // 2 + 1
        
        print(length)
        p1 = head
        while length != 1:
            p1 = p1.next
            length -= 1
        return p1
            