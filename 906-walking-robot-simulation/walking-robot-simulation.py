class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dic = defaultdict(int)
        for i in obstacles:
            dic[(i[0],i[1])] = 1
        move = [0,1,2,3]
        dir = 0

        pos = [0,0]
        ans = 0
        for i in commands:
            if i == -2:
                dir = move[(dir -1)%4]
            elif i == -1:
                dir = move[(dir + 1)%4]
            else:
                for y in range(1,i+1):
                    
                    if dir == 0:
                        if (pos[0],pos[1]+1) in dic:
                            break
                        pos[1]+= 1
                    elif dir == 1:
                        if (pos[0]+1,pos[1]) in dic:
                            break
                        pos[0] += 1
                    elif dir == 2:
                        if (pos[0],pos[1]-1) in dic:
                            break
                        pos[1] -= 1
                    else:
                        if (pos[0]-1,pos[1]) in dic:
                            break
                        pos[0] -= 1
                ans = max((pos[0]**2 + pos[1]**2),ans)
              
        return ans
