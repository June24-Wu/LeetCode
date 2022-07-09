class Solution {
    public int[] runningSum(int[] nums) {
        int[] ans = new int[nums.length];
        int val = 0;
        for (int i = 0 ; i < nums.length ; i ++){
            val += nums[i];
            ans[i] = val;
        }
        return ans ;
    }
}