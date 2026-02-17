class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        double_tracker = {}

        for i in nums:

            if i in double_tracker:

                double_tracker[i] += 1

            else:

                double_tracker[i] = 1

        for i in double_tracker:

            if double_tracker[i] == 1:

                return i 
        