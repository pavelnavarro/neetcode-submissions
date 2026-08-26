class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        return max((self.robHouse(nums,0,len(nums)-1,1)),(self.robHouse(nums,(len(nums)-1),0,-1)))
    
    def robHouse(self,nums,start,end,direction):
        house1,house2 = 0,0
        for i in range(start,end,direction):
            temp = house2
            house2 = max((nums[i]+house1),house2)
            house1 = temp
        return house2
        
        
        