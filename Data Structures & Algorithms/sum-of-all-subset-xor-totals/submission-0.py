class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i,count):
            if i>=len(nums):
                return count

            return dfs(i+1,count^nums[i]) + dfs(i+1,count)

        return dfs(0,0)
        