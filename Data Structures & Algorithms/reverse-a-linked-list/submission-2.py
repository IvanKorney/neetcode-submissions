# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        stack = []
        cur = head
        curres = res
        while cur:
            stack.append(cur)
            cur = cur.next
        while stack:
            node = stack.pop()
            curres.next = node
            curres = curres.next
        curres.next = None
        return res.next