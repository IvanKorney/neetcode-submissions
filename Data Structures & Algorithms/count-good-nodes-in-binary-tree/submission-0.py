# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res =[0]
        def dfs(maxNum,root):
            if not root:
                return 
            else:
                if root.val >= maxNum:
                    maxNum = root.val
                    res[0] += 1
                dfs(maxNum,root.left)
                dfs(maxNum,root.right)
        dfs(root.val,root)
        return res[0]
                

            