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
    List<List<Integer>> ans = new ArrayList<>();
    List<Integer> path = new ArrayList<>();
    int targetSum;
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        this.targetSum = targetSum;
        dfs(root);
        return ans;
    }
    
    public void dfs(TreeNode node){
        if (node == null)
            return;
        path.add(node.val);
        if (node.left == null && node.right == null){
            int pathsum = 0;
            List<Integer> new_path = new ArrayList<>();
            for (int i : path){
                pathsum += i;
                new_path.add(i);
            }
            if (pathsum == targetSum){
                ans.add(new_path);
            }
        }
        dfs(node.left);
        dfs(node.right);
        path.remove(path.size()-1);
        return;
    }
}