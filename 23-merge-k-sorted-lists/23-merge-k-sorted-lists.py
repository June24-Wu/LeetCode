# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l,r):
            if l == r:
                return lists[l]
            if l > r:
                return None
            mid = (l+r) // 2
            return mergeSort(merge(l,mid),merge(mid+1,r))
        # ans = None
        
        def mergeSort(node1,node2):
            dummy = ListNode(-1)
            p = dummy
            p1 = node1 ; p2 = node2

            while p1 != None or p2 != None:
                if p2 == None or (p2!= None and p1 != None and p1.val <= p2.val):
                    p.next = p1
                    p1 = p1.next
                    p = p.next
                else:
                    p.next = p2
                    p2 = p2.next
                    p = p.next
            return dummy.next
        return merge(0,len(lists)-1)
        