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
        p = head
        dummy = Node(-1)
        p2 = dummy
        table = {}  # old : new
        while p:
            node = Node(p.val,p.next,None) # new node
            table[p] = node
            p2.next = node
            p2 , p = p2.next , p.next
        
        p = head
        while p:
            if p.random != None:
                table[p].random = table[p.random]
            else:
                table[p].random = None
            p = p.next
        return dummy.next

            