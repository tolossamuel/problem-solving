class Solution:
    def recurtions(self,nums,player1,player2):
        if not nums:
            
            if player1 >= player2:
                return True
            return False
        left = 0
        right = 0
        left1 = 0
        right1 = 0
        if len(nums) > 2:
            left = nums[1]
            right = nums[-2]
            left1 = nums[0]
            right1 = nums[-1]
        # print(player1,player2)
        return (self.recurtions(nums[2:],player1 + nums[0],player2 + left) and self.recurtions(nums[1:len(nums)-1],player1 + nums[0],player2 + right1)) or (self.recurtions(nums[:-2],player1 + nums[-1],player2 + right) and self.recurtions(nums[1:len(nums)-1],player1 + nums[-1],player2 + left1))
    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.recurtions(nums,0,0)
       