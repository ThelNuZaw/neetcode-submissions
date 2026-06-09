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
        #split half
        second = slow.next
        slow.next = None

        #make revere the second half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        #merge
        left = head
        right = prev

        while right:
            lnxt = left.next
            rnxt = right.next
            left.next = right
            right.next = lnxt
            left = lnxt
            right = rnxt
        
            



