class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        right = 0
        counter = 0
        while(right < len(students)):
            counter += abs(seats[right] - students[right])
            right += 1
        return counter