class Solution:
    def reverseList(self, head):
        curr, prev = head, None
        while curr:
            next, curr.next = curr.next, prev
            prev, curr = curr, next
        return prev