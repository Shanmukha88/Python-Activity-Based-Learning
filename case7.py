marks_matrix = [
    [85, 90, 78],  # Student 1
    [60, 55, 70],  # Student 2
    [92, 88, 95]   # Student 3
]

print("--- Student Total Marks ---")
student_number = 1
for row in marks_matrix:
    total_marks = sum(row)
    print("Student", student_number, "Total Marks:", total_marks)
    student_number += 1

total_students = len(marks_matrix)
total_subjects = len(marks_matrix[0])

print("\n--- Subject Average Marks ---")
for col in range(total_subjects):
    subject_sum = 0
    for row in range(total_students):
        subject_sum += marks_matrix[row][col]
    subject_avg = subject_sum / total_students
    print(f"Subject {col + 1} Average Score: {subject_avg:.2f}")