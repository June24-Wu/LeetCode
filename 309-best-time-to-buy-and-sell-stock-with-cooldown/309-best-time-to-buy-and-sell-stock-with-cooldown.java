class Solution {
    public int maxProfit(int[] prices) {
        int[] dp = new int[3] ;
        dp[0] = -prices[0];
        int[] temp ;
        for (int i = 1 ; i < prices.length; i ++){
            temp = dp.clone();
            dp[0] = Math.max(temp[0],temp[2] - prices[i]);
            dp[1] = Math.max(temp[1],temp[0] + prices[i]) ; 
            dp[2] = Math.max(temp[1],temp[2]);
        }
        return Math.max(dp[1],dp[2]) ;
        
    }
}