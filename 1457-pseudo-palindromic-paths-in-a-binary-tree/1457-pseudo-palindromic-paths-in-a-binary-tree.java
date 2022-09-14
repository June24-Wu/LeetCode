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
    int ans = 0 ; 
    HashMap <Integer , Integer> table = new HashMap<>();
    public int pseudoPalindromicPaths (TreeNode root) {
        dfs(root);
        return ans ;
    }
    public void dfs(TreeNode node){
        if (node == null){
            return ;
        }
        table.put(node.val,table.getOrDefault(node.val,0) + 1);
        if (node.left == null && node.right == null){
            if (isValid(table))
                ans ++ ;
            table.put(node.val,table.get(node.val) - 1);
            return ;
        }
        dfs(node.left);
        dfs(node.right);
        table.put(node.val,table.get(node.val) - 1);
        return ;
    }
    public boolean isValid(HashMap<Integer,Integer> table){
        int cnt = 0 ;
        for (Map.Entry<Integer,Integer> entry : table.entrySet()){
            if (entry.getValue() % 2 == 1)
                cnt ++;
        }
        return cnt <= 1 ; 
    }
}