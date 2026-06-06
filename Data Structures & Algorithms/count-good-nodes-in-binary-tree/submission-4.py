# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(root, maxVal):
            if not root:
                return
            if root.val>=maxVal:
                res[0]+=1
            dfs(root.left,max(maxVal,root.val))
            dfs(root.right,max(maxVal,root.val))
        dfs(root,float('-inf'))
        return res[0]
        
            

            
        