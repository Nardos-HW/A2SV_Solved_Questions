from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        count = 0
       
        freq = Counter(s)

        for i in t:

            if i in freq and freq[i] > 1:

                freq[i] -= 1

            elif i in freq and freq[i] == 1:

                del freq[i]

            else:

                count += 1

        return count



