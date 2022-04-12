# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []
        p1 = head
        while p1 != None:
            li.append(p1.val)
            p1 = p1.next
        
        p1 = 0 ; p2 = len(li) - 1
        while p1 <= p2:
            if li[p1] == li[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True
            
        