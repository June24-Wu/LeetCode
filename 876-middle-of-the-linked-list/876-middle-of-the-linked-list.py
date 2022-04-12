# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 双指针
        p1 = head ; p2 = head
        
        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next
        return p1
        
        # 第一种解法
#         length = 0 ; p1 = head
        
#         while p1 != None:
#             length += 1
#             # print(length)
#             p1 = p1.next
#         length = length // 2 + 1
        
#         p1 = head
#         while length != 1:
#             p1 = p1.next
#             length -= 1
#         return p1
    

    
            