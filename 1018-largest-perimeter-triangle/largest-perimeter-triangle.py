class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        ans = 0

        for i in range(len(nums)-2):

            if nums[i+2] > nums[i] - nums[i+1]:

                return nums[i] + nums[i+1] + nums[i+2]

        return 0 
            

        return(ans)

