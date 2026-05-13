# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            else:
                if p.val == q.val:
                    return isSameTree(p.right,q.right) and isSameTree(p.left,q.left)
                else:
                    return False
        
        
        if not subRoot:
            return True
        if not root: 
            return False
        else:
            if isSameTree(root,subRoot): 
                return True
            else:
                return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        
        
        
        
        
        
