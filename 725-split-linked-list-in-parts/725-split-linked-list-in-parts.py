# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        while node != None:
            n += 1
            node = node.next
        
        quotinent , reminder = n // k , n % k  # 3, 1 
        
        array = [None for i in range(k)]
        
        # p = head
        # i = 0
        # while i < k and p:
        #     array[i] = p
        #     split = quotinent + ( 1 if i < reminder else 0)
        #     for i in range(split - 1):
        #         p = p.next
        #     p2 = p.next
        #     p.next = None
        #     p = p2
        #     i+=1
        # return array

#         n = 0
#         node = head
#         while node:
#             n += 1
#             node = node.next
#         quotient, remainder = n // k, n % k

        parts = [None for _ in range(k)]
        i, curr = 0, head
        while i < k and curr:
            parts[i] = curr
            part_size = quotinent + (1 if i < reminder else 0)
            for _ in range(part_size - 1):
                curr = curr.next
            next = curr.next
            curr.next = None
            curr = next
            i += 1
        return parts
        