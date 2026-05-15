# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        carry = 0

        while l1 or l2 or carry:
            l1val,l2val = 0,0
            if l1:
                l1val = l1.val
                l1 = l1.next
            if l2:
                l2val = l2.val
                l2 = l2.next
            total = l2val + l1val + carry
            carry = total // 10
            val = total % 10
            node = ListNode(val,None)
            cur.next = node
            cur = cur.next



        return head.next