class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]

        strs.sort(key = lambda x : len(x) )
        
        for i in range(len(strs[0])):

            for j in range(1,len(strs)):

                if strs[0][i] != strs[j][i]:

                    if i == 0:
                        return ""

                    return strs[0][0:i]
        return strs[0]