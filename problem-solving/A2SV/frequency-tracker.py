class FrequencyTracker(object):

    def __init__(self):
       
        self.freq = defaultdict(int)
        self.freqCounter = defaultdict(int)
        
    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        # print(self.freq)
        # print(self.freqCounter)
        self.freqCounter[self.freq[number]] -= 1
        self.freq[number] += 1
        
        self.freqCounter[self.freq[number]] += 1
        # print(self.freq)
        # print(self.freqCounter)
        # print(123)
    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        
        if self.freq[number]>0:
            self.freqCounter[self.freq[number]] -= 1
            self.freq[number] -= 1
            self.freqCounter[self.freq[number]] += 1
    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        # print(self.freq)
        # print(self.freqCounter)
        if self.freqCounter[frequency] >0:
            # print(1234)
            return True
        return False

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)