class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost0, cost1 = 0,0
        for i in range(len(cost)):
            temp = cost1
            cost1 = cost[i]+min(cost0,cost1)
            cost0 = temp
        return min(cost0,cost1)

        
            