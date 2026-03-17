from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        cnt = Counter(s)
        res = []
        
        for c in order:
            if c in cnt:
                res.append(c * cnt[c])
                del cnt[c]
        
        for c in cnt:
            res.append(c * cnt[c])
        
        return "".join(res)