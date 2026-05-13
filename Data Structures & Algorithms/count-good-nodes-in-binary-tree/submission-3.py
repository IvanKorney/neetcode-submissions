# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dp(node,maxNum):
            if not node:
                return
            if node.val >= maxNum:
                maxNum = node.val
                res[0] += 1
            dp(node.left,maxNum)
            dp(node.right,maxNum)
            
        dp(root,-101)
        return res[0]
        