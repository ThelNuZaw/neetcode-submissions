# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next #second
        slow.next = None #first

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        left = head
        right = prev

        while right:
            lnxt = left.next
            rnxt = right.next
            left.next = right
            right.next = lnxt
            left = lnxt
            right = rnxt
