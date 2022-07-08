class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int curr_max = prices[n - 1];
        int ans = 0;
        for (int i = n-2; i>=0 ;i--){
            if (prices[i] < curr_max){
                ans = Math.max(ans,curr_max - prices[i]);
            }
            if (prices[i] > curr_max)
                curr_max = prices[i] ; 
        }
        return ans ; 
    }
}