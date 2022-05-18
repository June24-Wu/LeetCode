# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        def dfs(node):
            nonlocal ans
            if node == None:
                ans.append("None")
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        print(",".join(ans))
        return ",".join(ans)
        
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        treeList = data.split(",")
        root = None
        def dfs():
            nonlocal treeList
            val = treeList.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans