"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldCurr = head
        table = {} # old : new
        table[None] = None
        while oldCurr != None:
            newCurr = Node(oldCurr.val)
            table[oldCurr] = newCurr
            oldCurr = oldCurr.next
        oldCurr = head
        while oldCurr != None:
            oldNext = oldCurr.next; oldRandom = oldCurr.random
            newCurr = table[oldCurr]
            newCurr.next = table[oldNext] ; newCurr.random = table[oldRandom]
            oldCurr = oldCurr.next
        return table[head]
            
        