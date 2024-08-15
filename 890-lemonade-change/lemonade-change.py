class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0,0]
        for x in  bills:
            if x == 5:
                change[0] += 1
            elif x == 10:
                if change[0] > 0:
                    change[0] -= 1
                    change[1] += 1
                else:
                    return False
            else:
                if change[1] > 0 and change[0] >= 1:
                    change[1] -= 1
                    change[0] -= 1
                    change[2] += 1
                elif change[0] >= 3:
                    change[0] -= 3
                    change[2] += 1
                else:
                    return False
        return True