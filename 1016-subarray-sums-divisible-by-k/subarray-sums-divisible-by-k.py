class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0: 1}
        prefix = 0
        res = 0
        for n in nums:
            prefix = (prefix + n) % k
            res += count.get(prefix, 0)
            count[prefix] = count.get(prefix, 0) + 1
        return res       