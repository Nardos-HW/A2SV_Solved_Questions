class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n = len(names)

        for i in range(1,n):

            currenth = heights[i]
            currentn = names[i]
        
            for j in range(i-1,-1,-1):

                if currenth > heights[j]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]

                else:

                    break

                    
        return names

                    
        