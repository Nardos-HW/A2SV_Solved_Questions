class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        
        diff = [0] * (n + 1)
        for l, r in requests:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        
        freq = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            freq[i] = curr
        
        nums.sort()
        freq.sort()
        
        res = 0
        for i in range(n):
            res = (res + nums[i] * freq[i]) % MOD
        
        return res