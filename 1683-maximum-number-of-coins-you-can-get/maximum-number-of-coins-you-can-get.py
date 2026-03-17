class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res = 0
        n = len(piles) // 3
        
        for i in range(n):
            res += piles[2*i + 1]
        
        return res