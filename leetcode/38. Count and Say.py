class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def recurtions(string,index,n):
          if index == n:
            return string
          else:
            ans = ""
            counter = 1
            for i in range(1,len(string)):
              if string[i] != string[i-1]:
                ans += (str(counter)+string[i-1])
                counter  = 1
              else:
                counter += 1
            else:
              ans += (str(counter)+string[len(string)-1])
            
            return recurtions(ans,index+1,n)
        return recurtions("1",1,n)
        

