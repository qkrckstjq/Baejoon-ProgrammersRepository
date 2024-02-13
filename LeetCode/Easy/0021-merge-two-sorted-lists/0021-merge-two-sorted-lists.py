# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        merged_node = None
        if list1.val < list2.val:
            merged_node = list1
            list1 = list1.next
        else:
            merged_node = list2
            list2 = list2.next    
        
        start_node = merged_node
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                merged_node.next = list1
                list1 = list1.next
            else:
                merged_node.next = list2
                list2 = list2.next
            merged_node = merged_node.next
        
        if list1 is None:
            merged_node.next = list2
        else:
            merged_node.next = list1
        
        return start_node
        