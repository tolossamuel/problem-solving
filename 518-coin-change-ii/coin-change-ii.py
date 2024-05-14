class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        catch = {}
        def solve(index,amount):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if index >= len(coins):
                return 0
            if (index,amount) in catch:
                return catch[(index,amount)]
            ans =  (solve(index,amount - coins[index]) + solve(index + 1,amount))
            catch[(index,amount)] = ans
            return ans
        return solve(0,amount)