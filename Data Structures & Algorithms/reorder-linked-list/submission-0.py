# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        l1 = head
        l2 = prev
        while l2.next:
            buff1 = l1.next 
            buff2 = l2.next
            l1.next = l2
            l2.next = buff1
            l1 = buff1
            l2 = buff2
            
        