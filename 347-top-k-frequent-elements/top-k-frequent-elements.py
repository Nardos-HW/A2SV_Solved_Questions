from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        lst = []
        output = []

        freq2 = {}

        for i in freq:

            if freq[i] in freq2:

                freq2[freq[i]].append(i)

            else:

                freq2[freq[i]] = [i]

        for num in freq2:

            lst.append(num)

        lst.sort()
        lst.reverse()

        i = 0
        count = 1

        print(freq)
        print(freq2)

        while count <= k:

            f = freq2[lst[i]]

            if len(f) > 1:

                output.append(f[-1])
                f.pop()
                count += 1
                continue

            else:
                output.append(f[0])
                count += 1
                i += 1

        return output


            
        

