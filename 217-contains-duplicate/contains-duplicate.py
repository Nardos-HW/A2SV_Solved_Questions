class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {}

        for i in nums:

            if i in freq:

                return True

            else:

                freq[i] = 1

        return False