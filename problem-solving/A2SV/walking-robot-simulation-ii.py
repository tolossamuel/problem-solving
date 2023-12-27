class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.dir = "East"
        self.total = 2*(height) + (2*(width - 1)-1)
        self.pos = [0,0]
        self.width = width
        self.height = height
        self.current = 0

    def step(self, num):
        # print(self.total)
        """
        :type num: int
        :rtype: None
        """

        num += self.current
        totalStep = self.total 
        self.current += (num - self.current)
     
        # print(self.height + self.width-1)
        if num >= (totalStep-1):
            num %= (totalStep-1)
            if num == 0:
                self.pos = [0,0]
                self.dir = "South"
        if num >= (totalStep - self.height ):
            num -=(totalStep - self.height)
            if num == 0:
                self.pos = [0,self.height-1]
                self.dir = "West"
            elif num < self.height:
                self.pos = [0,(self.height - num-1)]
                self.dir = "South"

        elif num >= (self.height + self.width-2):
            num -= (self.height + self.width-2)
            if num == 0:
                self.pos = [self.width-1,self.height-1]
                self.dir = "North"
            elif num < self.width:
                self.pos = [self.width-1-num,self.height-1]
                self.dir = "West"
        elif num >= (self.width-1):
            num -= (self.width-1)
            if num == 0:
                self.pos = [self.width-1,0]
                self.dir = "East"
            else:
                self.pos = [self.width-1,num]
                self.dir = "North"
        elif num > 0:
            self.pos = [num,0]
            self.dir = "East"
            num = 0 
    def getPos(self):
        """
        :rtype: List[int]
        """
        return self.pos
    def getDir(self):
        """
        :rtype: str
        """
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()