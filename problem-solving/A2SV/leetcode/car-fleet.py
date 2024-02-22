class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = sorted(list(zip(position,speed)))
        stack = [pos[-1]]
        for i in range(len(pos)-2,-1,-1):
            _sum = ceil(target - pos[i][0])/pos[i][1]
            prev = ceil(target - stack[-1][0])/stack[-1][1]
            if prev >= _sum:
               continue
            else:
                stack.append(pos[i])
        return len(stack)
            
        # return 3