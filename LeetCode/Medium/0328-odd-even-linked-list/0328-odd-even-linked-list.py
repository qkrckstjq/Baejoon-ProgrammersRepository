# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        even_node = head
        odd_node = head.next
        odd_start = head.next
        
        while even_node.next is not None and even_node.next.next is not None:
            even_node.next = odd_node.next
            odd_node.next = even_node.next.next
            even_node = even_node.next
            odd_node = odd_node.next
        
        even_node.next = odd_start
        
        return head
        