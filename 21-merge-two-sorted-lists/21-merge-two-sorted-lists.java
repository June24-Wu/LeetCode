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
    public ListNode mergeTwoLists(ListNode p1, ListNode p2) {
        
        ListNode res = new ListNode() ;
        ListNode ans = res;
        while (p1 != null && p2 != null){
            if (p1.val < p2.val){
                ans.next = p1;
                p1 = p1.next;
                ans = ans.next;
            } else {
                ans.next = p2;
                p2 = p2.next ; 
                ans = ans.next;
            }
        }
        if (p1 == null)
            ans.next = p2;
        if (p2 == null)
            ans.next = p1;
        return res.next;
    }
}