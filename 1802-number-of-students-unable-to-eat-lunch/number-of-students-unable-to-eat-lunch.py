class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zero = students.count(0)
        one = students.count(1)
        students = deque(students)
        sandwiches = deque(sandwiches)
        while(True):
            if not sandwiches or not students:
                return len(students)
            if sandwiches[0] == students[0]:
                x = students.popleft()
                sandwiches.popleft()
                if x == 1:
                    one -= 1
                else:
                    zero -= 1
            elif sandwiches[0] != students[0]:
                if sandwiches[0] == 1 and one == 0:
                    return len(students)
                elif sandwiches[0] == 0 and zero == 0:
                    return len(students)
                else:
                    students.append(students.popleft())
        