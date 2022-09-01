/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null){
            return head ;
        }
        ListNode ans  = new ListNode(-1) ;
        ListNode curr = ans ;
        ListNode p1 = head ;
        ListNode p2 = head.next ;
        while (p1 != null && p2 != null){
            curr.next = new ListNode(p2.val);
            if (p2.next != null){
                p2 = p2.next.next;
            } else{
                p2 = null;
            }
            curr = curr.next;
            curr.next = new ListNode(p1.val);
            if (p1.next != null){
                p1 = p1.next.next;
            } else {
                p1 = null;
            }
            curr = curr.next;
        }
        if (p1 == null){
            curr.next = p2;
        }
        else{
            curr.next = p1;
        }
        return ans.next;
    }
}