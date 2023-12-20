class ATM(object):

    def __init__(self):
        self.dic = {20:0,50:0,100:0,200:0,500:0}
    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
       
        self.dic[20] += banknotesCount[0]
        self.dic[50] += banknotesCount[1]
        self.dic[100] += banknotesCount[2]
        self.dic[200] += banknotesCount[3]
        self.dic[500] += banknotesCount[4]
        

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        ans = 0
        val = amount
        returnVal = [0,0,0,0,0]
        check  = {500:0,200:0,100:0,50:0,20:0}
        for i in [500,200,100,50,20]:
            if  val >= i and ans < amount:
                # print(i,ans,val)
                x = min(self.dic[i],val//i)
            
                ans +=(x*i)
                val -= (x*i)
                check[i] += x
        print(ans)
        if ans == amount:
            print(ans)
            self.dic[500] -= check[500]
            returnVal[-1] = check[500]
            self.dic[200] -= check[200]
            returnVal[-2] = check[200]
            self.dic[100] -= check[100]
            returnVal[-3] = check[100]
            self.dic[50] -= check[50]
            returnVal[-4] = check[50]
            self.dic[20] -= check[20]
            returnVal[-5] = check[20]
            return returnVal
        else:
            return [-1]
                
            
        

                


        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)