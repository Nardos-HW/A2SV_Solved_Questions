from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        dic1 = Counter(word1)
        dic2 = Counter(word2)

        len1, len2 = list(dic1.values()), list(dic2.values())
        set1 = set(word1)
        set2 = set(word2)

        if len(word1) == len(word2) and set1 == set2 and sorted(len1) == sorted(len2):

            return True

        return False

       