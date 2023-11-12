class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        sum_of = 0
        team = []
        for i in range(len(skill)//2):
            team.append([skill[i],skill[-1-i]])
        if team:
            skill = team[0][0]+team[0][1]
        for i in range(len(team)):
            if team[i][0]+team[i][1] == skill:
                sum_of +=  (team[i][0]*team[i][1   ])   
            else:
                return -1
        return sum_of