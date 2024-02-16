class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        counter = 0
        pos = target
        while(pos > 1):
            if maxDoubles > 0 and (pos % 2) == 0:
                # print
                pos //= 2
                maxDoubles -= 1
            elif maxDoubles == 0:
                return counter + pos-1
            else:
                pos -= 1
            # print(pos)
            counter += 1
        return counter