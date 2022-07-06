class Solution {
    public int maxProduct(int[] nums) {
        int mincurr = nums[0] ; 
        int maxcurr = nums[0] ; 
        int ans = maxcurr ; 
        
        for (int i = 1 ; i < nums.length ;i++){
            int curr = nums[i];
            int temp_mincurr = Math.min(curr,Math.min(curr * mincurr,curr * maxcurr));
            maxcurr = Math.max(curr,Math.max(curr * mincurr,curr * maxcurr));
            mincurr = temp_mincurr;
            ans = Math.max(maxcurr,ans);
        }
        return ans;
        
    }
}