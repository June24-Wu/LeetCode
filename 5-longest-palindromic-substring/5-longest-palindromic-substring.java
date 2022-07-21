class Solution {
    public String longestPalindrome(String s) {
        int n = s.length() ; 
        int[][] dp = new int[n][n];
        int length = 1;
        String ans = s.substring(0,1);
        for (int i = n - 1 ; i >= 0 ; i--){
            for (int j = i ; j < n ; j++){
                if (i==j){
                    dp[i][j] = 1;
                    continue;
                }
                if (s.charAt(i) == s.charAt(j)){
                    if (j - i == 1){
                        dp[i][j] = 2;
                    } else {
                        dp[i][j] = dp[i+1][j-1] > 0? dp[i+1][j-1] + 2 : 0;
                    }
                    if (dp[i][j] > length){
                        length = dp[i][j];
                        ans = s.substring(i,j+1);
                    }
                }
            }
        }
        return ans;
    }
}