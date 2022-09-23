class Solution {
    HashMap<Integer, Integer> table = new HashMap<>();
    long mod = (int) Math.pow(10, 9) + 7;
    public int numberOfWays(int numPeople) {
        if (table.containsKey(numPeople))
            return Integer.valueOf(table.get(numPeople));
        if (numPeople == 0 || numPeople == 1)
            return 1;
        long ans = 0;
        for (int i = 0 ; i < numPeople; i+=2) {
            ans += ((long) numberOfWays(i) * numberOfWays(numPeople - i - 2));
            ans %= mod;
        }
        table.put(numPeople,(int)ans);
        return (int) ans;
    }
}

// class Solution {
    
//     HashMap<Integer, Integer> map = new HashMap<>();
//     int mod = (int) Math.pow(10, 9) + 7;

//     public int numberOfWays(int numPeople) {
//         if (numPeople % 2 != 0) {
//             return 0;
//         }
//         if (numPeople == 2 || numPeople == 0) {
//             return 1;
//         }
//         if (numPeople <= 0) {
//             return 0;
//         }
//         if (map.containsKey(numPeople)) {
//             return map.get(numPeople);
//         }
//         long ways = 0;
//         for (int second = 1; second < numPeople; second++) {
//             if (second == numPeople - 1) {
//                 ways += numberOfWays(numPeople - 2);
//                 ways %= mod;
//             } else {
//                 ways += ((long) numberOfWays(second - 1) * numberOfWays(numPeople - second - 1));
//                 ways %= mod;
//             }
//         }
//         map.put(numPeople, (int) ways);
//         return (int) ways;
//     }
// }