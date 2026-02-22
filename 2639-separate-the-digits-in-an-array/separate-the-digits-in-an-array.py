class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        for i in nums:

            x = str(i)
            lst = list(x)
            output.extend(lst)

        for i in range(len(output)):

            output[i] = int(output[i])

        return output
        