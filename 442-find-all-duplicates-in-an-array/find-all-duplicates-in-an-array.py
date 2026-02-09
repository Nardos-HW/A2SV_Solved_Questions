class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        dic = {}

        for i in nums:

            if i in dic:
                dic[i] = 2

            else:
                dic[i] = 1

        output = []
        for i in dic:
            if  dic[i] == 2:
                output.append(i)

        return output
        