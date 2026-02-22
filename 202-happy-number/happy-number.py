class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        collection = set()

        while True:

            x = 0

            for i in str(n):

                x += int(i)**2
                
            if x == 1:

                return True

            elif x in collection:

                return False
            collection.add(x)
            n = x


        