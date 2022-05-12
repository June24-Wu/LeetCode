# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {root:None} # children : parents
        
        def dfs(node):
            nonlocal parents
            if node == None:return
            parents[node.left] = node
            parents[node.right] = node
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        visited = set()
        visited.add(target.val)
        queue = [target]
        length = len(queue)
        for _ in range(k):
            for i in range(length):
                node = queue.pop(0)
                if node.left != None and node.left.val not in visited:
                    queue.append(node.left)
                    visited.add(node.left.val)
                if node.right != None and node.right.val not in visited:
                    queue.append(node.right)
                    visited.add(node.right.val)
                if parents[node] != None and parents[node].val not in visited:
                    queue.append(parents[node])
                    visited.add(parents[node].val)
            length = len(queue)
        ans = []
        for i in queue:
            ans.append(i.val)
        # print(ans)
        return ans
        