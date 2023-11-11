class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # "tree" t 1 r 1 and e = 2 1,1,2 sort by order of the number it appears in the strings 2,1,1, eert
        # dic = {}
        # for _ in s
        # dic[_] = 1
        #  if dic[_] is exist so it update the values
        # dic[_] += 1
        # sort the dic base on the values
        # after sort it create string based on order and the values
        # dic = {}    o(n) it was change based on the values of the array        o(n) 
        # for _ in "tree":
        #     try:
        #         if dic[_]:
        #             dic[_] += 1          0(n)
        #     except:
        #         dic[_] = 1

        # dic = {"t" : 1,"r":1,"e":2,}
        # sort the dic                             O(n^2)       o(n) + o(n^2) +O(n) ====   o(n^2)  time complexity 
        # dic = {"e":2,"r":1,"t":1}
        # result = ""
        # for i in dic("e","r"."t"):
        #     result += (i * dic[i])           O(n)
        # return result
        dic  = {}
        for i in s:
            
            try:
                if dic[i]:
                    dic[i] += 1
            except:
                dic[i] = 1
        new_dic = sorted(dic.items(), key=lambda x:x[1],reverse = True)
        string = ""
       
        for i in new_dic:
            a = i[0]
            x =  i[1]
            string += (a*x)
        return string


