# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(left,root,right):
            if not root:
                return True
            if not (root.val > left and root.val < right):
                return False
            else:
                return check(root.val,root.right,right) and check(left,root.left,root.val)
                 

        return check(float('-inf'),root,float('inf'))
        