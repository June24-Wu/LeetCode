class MyCircularQueue {
    private int left;
    private int right;
    private int size;
    private int[] array;
    public MyCircularQueue(int k) {
        this.array = new int[k];
        this.left = left ; 
        this.right = right;
        this.size = k;
    }
    
    public boolean enQueue(int value) {
        if (isFull()){
            return false;
        }
        array[right%size] = value;
        right ++;
        return true;
        
    }
    
    public boolean deQueue() {
        if (isEmpty())
            return false;
        left ++;
        return true;
    }
    
    public int Front() {
        if (isEmpty())
            return -1;
        return array[left % size];
    }
    
    public int Rear() {
        if (isEmpty())
            return -1;
        return array[(right - 1) % size];
    }
    
    public boolean isEmpty() {
        return left == right;
    }
    
    public boolean isFull() {
        return right - left == size;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */