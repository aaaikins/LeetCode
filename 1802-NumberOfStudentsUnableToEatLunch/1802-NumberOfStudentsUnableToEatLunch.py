# Last updated: 12/18/2025, 1:50:40 PM
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while counter < len(students):
            if students[0]== sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = 0
            else:
                students.append(students.pop(0))
                counter+=1
        return len(students)

        