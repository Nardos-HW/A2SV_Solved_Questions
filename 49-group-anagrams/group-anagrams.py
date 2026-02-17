class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        container = {}
        output = []

        for i in strs:

            temp = "".join(sorted(i))

            if temp in container:

                container[temp].append(i)

            else:

                container[temp] = []
                container[temp].append(i)

        for i in container:

            output.append(container[i])

        return output
        
        