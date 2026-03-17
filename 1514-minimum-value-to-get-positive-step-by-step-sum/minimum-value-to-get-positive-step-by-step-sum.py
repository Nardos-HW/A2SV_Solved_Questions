class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        total = 0
        min_prefix = 0
        
        for num in nums:
            total += num
            min_prefix = min(min_prefix, total)
        
        return 1 - min_prefix