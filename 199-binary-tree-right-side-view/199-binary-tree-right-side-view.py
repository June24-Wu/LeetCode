# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        queue = [root]
        while queue:
            length = len(queue)
            ans.append(queue[0].val)
            for _ in range(length):
                node  = queue.pop(0)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return ans
        