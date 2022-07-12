class Solution {
    public int maxProfit(int[] prices, int fee) {
        int buy = - prices[0] , sell = 0 , tempBuy , tempSell;
        for (int i = 1 ; i < prices.length ; i ++){
            tempBuy = buy ; 
            tempSell = sell ; 
            buy = Math.max(tempBuy,tempSell - prices[i]) ; 
            sell = Math.max(tempSell , tempBuy + prices[i] - fee) ; 
        }
        return sell ; 
    }
}