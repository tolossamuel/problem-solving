class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        # self.counter = 0
        self.dic = {}
        self.time = timeToLive

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.dic[tokenId] = currentTime + self.time
        

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        # print(self.dic)
        if tokenId in self.dic and self.dic[tokenId] > currentTime:
            self.dic[tokenId] = currentTime + self.time
        # elif self.dic[tokenId] == 0:
        #     self.dic[tokenId] = max(self.dic[tokenId],(currentTime+self.time))

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        # print(currentTime,self.dic)
        counter = 0
        for key in self.dic:
            if self.dic[key] > currentTime:
                counter += 1
        return counter
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)