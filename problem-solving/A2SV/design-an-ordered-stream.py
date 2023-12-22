class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.arr = ["0"]*n
        self.counter = 0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        l = []
        
        self.arr[idKey-1] = value
        while(self.arr[self.counter] != "0" and self.counter < len(self.arr)):
            l.append(self.arr[self.counter])
            # print(123)
            self.counter += 1
            if self.counter >= len(self.arr):
                break
        

      
        return l
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)