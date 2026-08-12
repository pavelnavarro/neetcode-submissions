class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def dfs(openP,closeP):
            if openP==n and closeP==n:
                res.append("".join(subset))
            if openP>n or closeP>openP:
                return
            
            subset.append("(")
            dfs(openP+1,closeP)
            subset.pop()
            
            subset.append(")")
            dfs(openP,closeP+1)
            subset.pop()

        
        dfs(0,0)
        return res
        

        