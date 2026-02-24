class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        lst = []
        count = 1

        if len(nums) == 0:

            return 0

        print(nums)

        for i in range(len(nums)-1):

            if nums[i] == nums[i+1] - 1:

                count += 1
            elif nums[i] == nums[i+1] and count > 1:
                continue
            else:

                lst.append(count)
                count = 1

        lst.append(count)

        return max(lst)
        