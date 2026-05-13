# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head
        cur2 = head
        last = None
        while cur:
            arr.append(cur)
            cur = cur.next
        l,r = 0, len(arr)-1
        while l <= r:
            cur2.next = arr[l]
            cur2 = cur2.next
            last = arr[l]
            l += 1
            if l > r:
                break
            cur2.next = arr[r]
            cur2 = cur2.next
            last = arr[r]
            r -=1
            if r < l:
                break
        if last:
            last.next = None
            
