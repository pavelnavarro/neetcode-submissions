class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i,count):
            if count>target or i>=len(nums):
                return
            if count == target:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i,count+nums[i])
            subset.pop()
            dfs(i+1,count)
            
            return
        dfs(0,0)
        return res
            

        