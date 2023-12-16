class MyHashSet(object):

    def __init__(self):
        self.object = set()
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.object.add(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None

        """
        if self.contains(key):
            self.object.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.object:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)