class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = defaultdict(int)
        dic = defaultdict(int)
        for i in arr1:
            count[i] += 1
        x = 0
    
        for i in range(len(arr2)):
            dic[arr2[i]]  = count[arr2[i]]+x
            x += count[arr2[i]]
        ans = [0]*len(arr1)
        nots = []
   
        index = 0

        for i in arr1:
            index = max(index,dic[i])
            if dic[i] == 0:
               
                nots.append(i)
            else:
                ans[dic[i]-1] = i
             
                dic[i] -= 1

        nots.sort()
        ans[index:] = nots
        return ans

