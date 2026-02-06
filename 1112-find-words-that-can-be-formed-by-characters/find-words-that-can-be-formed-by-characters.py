class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        
        
        tot = 0
        temp = chars

        

        for i in words:

            chars = list(chars)

            for j in i:

                if j in chars :

                    chars.remove(j)
                    continue

                else:
                    
                    break
            else:
                tot += len(i)
                
            chars = temp

        return tot






        