class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i>=len(nums):
                res.append(subset[:])
                return

            #choose the number
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()

            #do not choose the number
            dfs(i+1)
            return

        dfs(0)
        return res
        