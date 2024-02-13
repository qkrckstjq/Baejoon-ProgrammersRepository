# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_i = list1
        node_j = list2

        if node_i == None:
            return node_j
        if node_j == None:
            return node_i

        merged_node = None

        if node_i.val < node_j.val:
            merged_node = node_i
            node_i = node_i.next
        else:
            merged_node = node_j
            node_j = node_j.next

        cur_node = merged_node
        while node_i != None and node_j != None:
            if node_i.val >= node_j.val:
                cur_node.next = node_j
                node_j = node_j.next
            else:
                cur_node.next = node_i
                node_i = node_i.next
            cur_node = cur_node.next

        if node_i != None:
            cur_node.next = node_i

        if node_j != None:
            cur_node.next = node_j

        return merged_node

