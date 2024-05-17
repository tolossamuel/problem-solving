class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        catch = {}
        nums.sort()
        # counter = 0
        def solve(amount):
            if amount == target:
                return 1
            if amount > target:
                return 0
            if amount in catch:
                
                return catch[amount]
            counter = 0
            for num in nums:
                if amount + num > target:
                    break
                counter += solve(amount + num)
            
            catch[amount] = counter
            return counter
         
        solve(0)
        return catch[0]

        # [3,4,5,6,7,10]