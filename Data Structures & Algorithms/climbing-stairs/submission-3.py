class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return n

        steps = [1,1]
        for i in range(n-1):
            temp = steps[0]
            steps[0]=steps[0]+steps[1]
            steps[1]=temp
        return steps[0]
        