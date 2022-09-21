class Solution {
    List<Integer> ans = new ArrayList<>();
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int res = 0;
        for (int i : nums){
            if (i % 2 == 0){
                res += i;
            }
        }
        for (int idx = 0 ; idx < queries.length; idx ++){
            int index = queries[idx][1];
            int val = queries[idx][0];
            if (nums[index] % 2 == 0 && val % 2 == 0){
                res += val;
            } else if (nums[index] % 2 == 0 && val % 2 != 0){
                res -= nums[index];
            } else if (nums[index] % 2 != 0 && val % 2 != 0){
                res += nums[index] + val;
            }       
            nums[index] += val;
            ans.add(res);
        }
        int[] a = new int[queries.length];
        int cnt = 0;
        for (int i : ans){
            a[cnt] = i;
            cnt ++;
        }
        return a;
    }
}