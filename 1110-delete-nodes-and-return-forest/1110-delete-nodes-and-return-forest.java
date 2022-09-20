/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<TreeNode> ans = new ArrayList<>();
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        root = dfs(root,to_delete);
        if (root != null)
            ans.add(root);
        return ans;
    }
    public TreeNode dfs(TreeNode node, int[] to_delete){
        if (node == null)
            return null;
        node.left = dfs(node.left,to_delete);
        node.right = dfs(node.right,to_delete);
        for (int i : to_delete){
            if (node.val == i){
                if (node.left != null)
                    ans.add(node.left);
                if (node.right != null)
                    ans.add(node.right);
                return null;
            }
        }
        return node;
    }

}