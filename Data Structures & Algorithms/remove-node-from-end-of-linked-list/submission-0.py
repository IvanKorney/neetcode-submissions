# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur2 = dummy
        cur = head
        while n > 0:
            cur = cur.next 
            n -= 1
        while cur != None:
            cur = cur.next
            cur2 = cur2.next
        cur2.next = cur2.next.next
        return dummy.next