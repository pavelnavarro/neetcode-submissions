# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node, leftChildren, parent):
            if not node:
                return 

            dfs(node.left,True,node)
            dfs(node.right,False,node)

            if not node.left and not node.right and node.val==target:
                if leftChildren:
                    parent.left = None
                else:
                    parent.right = None
            return
                    
        dfs(root,True,root)

        if root and root.val == target and not root.left and not root.right:
            return None
        return root        