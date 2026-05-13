# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        removeIndex = len(arr)-n
        if removeIndex == 0:
            return head.next
        cur2 = head
        while removeIndex != 1:
            cur2 = cur2.next
            removeIndex -= 1
        cur2.next = cur2.next.next
        return head

        