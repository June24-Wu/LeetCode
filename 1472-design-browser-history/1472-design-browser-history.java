class Node{
    String val;
    Node next;
    Node pre;
    public Node(String val){
        this.val = val;
    }
}

class BrowserHistory {
    Node curr;
    public BrowserHistory(String homepage) {
        curr = new Node(homepage);
    }
    
    public void visit(String url) {
        curr.next = new Node(url);
        curr.next.pre = curr;
        curr = curr.next;
        return ;
    }
    
    public String back(int steps) {
        for (int i = 0 ; i < steps ; i ++){
            if (curr.pre != null)
                curr = curr.pre;
        }
        return curr.val;
    }
    
    public String forward(int steps) {
        for (int i = 0 ; i < steps ; i ++){
            if (curr.next != null)
                curr = curr.next;
        }
        return curr.val;     
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */