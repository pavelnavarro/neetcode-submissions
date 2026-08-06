class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        def dfs(i,count):
            if count == target:
                res.append(subset[:])
                return
            if i>=len(candidates) or count>=target:
                return
            
            subset.append(candidates[i])
            dfs(i+1,count+candidates[i])
            subset.pop()
            while i+1 < len(candidates) and candidates[i+1]==candidates[i]:
                i+=1

            dfs(i+1,count)
            

        
        dfs(0,0)
        return res
        

        