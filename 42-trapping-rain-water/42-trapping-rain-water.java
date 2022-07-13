class Solution {
    public int trap(int[] height) {
        int[] left = new int[height.length] ; 
        int[] right = new int[height.length] ; 
        int leftmax = 0;
        int rightmax = 0;
        int ans = 0 ;
        for (int i = 0 ; i < height.length ; i ++){
            left[i] = leftmax;
            leftmax = Math.max(leftmax,height[i]);
        }
        for (int i = height.length - 1 ; i >= 0 ; i --){
            right[i] = rightmax;
            rightmax = Math.max(rightmax,height[i]);
        }
        for (int i = 0 ; i < height.length ; i ++){
            ans += Math.max(0,Math.min(right[i],left[i]) - height[i]);
        }
        return ans ;
        
    }
}