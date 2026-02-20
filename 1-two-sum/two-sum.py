class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        output = []

        for i, value in enumerate(nums):

            if value in dic:

                dic[value].append(i)

            else:

                dic[value] = [i]

        print(dic)

        for i in dic:

            if target - i in dic and target - i != i:

                output.append(dic[i][0])
                output.append(dic[target-i][0])
                break

            elif target - i in dic and target - i == i and len(dic[i]) >= 2:

                output.append(dic[i][0])
                output.append(dic[i][1])
                break

        return output

        
            
        