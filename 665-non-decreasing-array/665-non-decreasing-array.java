class Solution {
    public boolean checkPossibility(int[] nums) {
        int[] nums2 = new int[nums.length];
        for (int i = 0 ; i < nums.length ; i ++){
            nums2[i] = nums[i];
        }
        boolean front = true;
        boolean back = true;
        int cnt = 0;
        for (int i = 1 ; i < nums.length ; i++){
            // if (front == false)
            //     break;
            if (nums[i] >= nums[i-1])
                continue;
            if (cnt == 1){
                front = false;
                break;
            }
            nums[i] = nums[i-1];
            cnt ++;
        }
        cnt = 0 ; nums = nums2;
        for (int i = nums.length - 2 ; i >= 0; i--){
            // if (front == false)
            //     break;
            if (nums[i] <= nums[i+1])
                continue;
            if (cnt == 1){
                back = false;
                break;
            }
            nums[i] = nums[i+1];
            cnt ++;
        }
        return front || back;
    }
}