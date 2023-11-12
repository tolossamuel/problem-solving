class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        
        left = 0
        right = 0
        counter = 0
        while (left < len(players) and right < len(trainers)):
            if players[left]<= trainers[right]:
                counter += 1
                left += 1
                right += 1
            else:
                right += 1
        return counter
