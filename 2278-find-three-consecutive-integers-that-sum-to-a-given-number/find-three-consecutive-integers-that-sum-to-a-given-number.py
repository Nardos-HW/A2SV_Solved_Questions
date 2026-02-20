class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        output = []
        if num % 3 == 0:

            mid = num // 3
            output.append(mid-1)
            output.append(mid)
            output.append(mid+1)

        return output

            

            