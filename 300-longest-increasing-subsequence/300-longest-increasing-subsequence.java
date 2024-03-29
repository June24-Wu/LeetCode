class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        for (int i = 0 ; i < nums.length;i++){
            dp[i] = 1;
        }
        for (int i = 0 ; i < nums.length;i++){
            for (int j = i - 1 ; j >= 0 ; j -- ){
                if (nums[i] > nums[j]){
                    dp[i] = Math.max(dp[i],dp[j] + 1);
                }
            }
        }
        int ans = 0;
        for (int i = 0 ; i < nums.length;i++){
            ans = Math.max(dp[i],ans);
        }
        return ans;
        
    }
}