class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = 0
        catch = {}
        def travel(amount,index):
            nonlocal counter
            if index == len(nums):
                if amount == target:
                    counter += 1
                    return 1
                return 0
            if (index,amount) in catch:
                if (catch[(index,amount)]):
                    counter += catch[(index,amount)]
                return catch[(index,amount)]
            res = 0
            res += travel(amount - nums[index],index + 1)
            res += travel(amount + nums[index], index + 1)
            catch[(index,amount)] = catch.get((index,amount),0) + res
            return res
        travel(0,0)
        return counter