class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1] ; 

        dp[0] = 1 ;
        int length = dp.length ; 
        for (int j = 0 ; j < dp.length ; j ++ ){
            for (int i : nums){
                if (j - i >= 0)
                    dp[j]  += dp[j-i];
            }
            // System.out.println(Arrays.toString(dp));
        }
        return dp[target];
    }
}