class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(pool):
            if len(subset)>=len(nums):
                res.append(subset[:])
                return

            for i in range(len(pool)):
                subset.append(pool[i])
                dfs(pool[:i]+pool[i+1:])
                subset.pop()
        
        dfs(nums)
            
        return res
