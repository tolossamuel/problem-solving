class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        ans = 0
        level = capacity
        # if level < plants[0]:
        #     level = plants[0]
        for i in range(len(plants)):
            if level >= plants[i]:
                ans += 1
                level -= plants[i]
               
            else:
                print(ans,i,i-1)
                level = capacity-plants[i]
                ans += (i)
                ans += i+1
                print(level,ans)
        
        return ans