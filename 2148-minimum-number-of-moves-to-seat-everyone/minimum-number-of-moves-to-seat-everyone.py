class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        left = 0
        right = 0
        counter = 0
        while(left < len(seats) and right < len(students)):
            counter += abs(seats[left] - students[right])
            right += 1
            left += 1
        return counter