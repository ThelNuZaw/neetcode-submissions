# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def common_div(first, second):
            cd = 1
            for i in range(1, min(first, second) + 1):
                if first % i == 0 and second % i == 0:
                    cd = i
            return cd

        cur = head
        while cur and cur.next:
            first = cur
            second = cur.next
            cd = common_div(first.val, second.val)
            cd_Node = ListNode(cd)
            first.next = cd_Node
            cd_Node.next = second
            cur = second
        return head


           
