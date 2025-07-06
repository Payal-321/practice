public class ListNode {
     int val;
     ListNode next;

     // Constructor to create a new node
     ListNode(int x) {
     val = x;
     next = null;
     }
}

class Solution {
     public Listnode twoPassAlgorithm(ListNode head) {
          // o{N}
          int count = 0;
          ListNode current = head;
          while(current != null) {
               current = current.next;
               count++;
          }
          
          //o{N/2}
          current = head;
          for(int c = 0; c < count / 2; c++) {
               current = current.next;
          }
          return current;
     }
     
     public ListNode middleNode(ListNode head) {
          if(head == null || head.next == null)
          return head;
          // two pass algorithm
     }
}