# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(node1,node2):
            ans = ListNode(-1)
            res = ans
            p1 = node1 ; p2 = node2
            while p1 and p2:
                if p1.val < p2.val:
                    res.next = p1
                    p1 = p1.next
                else:
                    res.next = p2
                    p2 = p2.next
                res = res.next
            if not p1:
                res.next = p2
            else:
                res.next = p1
            return ans.next
        
        
        while len(lists) > 1:
            node1 = lists.pop(0)
            node2 = lists.pop(0)
            node = merge(node1,node2)
            lists.append(node)
        return lists[0]
        
        