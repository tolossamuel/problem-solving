class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start <= destination:
            x = sum(distance[start:destination])
            y = sum(distance[destination:]) + sum(distance[:start])
            return (min(x,y))
        else:
            
            x = sum(distance[destination:start])
            y = sum(distance[start:]) + sum(distance[:destination])
            print(x,y)
            return (min(x,y))
        