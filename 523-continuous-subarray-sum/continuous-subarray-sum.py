class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        mod_map = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            mod = total % k

            if mod in mod_map:
                if i - mod_map[mod] > 1:
                    return True
            else:
                mod_map[mod] = i

        return False