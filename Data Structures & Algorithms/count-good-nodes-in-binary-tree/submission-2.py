# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(root,maxNum):
            if not root:
                return 
            else:
                if root.val >= maxNum:
                    maxNum = root.val
                    res[0] += 1
                dfs(root.left,maxNum)
                dfs(root.right,maxNum)


        dfs(root,float("-inf"))
        return res[0]