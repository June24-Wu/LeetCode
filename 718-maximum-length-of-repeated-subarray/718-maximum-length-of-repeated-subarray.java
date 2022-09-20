class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        int[][] dp = new int[nums1.length][nums2.length];
        int ans = 0;
        for (int i = 0 ; i < nums1.length ; i ++){
            for (int j = nums2.length - 1 ; j >= 0 ; j--){
                if (nums1[i] == nums2[j]){
                    dp[i][j] = i > 0 && j > 0 ? dp[i-1][j-1] + 1 : 1;
                    ans = Math.max(dp[i][j],ans);
                }
            }
        }
        return ans;
    }
}