class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int sum = 0;
        int p1 = 0 ;
        int ans = Integer.MAX_VALUE;
        for (int i = 0 ; i < nums.length ; i ++){
            sum += nums[i] ; 
        }
        if (sum < target){
            return 0 ; 
        }
        sum = 0 ; 
        
        for (int p2 = 0 ; p2 < nums.length ; p2 ++){
            sum += nums[p2];
            while (sum >= target){
                ans = Math.min(ans , p2 - p1 + 1) ;
                sum -= nums[p1] ; 
                p1 ++ ;
            }
        }
        return ans ; 
    }
}