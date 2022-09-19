class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[] dp = new int[text1.length()];
        int ans = 0;
        for (int i = 0 ; i < text2.length();i ++){
            for (int j = dp.length -1 ; j >= 0 ; j --){
                if (text1.charAt(j) == text2.charAt(i)){
                    int maxVal = 0;
                    for (int k = 0 ; k < j ; k ++){
                        maxVal = Math.max(dp[k],maxVal);
                    }
                    dp[j] = Math.max(dp[j],maxVal + 1);
                    ans = Math.max(dp[j],ans);
                }
            }
        }
        return ans;
    }
}