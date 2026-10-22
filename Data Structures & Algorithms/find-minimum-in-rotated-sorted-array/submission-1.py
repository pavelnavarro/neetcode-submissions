class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0,len(nums)-1

        while l<=r:
            m = l+ (r-l)//2
            if nums[m]<res:
                res = nums[m]
            
            #second half is not sorted
            if nums[m]>nums[r]:
                l = m+1

            #second half is sorted
            else:
                r = m-1

        return res
        