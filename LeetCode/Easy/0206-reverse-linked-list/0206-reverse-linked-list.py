# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        reverse_node = None
        current_node = head
        
        while current_node is not None:
            prev_next_node = current_node.next  #현재 노드의 다음 노드 살려두기
            current_node.next = reverse_node    #현재 노드의 다음을 끊어진 이전 노드로
            reverse_node = current_node         #
            current_node = prev_next_node
        
        return reverse_node