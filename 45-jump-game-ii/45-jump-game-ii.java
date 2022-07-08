class Solution {
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp,Integer.MAX_VALUE);
        dp[0] = 0;
        for (int curr = 0 ; curr < nums.length; curr ++){
            for (int i = curr + 1 ; i < curr + nums[curr] + 1;i ++){
                if (i < nums.length)
                    dp[i] = Math.min(dp[i],dp[curr] + 1);
                
            }
        }
        
        return dp[nums.length - 1];
    }
}