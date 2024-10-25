# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        arr = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]
        arr[0][src] = 0
      
        
        graph = defaultdict(list)
        for x,y,z in flights:
            graph[x].append((y,z))
        start = deque([(0,src)])
        index = 1
        while(start):
            if index > n:
                break
           
            length = len(start)
           
            for _ in range(length):
                _sum,curr = start.popleft()
                arr[index][curr] = min(arr[index][curr],_sum,arr[index-1][curr])
                for x,y in graph[curr]:
                    
                    if (_sum + y ) < arr[index][x]:
                        start.append((_sum + y, x))
                    
                        arr[index][x] = min(arr[index][x],_sum + y,arr[index-1][x])
                
                    arr[index][x] = min(arr[index-1][x],arr[index][x])
        
            index += 1
  
        if len(arr) < (k+1):
            return -1
        

        if index < n:
            k = min(index-2,k)
       
        if arr[k+1][dst] == float("inf"):
            return -1
        return arr[k+1][dst]
                
