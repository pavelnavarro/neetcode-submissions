# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False

        def dfs(node):
            if not node:
                return False

            l = dfs(node.left)
            r = dfs(node.right)
            
            if node.val == subRoot.val:
                if self.isSameTree(node,subRoot):
                    return True
            
            return l or r

        return dfs(root)
    
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        l = self.isSameTree(p.left,q.left)
        r = self.isSameTree(p.right,q.right)

        if not l or not r:
            return False
        return True

        
        

        