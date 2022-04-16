class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        root = None
        flag = True
        def dfs(node):
            nonlocal flag
            if preorder == []:
                flag = False
                return None
            val = preorder.pop(0)
            if val == "#":
                node = None
                return
            node = TreeNode(int(val))
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        
        root = dfs(None)
        return flag and preorder == []
         
                
        