class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1)
            return 0;
        int p1 = 0 ; 
        int ans = 0 ;
        int total = 1 ; 
        for (int p2 = 0 ; p2 < nums.length;p2 ++){
            total = total * nums[p2];
            while (total >= k){
                total = total / nums[p1];
                p1 += 1 ;
            }
            ans += p2 - p1 + 1;
        }
        return ans ;
    }
}