class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        ans = 0
        level = capacity
        for i in range(len(plants)):
            if level >= plants[i]:
                ans += 1
                level -= plants[i]
               
            else:
                level = capacity-plants[i]
                ans += (i)
                ans += i+1
        
        return ans