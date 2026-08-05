class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i,count):
            if i==len(nums) or count>target:
                return
            if count==target:
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i,count+nums[i])
            subset.pop()

            dfs(i+1,count)

                

        dfs(0,0)
        return res

        