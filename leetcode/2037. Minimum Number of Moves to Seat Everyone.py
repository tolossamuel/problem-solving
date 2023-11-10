class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        counter = 0
        students.sort()
        seats.sort()
        for i in range(len(seats)):
            counter += abs(seats[i]- students[i])
            # print(counter)
        return counter
