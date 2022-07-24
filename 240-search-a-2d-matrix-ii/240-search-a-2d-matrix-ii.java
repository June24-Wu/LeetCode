class Solution {
    public boolean searchMatrix(int[][] mat, int target) {
        int m = mat.length;
        int n = mat[0].length;
        int x = m - 1;
        int y = 0 ;
        while (x >= 0 && y < n){
            if (mat[x][y] > target){
                x --;
            } else if (mat[x][y] < target){
                y ++;
            } else {
                return true;
            }
        }
        return false;
    }
}