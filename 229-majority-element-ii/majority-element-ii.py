class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        cnt = {}
        
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        
        for key in cnt:
            if cnt[key] > n // 3:
                res.append(key)
        
        return res