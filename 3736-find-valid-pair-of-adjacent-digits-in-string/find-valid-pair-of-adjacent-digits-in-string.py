class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in s:

            if i in dic:

                dic[i] += 1

            else:

                dic[i] = 1


        for i in range(len(s)-1):

            if dic[s[i]] == int(s[i]) and dic[s[i+1]] == int(s[i+1]) and s[i] != s[i+1]:

                return  s[i:i+2]
                

        return "" 
        