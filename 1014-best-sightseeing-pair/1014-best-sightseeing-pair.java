class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int curr_max = -1000000000;
        int ans = -1000000000;
        for (int i = 0 ; i < values.length;i++){
            ans = Math.max(ans,values[i] - i + curr_max);
            curr_max = Math.max(curr_max,values[i] + i);
        }
        return ans;
        
    }
}