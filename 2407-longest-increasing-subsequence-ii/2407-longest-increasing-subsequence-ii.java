class SegmentTree{
    int n ; int tree_size ;
    int[] nums ; int[] tree;
    public SegmentTree(int[] nums){
        this.nums = nums;
        this.n = nums.length;
        this.tree_size = this.n * 4;
        this.tree = new int[tree_size];
        build(0,0,n-1);
    }
    private void build(int root , int start , int end){
        if (start == end){
            tree[root] = nums[start];
            return;
        }
        int left_root = root * 2 + 1;
        int right_root = root * 2 + 2;
        int mid = start + (end - start) / 2;
        build(left_root,start,mid);
        build(right_root,mid+1,end);
        return;
    }
    public void update(int index, int val){
        update(0,0,n-1,index,val);
        return ;
    }
    private void update(int root,int start,int end,int index,int val){
        if (start == end && start == index){
            nums[index] = val;
            tree[root] = val;
            return ;
        }
        int left_root = root * 2 + 1;
        int right_root = root * 2 + 2;
        int mid = start + (end - start) / 2;
        if (index >= start && index <= mid){
            update(left_root,start,mid,index,val);
        }
        if (index >= mid+1 && index <= end){
            update(right_root,mid + 1,end,index,val);
        }
        tree[root] = Math.max(tree[left_root],tree[right_root]);
    }
    public int query(int left,int right){
        return query(0,0,n-1,left,right);
    }
    private int query(int root,int start , int end, int left , int right){
        if (right < start || left > end){
            return 0;
        }
        if (start >= left &&  end <= right){
            return tree[root];
        }
        int left_root = root * 2 + 1;
        int right_root = root * 2 + 2;
        int mid = start + (end - start) / 2;
        return Math.max(query(left_root,start,mid,left,right),query(right_root,mid+1,end,left,right));
    }
}


class Solution {
    public int lengthOfLIS(int[] nums, int k) {
        int maxVal = 0;
        for (int i : nums){
            maxVal = Math.max(i,maxVal);
        }
        int[] array = new int[maxVal];
        int ans = 0;
        SegmentTree tree = new SegmentTree(array);
        for (int i : nums){
            int max_length = tree.query(i - k,i-1);
            tree.update(i,max_length+1);
            ans = Math.max(ans,max_length+1);
        }
        return ans ;
    }
}