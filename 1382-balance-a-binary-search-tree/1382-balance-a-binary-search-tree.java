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
    ArrayList<Integer> list = new ArrayList<Integer>();
    public TreeNode balanceBST(TreeNode root) {
        dfs(root);
        return build(0,list.size()-1);
    }
    public void dfs(TreeNode node){
        if (node == null)
            return;
        dfs(node.left);
        list.add(node.val);
        dfs(node.right);
        return;
    }
    
    public TreeNode build(int left , int right){
        if (left > right) 
            return null;
        if (left == right)
            return new TreeNode(list.get(left));
            
        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(list.get(mid));
        node.left = build(left,mid-1);
        node.right = build(mid+1,right);
        return node;
    }
}