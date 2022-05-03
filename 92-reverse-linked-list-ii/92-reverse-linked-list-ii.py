# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None or head == None or left == right:
            return head
        dummy = ListNode(0) ; dummy.next = head
        length = 0
        curr = dummy
        while length != right:
            if length == left - 1:
                leftNode = curr
            curr = curr.next
            length += 1
        rightNode = curr.next
        node = leftNode.next
        leftNode.next = None
        curr.next = None
        # return node
        
        pre = None
        curr = node
        while curr != None:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        # return pre
        leftNode.next = pre
        while pre.next != None:
            pre = pre.next
        pre.next = rightNode
        return dummy.next
        