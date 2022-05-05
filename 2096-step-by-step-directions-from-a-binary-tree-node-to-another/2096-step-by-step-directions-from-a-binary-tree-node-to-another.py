# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        fa = {}   # 父节点哈希表
        s = None   # 起点节点
        t = None   # 终点节点

        # 深度优先搜索维护哈希表与起点终点
        def dfs(curr: TreeNode) -> None:
            nonlocal s, t
            if curr.val == startValue:
                s = curr
            if curr.val == destValue:
                t = curr
            if curr.left:
                fa[curr.left] = curr
                dfs(curr.left)
            if curr.right:
                fa[curr.right] = curr
                dfs(curr.right)
        
        dfs(root)

        # 求出根节点到对应节点的路径字符串
        def path(curr: TreeNode) -> List[str]:
            res = []
            while curr != root:
                par = fa[curr]
                if curr == par.left:
                    res.append('L')
                else:
                    res.append('R')
                curr = par
            return res[::-1]
        
        path1 = path(s)
        path2 = path(t)
        # 计算最长公共前缀并删去对应部分，同时将 path_1 逐字符修改为 'U'
        l1, l2 = len(path1), len(path2)
        i = 0
        while i < min(l1, l2):
            if path1[i] == path2[i]:
                i += 1
            else:
                break
        finalpath = 'U' * (l1 - i) + ''.join(path2[i:])   # 最短路径对应字符串 
        return finalpath

    
    
    # 超时

#         parents = {}
        
#         def dfs(node):
#             if node == None:return
#             if node.left == None and node.right == None:
#                 return
#             if node.left != None:
#                 parents[node.left] = node
#                 dfs(node.left)
#             if node.right != None:
#                 parents[node.right] = node
#                 dfs(node.right)
#         dfs(root)
#         queue = []
#         def find_start(node):
#             nonlocal queue
#             if node == None:
#                 return
#             if node.val == startValue:
#                 queue = [node]
#             find_start(node.left)
#             find_start(node.right)
#         find_start(root)
        
#         methods = [""]
#         visited = set()
#         length = len(queue)
#         while queue != []:
#             for _ in range(length):
#                 node = queue.pop()
#                 method = methods.pop()
#                 if node in visited: continue
#                 if node.val == destValue: return method
#                 for _ in range(3):
#                     if node in parents:
#                         queue.append(parents[node])
#                         methods.append(method + "U")
#                     if node.left != None:
#                         queue.append(node.left)
#                         methods.append(method + "L")
#                     if node.right != None:
#                         queue.append(node.right)
#                         methods.append(method + "R")
#                 visited.add(node)
#             length = len(queue)
        # return "UURL"
        