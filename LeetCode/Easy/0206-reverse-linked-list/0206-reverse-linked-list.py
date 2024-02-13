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
            prev_next_node = current_node.next
            current_node.next = reverse_node
            reverse_node = current_node
            current_node = prev_next_node
        
        return reverse_node
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None or head.next == None:
#             return head

#         prev_node = None
#         cur_node = head
#         while cur_node != None:
#             next_node = cur_node.next
#             cur_node.next = prev_node
#             prev_node = cur_node
#             cur_node = next_node

#         return prev_node