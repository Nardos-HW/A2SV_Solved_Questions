class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        initial_sum = 0
        output = []

        for i in nums:

            if i % 2 == 0:

                initial_sum += i

        


        for j in queries:

            i = j[1]

            if (j[0] + nums[i]) % 2 == 0 and nums[i] % 2 == 0:

                initial_sum += j[0]


            elif (j[0] + nums[i]) % 2 == 0 and nums[i] % 2 != 0:

                initial_sum += j[0] + nums[i]

            elif (j[0] + nums[i]) % 2 != 0 and nums[i] % 2 == 0:

                initial_sum = initial_sum - nums[i]

            nums[i] = j[0] + nums[i]

            output.append(initial_sum)

        return output

        