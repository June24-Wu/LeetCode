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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null)
            return head;
        ListNode res = new ListNode();
        ListNode ans = res;
        ListNode p1 = head , p2 = head.next;
        while (p2 != null){
            if (p1.val != p2.val){
                ans.next = new ListNode(p1.val);
                p1 = p2;
                p2 = p1.next;
                ans = ans.next;
                continue;
            }
            while (p2 != null && p2.val == p1.val){
                p2 = p2.next;
            }
            p1 = p2;
            if (p2 != null)
                p2 = p2.next;
        }
        ans.next = p1;
        return res.next ;
    }
}