# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        def dfs(node):
            if node == None:
                return
            elif node.val < key:
                node.right = dfs(node.right)
            elif node.val > key:
                node.left = dfs(node.left)
            else:
                if node.left == None and node.right == None:
                    return None
                elif node.left == None:
                    return node.right
                elif node.right == None:
                    return node.left
                else:
                    p = node.right
                    while p.left != None:
                        p = p.left
                    node.val , p.val = p.val , node.val
                    node.right = dfs(node.right)
            return node
        return dfs(root)
        
        
        
        
        
        
                    
                
        