"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        vis = {}
        dummy = Node(0)
        curr = dummy
        while head:
            if head not in vis:
                vis[head] = Node(head.val)
            newhead = vis[head]
            curr.next = newhead
            curr = curr.next
            if head.random and head.random not in vis:
                vis[head.random] = Node(head.random.val)
            curr.random = vis[head.random] if head.random else None
            head = head.next
        return dummy.next
            
            
        