/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    HashSet<TreeNode> table = new HashSet<>();
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
        for (TreeNode node : nodes){
            table.add(node);
        }
        return find(root);
    }
    public TreeNode find(TreeNode node){
        if (node == null || table.contains(node)){
            return node;
        }
        TreeNode left = find(node.left);
        TreeNode right = find(node.right);
        if (left == null){
            return right ;
        }
        if (right == null){
            return left;
        }
        return node;
    }
}