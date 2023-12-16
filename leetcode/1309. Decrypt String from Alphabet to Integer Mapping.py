class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = "abcdefghijklmnopqrstuvwxyz"
        counter = 0
        ans = ""
        index = ""

        for i in range(len(s),0,-1):
            if s[i-1] != "#" and counter == 0:
               
                ans = string[int(s[i-1])-1] + ans
               
            elif counter == 3:
               
                counter = 0
               
                ans = string[int(index) - 1] + ans
                if s[i-1] != "#":
                    ans = string[int(s[i-1])-1] + ans
                else:
                    counter +=  1
                index = ""
            else:
                print(s[i-1])
                counter += 1
                if s[i-1] !="#":
                    index = s[i-1] + index
        else:
            if len(index) > 0:
                print(index)
                ans = string[int(index) - 1] + ans

        return ans
        