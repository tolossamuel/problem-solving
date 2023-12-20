class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        dic  = ["adfghjkls","eiopqrtuwy","bcmnvxz"]
        for i in  words:
            
            for x in range(3):
                flag = True
                for y in i:
                    if y.lower() not in dic[x]:
                        flag = False
                        break
                else:
                    flag = True
                if flag:
                    ans.append(i)

                    break

                
        return ans