# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,minVal,maxVal):
            if not root:
                return True
            if root.val<=minVal or root.val>=maxVal:
                return False

            l = dfs(root.left,minVal,root.val)
            r = dfs(root.right,root.val,maxVal)
        
            if not l or not r:
                return False
            return True
        return dfs(root,float('-inf'),float('inf'))
        