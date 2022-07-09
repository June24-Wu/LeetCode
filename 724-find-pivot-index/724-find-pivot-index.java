class Solution {
    public int pivotIndex(int[] nums) {
        int[] left = new int[nums.length] ;
        int[] right = new int[nums.length] ;
        int res = 0;
        for (int i = 1 ; i < nums.length ; i ++){
            res = res + nums[i - 1];
            left[i] = res;
        }
        res = 0;
        for (int i = nums.length - 2 ; i >= 0 ; i --){
            res = res + nums[i + 1];
            right[i] = res;
        }
        for (int i = 0 ; i < nums.length ; i ++){
            if (left[i] == right[i])
                return i;
            
        }
        return -1 ;
        
    }
}