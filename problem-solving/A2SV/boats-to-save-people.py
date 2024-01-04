class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left, right = 0, len(people)-1
        counter = 0
        while left< right:
            if (people[left] + people[right])<= limit:
                left += 1
                right -= 1
                counter += 1
            else:
                right -= 1
        return (len(people) - counter)