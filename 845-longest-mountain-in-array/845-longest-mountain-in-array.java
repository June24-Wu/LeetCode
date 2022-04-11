class Solution {
    public int longestMountain(int[] arr) {
        if(arr == null || arr.length < 3) return 0;

        int maxLen = 0;
        for(int i = 1; i < arr.length - 1; i++){
            int left = i - 1, right = i + 1;
            //如果两边的数大于当前数，则当前数不是‘山尖’
            if(arr[left] >= arr[i] || arr[right] >= arr[i]) continue;


            while(left > 0 && arr[left - 1] < arr[left] ){
                left--;
            }

            while(right < arr.length - 1 && arr[right] > arr[right + 1]){
                right++;
            }

            int currLen = right - left + 1;
            if(maxLen < currLen) maxLen = currLen;
        }

        return maxLen;
    }
}