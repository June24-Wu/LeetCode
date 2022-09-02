class Solution {
    public int brokenCalc(int start, int target) {
        int ans = 0;
        while (target > start){
            ans ++;
            if (target % 2 == 0){
                target = target / 2;
            } else {
                target ++;
            }
        }
        return ans + start - target ;
    }
}