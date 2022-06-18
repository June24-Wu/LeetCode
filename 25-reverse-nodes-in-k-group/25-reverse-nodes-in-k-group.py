# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(a,b):
            pre = None  ; curr = a ; next = None
            while curr != b:
                next = curr.next
                curr.next = pre
                pre = curr
                curr = next
            return pre
        
        def dfs(node):
            if node == None:
                return None
            a = b = node
            for i in range(k):
                if b == None:
                    return node
                b = b.next
            newNode = reverse(a,b)
            a.next = dfs(b)
            return newNode
        return dfs(head)

        