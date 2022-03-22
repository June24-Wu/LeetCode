# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # def dfs(inorder_left,inorder_right,postorder_left,postorder_right):
        #     if inorder_left == inorder_right:
        #         return TreeNode(inorder[inorder_left])
        #     if postorder_left == postorder_right:
        #         return TreeNode(postorder[postorder_left])
        #     if inorder_right < inorder_left or postorder_left > postorder_right:
        #         return None
        #     mid_val = postorder[postorder_right]
        #     inorder_mid_index = 0
        #     while inorder[inorder_mid_index] != mid_val:
        #         inorder_mid_index += 1
        #     postoder_right_start = 0
        #     if inorder_mid_index + 1 >= len(inorder):
        #         root = TreeNode(val = mid_val)
        #     while postorder[postoder_right_start] != inorder[inorder_mid_index + 1]:
        #         postoder_right_start += 1
        #     root = TreeNode(val = mid_val)
        #     root.left = dfs(inorder_left,inorder_mid_index-1,postorder_left,postoder_right_start-1)
        #     root.right = dfs(inorder_mid_index + 1,inorder_right,postoder_right_start,postorder_right-1)
        #     return root
        # root = dfs(0,len(inorder)-1,0,len(postorder)-1)
        # return root'
        def helper(in_left, in_right):
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None

            # 选择 post_idx 位置的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            index = idx_map[val]

            # 构造右子树
            root.right = helper(index + 1, in_right)
            # 构造左子树
            root.left = helper(in_left, index - 1)
            return root

        # 建立（元素，下标）键值对的哈希表
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)

            
        