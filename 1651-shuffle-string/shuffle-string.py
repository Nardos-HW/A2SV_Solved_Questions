class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        check = {}

        for i in range(len(s)):

            check[indices[i]] = s[i]

        output = [0] * len(s)

        

        for i in check:

            output[i] = check[i]

        return "".join(output)
        