import random
class RandomizedSet(object):

    def __init__(self):
        self.sets = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.sets:
            return False
        else:
            self.sets.append(val)
            return True

        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.sets:
            self.sets.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        rand =random.randrange(0, len(self.sets))
        return self.sets[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()