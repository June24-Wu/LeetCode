# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        curr = head
        while curr:
            len += 1
            curr = curr.next
        len = len // 2
        if len == 0:
            return None
        index = 1
        prev = head
        curr = head.next
        while curr:
            if index == len:
                prev.next = curr.next
                # print(prev.val,curr.val)
                break
            prev = curr
            curr = curr.next
            index += 1
        return head

        