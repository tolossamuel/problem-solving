class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        dic = Counter(nums)
        k = list(dic.keys())
        heapify(k)
        counter = 0
        while(k):
            i = heappop(k)
            if dic[i] > 1:
                counter  += dic[i]-1
                if (i+1) in dic:
                    dic[i+1] += dic[i]-1

                else:
                    dic[i+1] = dic[i]-1
                    heappush(k,i+1)
        return counter    

        # 1 1 2 2 3 7
        # 