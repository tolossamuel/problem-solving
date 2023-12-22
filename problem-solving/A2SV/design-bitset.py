class Bitset(object):

    def __init__(self, size):
        """
        :type size: int
        """
        
        self.bit = "0"*size
        self.ones = "1"*size
        self.zeros = "0"*size 
        self.counter = 0

    def fix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if self.bit[idx] == "0":
            self.counter += 1
            self.bit = self.bit[:idx] + "1" + self.bit[idx+1:]
            # self.bit[idx] = self.bit[:idx] + "1" + self.bit[idx+1:]
            self.zeros = self.zeros[:idx] + "1" + self.zeros[idx+1:]
            self.ones = self.ones[:idx] + "0" + self.ones[idx+1:]
      
        
    def unfix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        # print(123)
        # print(self.bit)
        if self.bit[idx] == "1":
            self.counter  -= 1
            self.bit = self.bit[:idx] + "0" + self.bit[idx+1:]
            # self.bit[idx] = self.bit[:idx] + "1" + self.bit[idx+1:]
            self.zeros = self.zeros[:idx] + "0" + self.zeros[idx+1:]
            self.ones = self.ones[:idx] + "1" + self.ones[idx+1:]
        

    def flip(self):
        """
        :rtype: None
        """
        # print(self.bit)
        self.bit = self.ones
        self.ones,self.zeros = (self.zeros),(self.ones)
        self.counter  = abs(self.counter - len(self.bit))
        # print(self.bit)
        # print(self.ones)
        # print(self.zeros)
        # print(self.bit)

    def all(self):
        """
        :rtype: bool
        """
        if self.counter == len(self.bit):
            return True
        return False
        

    def one(self):
        """
        :rtype: bool
        """
        if self.counter >= 1:
            return True
        return False

    def count(self):
        """
        :rtype: int
        """
       
        return self.counter

    def toString(self):
        """
        :rtype: str
        """
        return self.bit


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()