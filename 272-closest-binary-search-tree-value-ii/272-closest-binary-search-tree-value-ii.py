# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = [] # ( - abs, node.val)
        
        def dfs(node):
            nonlocal heap
            if node == None:
                return
            distance = abs(target-node.val)
            heapq.heappush(heap,(distance,node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        ans = []
        for _ in range(k):
            curr = heapq.heappop(heap)
            ans.append(curr[1])
        return ans