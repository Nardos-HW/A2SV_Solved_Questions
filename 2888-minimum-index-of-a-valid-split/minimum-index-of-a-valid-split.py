class Solution(object):
    def minimumIndex(self, nums):
        from collections import Counter
        n = len(nums)
        counts = Counter(nums)
        
        dom_val = -1
        total_freq = 0
        for val, freq in counts.items():
            if freq * 2 > n:
                dom_val = val
                total_freq = freq
                break
        
        prefix_count = 0
        for i in range(n - 1):
            if nums[i] == dom_val:
                prefix_count += 1
       
            if prefix_count * 2 > (i + 1) and (total_freq - prefix_count) * 2 > (n - i - 1):
                return i
                
        return -1