class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        sum_of = 0
        right = len(skill)-1
        left = 0
        div = skill[left]+skill[right]
        while(left < right):
            sum_of += (skill[left]*skill[right])
            if div != skill[left]+ skill[right]:
                return -1
            left += 1
            right -= 1
        return sum_of
        