class FrequencyTracker(object):

    

    def __init__(self):
        self.dic = {}
        self.freq_tracker = {}
        
        

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """

        if number in self.dic:

            old_freq = self.dic[number]
            self.dic[number] = self.dic[number] + 1
            new_freq = self.dic[number]

            if self.freq_tracker[old_freq] == 1:

                del self.freq_tracker[old_freq]

            else:

                self.freq_tracker[old_freq] -= 1

            if new_freq in self.freq_tracker:

                self.freq_tracker[new_freq] += 1

            else:

                self.freq_tracker[new_freq] = 1

        else:

            self.dic[number] = 1
            
            if 1 in self.freq_tracker:

                self.freq_tracker[1] += 1
            
            else:

                self.freq_tracker[1] = 1

        

        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.dic:

            if self.dic[number] == 1:

                del self.dic[number]

                if self.freq_tracker[1] == 1:

                    del self.freq_tracker[1]

                else:

                    self.freq_tracker[1] -= 1

            else:
                old_freq = self.dic[number]

                self.dic[number] = self.dic[number] - 1

                new_freq = self.dic[number]

                if self.freq_tracker[old_freq] == 1:

                    del self.freq_tracker[old_freq]

                else:

                    self.freq_tracker[old_freq] -= 1
                    

                if new_freq in self.freq_tracker :

                    self.freq_tracker[new_freq] += 1

                else:

                    self.freq_tracker[new_freq] = 1

        
        

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        if frequency in self.freq_tracker:

            return True

        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)