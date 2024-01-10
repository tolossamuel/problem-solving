class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        checked = set()
        n = len(nums)
        for i in range(n):
            if i not in checked:
                visited = set()
                while(True):
                    if i in visited :
                        return True
                    visited.add(i)
                    checked.add(i)
                    pre,i = i , (i +nums[i])%n
                    
                    if pre == i:
                        break
                    if nums[pre] > 0 != nums[i] < 0:
                        break
        return False