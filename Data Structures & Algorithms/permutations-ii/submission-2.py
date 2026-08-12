class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(pool):
            if len(subset)>=len(nums):
                res.append(subset[:])
            
            for i in range(len(pool)):
                if i>0 and pool[i]==pool[i-1]:
                    continue
                subset.append(pool[i])
                dfs(pool[:i]+pool[i+1:])
                subset.pop()

        
        dfs(nums)
        return res
        