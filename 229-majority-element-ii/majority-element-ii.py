class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        tracker = {}
        output = []
        n = len(nums)
        freq = n // 3

        for i in nums:

            if i in tracker:
                tracker[i] += 1

            else:
 
                tracker[i] = 1

        for i in tracker:

            if tracker[i] > freq:

                output.append(i)

        return output
        