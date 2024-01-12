class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = {}
        ans = float("inf")
        index = 0
        i = 0
        while(i < len(cards)):
            if cards[i] in dic and dic[cards[i]][1] >= index:
                ans = min(ans,(i - dic[cards[i]][1] + 1))
                index = dic[cards[i]][1] + 1

                dic[cards[i]] = [1,i]
                i+=1
            else:
                dic[cards[i]] = [1,i]
                i += 1
     

        return ans if ans != float("inf") else -1
               