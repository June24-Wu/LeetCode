class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        HashMap<Integer,Integer> table = new HashMap<>() ; 
        List<Integer> ans = new ArrayList<>() ;
        for (int num : nums) {
            if (!table.containsKey(num)){
                table.put(num,0) ; 
            }
            table.put(num,table.get(num) + 1) ; 
        }
        for (Map.Entry<Integer,Integer> entry: table.entrySet()) {
            if (entry.getValue() == 2){
                ans.add(entry.getKey()) ; 
            }
        }
        return ans;
    }
}