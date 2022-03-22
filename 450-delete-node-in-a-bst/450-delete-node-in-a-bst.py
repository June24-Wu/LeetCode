# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_successor(node):
            while node.left != None:
                node = node.left
            return node
                
        def dfs(node):
            if node == None:return node
            elif key > node.val:
                node.right =  dfs(node.right)
            elif key < node.val:
                node.left =  dfs(node.left)
            else:
                if node.left == None and node.right == None:
                    print(node.val)
                    node = None
                elif node.left == None:
                    node = node.right
                elif node.right == None:
                    node = node.left
                else:
                    d_node = find_successor(node.right)
                    node.val, d_node.val = d_node.val,node.val
                    node.right = dfs(node.right)
            return node
        return dfs(root)
                    
                
        