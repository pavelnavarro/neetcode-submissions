# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root,maxVal):
            nonlocal res

            if not root:
                return

            if maxVal<=root.val:
                res+=1
            
            dfs(root.left,max(root.val,maxVal))
            dfs(root.right,max(root.val,maxVal))

        dfs(root,float("-inf"))

        return res

        
            

            
        