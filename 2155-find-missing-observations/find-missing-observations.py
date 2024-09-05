class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        _sum = sum(rolls)
        length = len(rolls) + n
 
        val = (mean * length) - _sum
        if val < 0 or val < n:
            return []
        ans = val//n
        arr = [ans] * n
        x = 0
        remider = val%n
      
        while(remider):
            arr[x%len(arr)] += 1
            remider -= 1
            x += 1
  


        if ans > 6 or arr[0] > 6:
            return []
      

        return arr

