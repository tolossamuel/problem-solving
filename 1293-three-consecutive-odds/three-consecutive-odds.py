class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter =0 
        for x in arr:
            if x%2 == 1:
                counter += 1
            else:
                counter = 0
            if counter >= 3:
                return True
        return False