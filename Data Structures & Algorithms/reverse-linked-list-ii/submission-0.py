# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        LP = dummy
        cur = head
        for i in range(left - 1):
            LP = cur
            cur = cur.next

        prev = None
        for i in range(right- left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

       
        LP.next.next= cur
        LP.next = prev
        return dummy.next
        