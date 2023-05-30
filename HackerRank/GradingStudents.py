def gradingStudents(grades):
    # Write your code here
    def _helper(grade):
        if grade < 38:
            return grade

        difference = 5 - (grade % 5)

        if difference < 3: # round up
            grade += difference

        return grade

    for i in range(len(grades)):
        curr_grade = grades[i]
        grades[i] = _helper(curr_grade)

    return grades

print(gradingStudents([73, 67, 38, 33]))
