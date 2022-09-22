class Node{
    int key;
    int val;
    Node next;
    Node pre;
    public Node(int key , int val){
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    int capacity;
    Node head = new Node(-1,-1);
    Node tail = new Node(-1,-1);
    HashMap<Integer,Node> cache = new HashMap<>();
    public LRUCache(int capacity) {
        head.next = tail; tail.pre = head;
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key))
            return -1;
        Node node = cache.get(key);
        moveToHead(node);
        return node.val;
    }
    
    public void put(int key, int value) {
        if (!cache.containsKey(key)) {
            Node node = new Node(key, value);
            addHead(node);
            cache.put(key,node);
            capacity --;
            if (capacity == -1){
                Node last = delTail();
                cache.remove(last.key);
                capacity ++;
            }
        } else {
            Node node = cache.get(key);
            node.val = value;
            moveToHead(node);
        }
        return ;
    }
    public void addHead(Node node){
        Node next = head.next;
        head.next = node; node.next = next;
        next.pre = node ; node.pre = head;
        return ;
    }
    public void del(Node node){
        Node pre = node.pre;
        Node next = node.next;
        pre.next = next; 
        next.pre = pre;
        return ;
    }
    public Node delTail(){
        Node last = tail.pre;
        del(last);
        return last ;
    }
    public void moveToHead(Node node){
        del(node);
        addHead(node);
        return ;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */