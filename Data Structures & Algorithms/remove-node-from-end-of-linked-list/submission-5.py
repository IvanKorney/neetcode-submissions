# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        dummy.next = head
        cur = head
        while n:
            cur = cur.next
            n -= 1
        while cur:
            dummy = dummy.next
            cur = cur.next
        dummy.next = dummy.next.next
        return res.next
        